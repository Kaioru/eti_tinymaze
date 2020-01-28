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

            def move(player, direction):
                if not self.field.move(player, direction):
                    print("Invalid movement entered in game. Please try again")
                    time.sleep(1)

            menu = Menu([
                Option("w", "Move up", lambda: move(self.player, Direction.up)),
                Option("a", "Move left", lambda: move(self.player, Direction.left)),
                Option("s", "Move down", lambda: move(self.player, Direction.down)),
                Option("d", "Move right", lambda: move(self.player, Direction.right)),
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
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = input("Enter file name (without extension): ")

        try:
            csv_file = open(f'{file_name}.csv')
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_data = list(csv_reader)
            blocks = [[] for _ in range(sum(1 for row in csv_data))]
            start_block = None

            csv_file.close()

            for i, row in enumerate(csv_data):
                for ii, col in enumerate(row):
                    block = (
                        Wall(ii, i) if col == 'X' else
                        Portal(ii, i) if col == 'B' else
                        Path(ii, i)
                    )
                    blocks[i].append(block)
                    if col == 'A':
                        start_block = block
            print(f'Processed {len(blocks)} lines.')

            self.field = Field(blocks, start_block)
            self.player = Player()
            self.field.enter(self.player)
            print("\n" + self.field.render() + '\n')

            print("Successfully loaded maze!")
            time.sleep(3)
        except IOError:
            print("File does not exist.")
            input("Press Enter to continue...")