import os
import sys
import time
from src.menu import Menu, Option
from src.game import Player, Field, Direction
from src.game.blocks import Path, Wall, Portal


class App():
    def __init__(self):
        self.ended = False
        self.field = None
        self.player = Player()

        # Testing field for debugging purposes
        left_top = Path(0, 0)
        right_top = Portal(1, 0)
        left_bottom = Path(0, 1)
        right_bottom = Path(1, 1)
        blocks = [[left_top, right_top], [left_bottom, right_bottom]]
        self.field = Field(blocks, left_top)
        self.field.enter(self.player)

    def end(self):
        self.ended = True

    def start(self):
        menu = Menu([
            Option("1", "Read and load maze from file", lambda: None),
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

    def play_maze(self):
        finish = False

        while not finish:
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

            # todo: use menu api
            selection = input(
                "Use the WASD to move or M key to return to menu: ").lower()

            if selection == 'w':
                self.field.move(self.player, Direction.up)
            if selection == 'a':
                self.field.move(self.player, Direction.left)
            if selection == 's':
                self.field.move(self.player, Direction.down)
            if selection == 'd':
                self.field.move(self.player, Direction.right)
            if selection == 'm' or self.player.is_finished:
                if self.player.is_finished:
                    print()
                    print("You have completed the maze, congratulations!")
                    time.sleep(3)
                finish = True

    def view_maze(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.field.render())
        input("Press Enter to continue...")
