import os
import sys
from src.game import Player, Field, Direction
from src.game.blocks import Path, Wall, Portal

class App():
    def __init__(self):
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

    def start(self):
        finish = False

        while not finish:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.field.render())
            print()

            start = self.field.start_block
            blocks = [block for row in self.field.blocks for block in row]
            ends = [block for block in blocks if isinstance(block, Portal)]
            print("Location of start (A) = {0}".format(f"(row {start.y}, col {start.x})"))
            print("Location of End (B) = {0}".format(', '.join([f"(row {block.y}, col {block.x})" for block in ends])))

            # todo: use menu api
            selection = input("Use the WASD to move or M key to return to menu: ").lower()

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
                finish = True

