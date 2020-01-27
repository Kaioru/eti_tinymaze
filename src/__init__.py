import os
import sys
import time
import csv
from src.menu import Menu, Option
from src.game import Player, Field, Direction
from src.game.blocks import Path, Wall, Portal


class App():
    def __init__(self):
        self.field = None

        self.ended = False
        self.is_in_maze = False

    def end(self):
        self.ended = True

    def start(self):
        menu = Menu([
            Option("1", "Read and load maze from file", self.load_maze),
            Option("2", "View maze", self.view_maze),
            Option("3", "Play maze game", self.play_maze),
            Option("4", "Configure current maze", lambda: None),
            Option("0", "Exit maze", self.end),
        ])

        while not self.ended:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Main menu")
            print("=========")
            print(menu.render())
            if not menu.select(input("Enter your option: ")):
                print("Invalid menu option, try again!")
                time.sleep(3)
            print()

    def end_play_maze(self):
        self.is_in_maze = False

    def play_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        if self.field == None:
            print("There is no maze currently loaded.")
            input("Press Enter to continue...")
            return

        self.player = Player()
        self.field.enter(self.player)
        self.is_in_maze = True

        while self.is_in_maze:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.field.render())
            print()

            start = self.field.start_block
            blocks = [block for row in self.field.blocks for block in row]
            ends = [block for block in blocks if isinstance(block, Portal)]
            print("Location of start (A) = {0}".format(
                f"(row {start.y}, col {start.x})"))
            print("Location of End (B) = {0}".format(
                ', '.join([f"(row {block.y}, col {block.x})" for block in ends])))

            menu = Menu([
                Option("w", "Move up", lambda: self.field.move(
                    self.player, Direction.up)),
                Option("a", "Move left", lambda: self.field.move(
                    self.player, Direction.left)),
                Option("s", "Move down", lambda: self.field.move(
                    self.player, Direction.down)),
                Option("d", "Move right", lambda: self.field.move(
                    self.player, Direction.right)),
                Option("m", "Return to menu", lambda: self.end_play_maze()),
            ])
            selection = input(
                "Use the WASD to move or M key to return to menu: ")
            menu.select(selection)

            if self.player.is_finished:
                print()
                print("You have completed the maze, congratulations!")
                time.sleep(3)
                self.end_play_maze()

    def view_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        if self.field == None:
            print("There is no maze currently loaded.")
            input("Press Enter to continue...")
            return

        self.player = Player()
        self.field.enter(self.player)
        print(self.field.render())
        input("Press Enter to continue...")

    def load_maze(self):
        field = []
        row_count = 0
        name = input("Enter file name (without extension): ")
        player_position = None
        with open(f'{name}.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', )
            for row in csv_reader:
                blocks = []
                column_count = 0
                for block in row:
                    if (block == 'X'):
                        blocks.append(Wall(column_count, row_count))
                    elif (block == 'O' or block == 'A'):
                        if (block == 'A'):
                            player_position = Path(column_count, row_count)
                            blocks.append(player_position)
                        else:
                            blocks.append(Path(column_count, row_count))
                    elif (block == 'B'):
                        blocks.append(Portal(column_count, row_count))
                    column_count+= 1
                
                field.append(blocks)
                row_count += 1
            print(f'Processed {row_count} lines.')
        self.field = Field(field, player_position)
        print("\n" + self.field.render() + '\n')
        print("Successfully loaded!")
        time.sleep(3)
