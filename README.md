# **Tic-Tac-Toe** (A 2D game using pygame)

## Pygame

Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

## Installation

Enter the following command at a terminal prompt :

```bash
python -m pip install --user pygame
```

If this command doesn’t work on macOS, try running the command again without
the --user flag.

Then enter :

```bash
py game.py
```

## About the game 
> The game is played by two individuals. (First, we draw a board with a 3×3 square grid.) The first player chooses ‘X’ and draws it on any of the square grid, then it’s the chance of the second player to draw ‘O’ on the available spaces. Like this, the players draw ‘X’ and ‘O’ alternatively on the empty spaces until a player succeeds in drawing 3 consecutive marks either in the horizontal, vertical or diagonal way. Then the player wins the game otherwise the game draws when all spots are filled.