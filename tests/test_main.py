import tcod

from main import SCREEN_HEIGHT, SCREEN_WIDTH, move_player


def test_move_player_up():
    x, y = move_player(10, 10, tcod.event.KeySym.UP)
    assert (x, y) == (10, 9)


def test_move_player_down():
    x, y = move_player(10, 10, tcod.event.KeySym.DOWN)
    assert (x, y) == (10, 11)


def test_move_player_left():
    x, y = move_player(10, 10, tcod.event.KeySym.LEFT)
    assert (x, y) == (9, 10)


def test_move_player_right():
    x, y = move_player(10, 10, tcod.event.KeySym.RIGHT)
    assert (x, y) == (11, 10)


def test_move_player_does_not_go_out_of_bounds():
    x, y = move_player(0, 0, tcod.event.KeySym.LEFT)
    assert (x, y) == (0, 0)

    x, y = move_player(0, 0, tcod.event.KeySym.UP)
    assert (x, y) == (0, 0)

    max_x = SCREEN_WIDTH - 1
    max_y = SCREEN_HEIGHT - 1

    x, y = move_player(max_x, max_y, tcod.event.KeySym.RIGHT)
    assert (x, y) == (SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)

    x, y = move_player(max_x, max_y, tcod.event.KeySym.DOWN)
    assert (x, y) == (SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)


def test_move_player_ignores_non_move_key():
    x, y = move_player(10, 10, tcod.event.KeySym.RETURN)
    assert (x, y) == (10, 10)
