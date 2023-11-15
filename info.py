from rich.table import Table

logo = '''
██╗     ██╗   ██╗███╗   ██╗ █████╗ ██████╗      ██████╗ ██████╗ ██╗███╗   ██╗███████╗
██║     ██║   ██║████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██║████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║███████║██████╔╝    ██║     ██║   ██║██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╗██║██╔══██║██╔══██╗    ██║     ██║   ██║██║██║╚██╗██║╚════██║
███████╗╚██████╔╝██║ ╚████║██║  ██║██║  ██║    ╚██████╗╚██████╔╝██║██║ ╚████║███████║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
'''

overview = '''
The goal of the game is to turn all the new moons 🌑 into full moons 🌕.
By default, you have 5 turns.
Each turn you are given a randomly generated rack of letters.
Most tiles fill one moon 🌕.
Special tiles (denoted by bolded and underlined letters) fill two moons 🌝🌝.
Fill all moons in 5 words or less to win.

Also, you can enter '!q' or '!quit' to quit a game prematurely and start a new game (with custom settings perhaps?).
Another one is '!faq' for bringing up the FAQs.
'''

faq = '''
Q: What happens if I spell an invalid word?
A: Nothing, there's no penalty like a lost turn or anything. Just spell a word again until you get a valid one. Be sure to use at least 3 tiles!

Q: Help. I can't spell anything. I got softlocked. What do I do?
A: Enter '!q' in the input prompt to quit the game and be brought to the options screen where you can customize the number of turns, tiles, etc. 

Q: What are those tiles with underlined letters? 
A: They are super/lunar tiles and they fill two moons.
'''

# postgame_message = '''
# This game was a recreation (*cough* ripoff *cough*) of the Golden Coins minigame in Bookworm Adventures Vol. 2. Like in the original, the coin grid is 5 rows * 7 columns and you have 5 turns.

# Lunar Coins has some cool new features though, including:
# - Listing the hint for the longest possible word in the rack (in case you like hunting for the longest word a la Text Twist.)
# - Tabulating the logs of the current game, including a list of best possible words.
# - Changing the number of tiles, rows and columns in the coin grid, and turns (to make the game easier or harder).
# '''

options_table = Table(title="Settings")
for header in ["Setting", "Description", "Minimum", "Maximum", "Default"]:
     options_table.add_column(header)


table_rows = [
    ["Number of Tiles", "Sets the max. word length.", "10", "16", "12"],
    ["Number of Rows", "Sets the number of rows in the moon grid.", "1", "20", "5"],
    ["Number of Columns", "Sets the number of columns in the moon grid.", "4", "20", "7"],
    ["Number of Turns", "Sets the number of turns. If you want a shorter or longer game.", "1", "100", "5"],
    ["Longest Word Hint", "Shows the length of the longest possible word in the rack.", "n/a", "n/a", "True"],
    ["History Table", "Shows the history/log of the game so far.", "n/a", "n/a", "True"],
    ]


for row in table_rows:
    options_table.add_row(*row)


game_modes_table = Table(title="Game Modes", caption="Warning! Modes other than Classic are not balanced. The settings for Custom and Random adhere to the minimums and maximums listed in the Settings table above.")
for header in ["Key", "Game Mode", "Word Length/Tile Count", "Moon/Coin Grid Size", "Turns"]:
     game_modes_table.add_column(header)

table_rows = [
    ["1", "Classic", "12", "5 rows * 7 columns = 35 moons", "5"],
    ["2", "EasyMode", "16", "4 rows * 5 columns = 20 moons", "7"],
    ["3", "HardMode", "10", "6 rows * 8 columns = 48 moons", "6"],
    ["4", "Custom", "Custom", "Custom", "Custom"],
    ["5", "Random", "Random", "Random", "Random"],
    ]

for row in table_rows:
    game_modes_table.add_row(*row)


keep_prompt_msg = '''Keep longest word hint and history table? [1/2/3/4]
1 - Keep both. (recommended for the QoL)
2 - Keep hint only.
3 - Keep history table only.
4 - Hide both. (for a more vanilla experience)
'''

# Minigame recreated by raynsquall