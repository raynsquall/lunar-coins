
# Lunar Coins --- A Golden Coins Clone

This project is a recreation/clone of the **Golden Coins** minigame in **Bookworm Adventures Volume 2** as a command-line Python game. This repository aims to replicate the gameplay mechanics of the original minigame for personal learning and nostalgic purposes. While it is still a clone, new features were added.

### Installation

1. Ensure you have [Python](https://www.python.org/downloads/) installed (3.12 as of writing).
2. Download this repository. 
3. Enter `pip install rich` or `py -m pip install rich` in your terminal
4. Run main.py.

### How to Play

Here is a sample gameplay from the minigame this project was based on:

![gameplay_og](https://i.ibb.co/VLh8xMG/gc-og.gif)

As you can see, the goal is to spell 5 words from the randomly generated 12-tile racks. Golden tiles fill two coins. Fill the board/grid to win. In this project though, it is the case that:
1. Unfilled slots are new moons.
2. Coins are full moons.
3. Golden coins are smiling full moons. 
4. Golden tiles are lunar tiles (denoted by bold and underline but are the same color as regular tiles).

![gameplay_cmd](https://raw.githubusercontent.com/raynsquall/lunar-coins/main/sample_play.gif)

Notice that there are features that did not exist in the original though. 

### New Features

1. Longest Word Hint - Situated below each rack. You can refer to it if you want to hunt for the longest word a la Text Twist. Kinda tough here though, given that there is no Twist option. This can be turned off for a more vanilla experience.
2. Tabulated History - After each turn, a table showing the previous rack, longest possible words, your played word, moons filled, and lunar tiles used appears. Like the hint, this can also be turned off.
3. New Game Modes - Classic Mode is the default (same as vanilla) mode. The rest of the modes (EasyMode, HardMode, Custom, Random) are pretty self-explanatory albeit not balanced.

![game_modes](https://i.ibb.co/yd6t8Qq/gamemodes.jpg)

The highlight here is probably just Custom, really. Hope you have fun with it!

### Possible Feature Additions in the Future

1. Scoring System - The original minigame has a scoring system but this clone does not have one. It seems unnecessary at the moment. 
2. High Scores Keeping - Have a persistent txt/csv/db that records and displays your previous scores and plays.
3. Endless Mode - This is technically already endless but one without prompts would probably be nice.
4. Rack Twisting - Shuffling without changing the rack, just like in Text Twist and Reader's Digest Super Word Power.
5. Rack Color Customizing - Changing the colors of the rack, with preset themes perhaps.

### Project Status and Use:

- **Non-Commercial Use:** This clone is not intended for commercial purposes or distribution.
- **Personal Learning:** It is meant for personal experimentation, educational purposes, and portfolio building.
- **No Open-Source License:** This project does not have an associated open-source license due to its nature as a clone.

### Legal Disclaimer:

- **Legal Implications:** Using or distributing this clone might have legal implications, especially concerning copyright or intellectual property rights.
- **Non-Affiliation:** This project is not affiliated with Bookworm Adventures Volume 2's creators or associated entities.

### Contributions and Contact:

- **Contributions:** Due to potential legal concerns, contributions might not be accepted.
- **Contact:** For questions or concerns regarding the project, please contact raynsquall@gmail.com.