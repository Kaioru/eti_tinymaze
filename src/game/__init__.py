class Player():
    def __init__(self):
        self.field = None
        self.block = None
        self.is_finished = False


class Field():
    def __init__(self, blocks, start_block):
        self.blocks = blocks
        self.start_block = start_block

    def enter(self, player):
        player.field = self
        self.start_block.step(player)

    def render(self):
        pass


class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = None

    def is_wall(self):
        pass

    def step(self, player):
        if player.block != None:
            player.block.player = None
        player.block = self
        self.player = player

    def render(self):
        pass
