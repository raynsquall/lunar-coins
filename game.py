import random
from collections import Counter
from typing import List

from rich import box
from rich.console import Console
from rich.table import Table

# Color source: https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
RACK_LETTER_COLOR = "purple4"
RACK_BACKGROUND_COLOR = "light_cyan1"

console = Console()

# Letter distribution, in descending order of frequency to be used for random.choices(). Credits to MHTAL#7800
letter_distribution = {
    "E": 13.0, "A": 9.32, "R": 7.52, "I": 7.23, "T": 6.84, "O": 6.63, "S": 5.94,
    "N": 5.47, "L": 4.66, "U": 4.28, "D": 3.76, "P": 2.61, "G": 2.57, "Y": 2.52,
    "H": 2.52, "F": 2.35, "C": 2.18, "M": 2.14, "V": 1.71, "B": 1.71, "W": 1.54,
    "Qu": 1.15, "J": 0.77, "X": 0.60, "K": 0.56, "Z": 0.42,
}

letters, percentages = zip(*letter_distribution.items())

# Parses the wordlist, retrieved from http://dugongue.com/BookwormAdventures/ba2-wordlist.txt
with open("wordlist.txt") as word_list:
    word_bank : List[str] = [word.strip().upper() for word in word_list]

class LunarCoins():
    
    def __init__(self, 
                 max_word_length : int = 12,
                 rows : int = 5,
                 columns : int = 7,
                 turns : int = 5):
        self.max_word_length = max_word_length
        self.rows, self.columns = rows, columns
        self.turns = turns

        # Count the super/lunar tiles (worth double the normal tiles). It takes the number of turns, makes the first and last turns be 0 and 3 tiles respectively. In the middle of them, 67% have 1 tile and 33% have 2. If there is only 1 turn then it will just be 3 lunar tiles.
        self.super_tiles_count : List[int] = [0] * 1 + [1] * round((2 / 3) * (turns - 2)) + [2] * round((1 / 3) * (turns - 2)) + [3] * 1 if turns != 1 else [3]
        self.word_bank : List[str] = [word for word in word_bank if len(word) <= self.max_word_length]
        self.coins : int = 0
        self.coin_seq : List[int] = []
        self.coin_seq_for_current_word : List[int] = []
        self.word_count : int = 0
        self.rack : List[str] = []
        self.legal_words : List[str] = []
        self.longest_words : List[str] = []
        self.point_values : List[int] = []


        self.new_moons = ["🌑"] * rows * columns
        self.history_table = Table()
        for header in ["Previous Rack", "Best Possible Words", "Your Word", f"Full Moons (Goal: {rows * columns})", "[underline]Lunar Tiles Used"]:
            self.history_table.add_column(header)

        self.word_played : List[str] = []
        
    def draw_tiles(self) -> List[str]:
        self.rack = [random.choices(letters, percentages)[0] for _ in range(self.max_word_length)]
        return self.rack
    

    def get_longest_words(self) -> List[str]:
        # Filter the word bank such that words are not longer than the max_word_length. The 'QU's in word bank are replaced with a singular 'Qu' string so that they can be compared with the 'Qu' generated in the random rack (otherwise, 'QU' will be processed as 'Q', 'U' and not 'Qu'). Use the Counter() class to only include those words whose letters (tiles) are a subset of the current rack's tiles.
        self.legal_words : List[str] = [word for word in word_bank if len(word) <= self.max_word_length and Counter([letter if letter != "Q" else "Qu" for letter in word.replace("QU", "Q")]) <= Counter(self.rack)]

        # Sort above list in descending order of length and slice to get only the first 5 words in the list.
        self.longest_words = sorted(self.legal_words, key=lambda x: len(x), reverse=True)[:5]
        return self.longest_words
    

    def display_tiles(self) -> None:
        # Generate a default list of the length max_word_length, taking into account the number of super tiles for the current turn and shuffling afterwards.
        self.point_values = [1] * (self.max_word_length - self.super_tiles_count[self.word_count]) + [2] * self.super_tiles_count[self.word_count]
        random.shuffle(self.point_values)

        table_rows = [
            [letter if value == 1 else "[bold underline]" + letter for letter, value in zip(self.rack, self.point_values)]
        ]
        tile_table = Table(box=box.HEAVY, show_header=False)
        for row in table_rows:
            tile_table.add_row(*row)
        console.print(tile_table, style=f"{RACK_LETTER_COLOR} on {RACK_BACKGROUND_COLOR}")

    def display_history(self) -> None:
        self.history_table.add_row(''.join(self.rack), 
                                   ' '.join(self.longest_words), 
                                   ''.join(self.word_played),  
                                   f"{self.coins} {"" if self.word_count < 1 else f"(+{sum(self.coin_seq_for_current_word)})"}",
                                   f"{self.coin_seq_for_current_word.count(2)} of {self.super_tiles_count[self.word_count]}")
        
        console.print(self.history_table)
        

    def determine_legality(self, word) -> bool:
        # Turn the input word into a list of tiles, converting QUs (if any) into single Qu tiles.
        self.word_played = [letter if letter != "Q" else "Qu" for letter in word.replace("QU", "Q")]

        # Check whether the word is in the legal word list generated above and whether the word is a subset of the rack.
        if word in self.legal_words and Counter(self.word_played) <= Counter(self.rack):
            self.calculate_coin_seq()
            return True
        else:
            return False

    def calculate_coin_seq(self) -> None:
        # Zip the letters and point values of the tiles in the current rack. Sort them in descending order of points (which are just 1 or 2 so [1,1,2,1,2] becomes [2,2,1,1,1]) so that super tiles are first in the list (The reason for doing this is that there could be two tiles of the same letter with one being a normal tile and the other super. If only one of the tiles is used and the normal tile comes before the super tile, then the normal tile is used since it is the first match in the word-to-rack comparison loop. We obviously don't want that so we have to give super tiles priority by doing this.). Unzip letters and point values, converting them back into lists. Compare the word_played (word as a list). Go through each letter where if a match is found, add either 1 or 2 in the coin sequence list, delete the matched entry in the unzipped points list and rack list.
        sorted_letter_value_pairs = sorted(list(zip(self.rack, self.point_values)), key=lambda x: x[1], reverse=True)
        rack, points = map(list, zip(*sorted_letter_value_pairs))
        self.coin_seq_for_current_word = []
        for letter in self.word_played:
            if letter in self.rack:
                self.coin_seq_for_current_word.append(points[rack.index(letter)])
                del points[rack.index(letter)]
                rack.remove(letter)
        self.coin_seq.extend(self.coin_seq_for_current_word)
        self.coins += sum(self.coin_seq_for_current_word)


    def display_grid_coins(self) -> None:
        # Generate special indices so that the order of new moon 🌑 to full moon 🌕 replacement is from left to right but starting from the bottom row and ending in the top row instead of the default top row to bottom row.
        indices = [element for row in  [(list(range(-(n + 1) * self.columns, -n * self.columns))) for n in range(self.rows)] for element in row]
        spec_index = 0
        for count in self.coin_seq:
            for _ in range(count):
                if spec_index < self.rows * self.columns:
                    self.new_moons[indices[spec_index]] = "🌕" if count == 1 else "🌝" # if count == 2
                    spec_index += 1

        # Display the grid in accordance to the number of columns. If the index + 1 is divisible by the column count then start a new row.
        for index, coin in enumerate(self.new_moons):
            print(coin, end=' ')
            if (index + 1) % self.columns == 0:
                print("\n", end='')

    def score(self) -> int:
        '''to be added in the future?'''
        pass
