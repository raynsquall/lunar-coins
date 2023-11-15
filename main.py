from game import LunarCoins

from info import logo, overview, options_table, game_modes_table, keep_prompt_msg, faq
from rich.console import Console
from rich.table import Table
from typing import List
import random

console = Console()

print(logo)
print(overview)

show_hint = True
show_table = True

def true_if_in_choice(answer : str, choice_list : List[int]) -> bool:
    if not answer.isdigit() or not (int(answer) in choice_list):
        print(f"The choices are limited to {', '.join([str(num) for num in choice_list])}.")
        return False        
    else:
        return True

game = LunarCoins()

def pre_game_init():
    console.print(options_table)
    console.print(game_modes_table)
    print()
    while True:
        game_mode = input("Choose a game mode: [1/2/3/4/5] (Refer to table above.): ").strip()
        if true_if_in_choice(game_mode, [1, 2, 3, 4, 5]):
            game_mode = int(game_mode)
            global game
            if game_mode == 1:
                game = LunarCoins()
            elif game_mode == 2:
                game = LunarCoins(max_word_length = 16, rows = 4, columns = 5, turns = 7)
            elif game_mode == 3:
                game = LunarCoins(max_word_length = 10, rows = 6, columns = 8, turns = 6)
            elif game_mode == 4:
                while True:
                    max_word_len = input("Enter the desired number of tiles per rack [min: 10; max: 16]: ").strip()
                    if true_if_in_choice(max_word_len, list(range(10, 17))):
                        break
                while True:
                    number_of_rows = input("Enter the desired number of rows in the moon grid [min: 1; max: 20]: ").strip()
                    if true_if_in_choice(number_of_rows, list(range(1, 21))):
                        break
                while True:
                    number_of_cols = input("Enter the desired number of columns in the moon grid [min: 4; max: 20]: ").strip()
                    if true_if_in_choice(number_of_cols, list(range(4, 21))):
                        break
                while True:
                    number_of_turns = input("Enter the desired number of turns [min: 1; max: 100]: ").strip()
                    if true_if_in_choice(number_of_turns, list(range(1, 101))):
                        break
                max_word_len, number_of_rows, number_of_cols, number_of_turns = [int(str_number) for str_number in [max_word_len, number_of_rows, number_of_cols, number_of_turns]]
                game = LunarCoins(max_word_length = max_word_len, rows = number_of_rows, columns = number_of_cols, turns = number_of_turns)
            else: # == 5 (Random)
                minimums, maximums = [10, 1, 4, 1], [16, 20, 20, 100]
                max_word_len, number_of_rows, number_of_cols, number_of_turns = [random.randint(a, b) for a, b in zip(minimums, maximums)]
                game = LunarCoins(max_word_length = max_word_len, rows = number_of_rows, columns = number_of_cols, turns = number_of_turns)

            break

    print()
    while True:
        other_options = input(keep_prompt_msg).strip()
        if true_if_in_choice(other_options, [1, 2, 3, 4]):
            other_options = int(other_options)
            global show_hint, show_table
            if other_options == 1:
                show_hint, show_table = True, True
            elif other_options == 2:
                show_hint, show_table = True, False
            elif other_options == 3:
                show_hint, show_table = False, True
            else: # == 4 (Hide both.)
                show_hint, show_table = False, False
            break

    print(logo)
    active_settings_table = Table(title="Current Settings")
    for header in ["Tiles Per Rack", "Rows", "Columns", "Turns", "Show Hint", "Show Table"]:
        active_settings_table.add_column(header)
    row = [str(option) for option in [game.max_word_length, game.rows, game.columns, game.turns, show_hint, show_table]]
    active_settings_table.add_row(*row)
    console.print(active_settings_table)
    start_game()


def start_game():
    while game.coins < game.rows * game.columns and game.turns != 0:
        print(f"Turns left: {game.turns}")
        
        game.draw_tiles()
        game.display_tiles()
        game.get_longest_words()
        
        if show_hint and game.longest_words:
            print(f"Hint: The longest word has {len(game.longest_words[0])} letters.\n")
        while True:
            your_word = input("Form a word from the given rack: ").strip().upper()
            if your_word in ["!Q", "!QUIT"]:
                if input("Really quit? [yes/no]: ") == "yes":
                    pre_game_init()
            if your_word == "!FAQ":
                print(faq)
            if game.determine_legality(your_word):
                break
        if show_table:
            game.display_history()
        game.display_grid_coins()
        game.word_count += 1
        game.turns -= 1

    if game.coins < (max_coins := game.rows * game.columns):
        print(f"\nAwh 🌚. You were short {max_coins - game.coins} 🌕.")

    else:
        print(f"\nYou did it! 🌝")
        if game.coins > max_coins:
            print(f"With an overflow of {game.coins - max_coins} 🌕 to boot.")
        if game.turns > 0:
            print(f"And you even have {game.turns} unused turns.")
        print("\n")
    pre_game_init()

start_game()


