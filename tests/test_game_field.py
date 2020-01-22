from src.game import Player, Field
from src.game.blocks import Path, Wall, Portal


def test_field_enter():
    start_block = Path(0, 0)
    blocks = [[start_block, Path(1, 0)]]
    field = Field(blocks, start_block)
    player = Player()

    assert player.field == None
    assert player.block == None

    field.enter(player)

    assert player.field == field
    assert player.block == start_block


def test_field_render():
    start_block = Path(0, 0)
    blocks = [[start_block, Path(1, 0)]]
    field = Field(blocks, start_block)

    assert field.render() == [['O', 'O']]

    player = Player()
    field.enter(player)

    assert field.render() == [['A', 'O']]