#!/usr/bin/env python3
from pathlib import Path

import tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MOVE_KEYS = {
    tcod.event.KeySym.UP: (0, -1),
    tcod.event.KeySym.DOWN: (0, 1),
    tcod.event.KeySym.LEFT: (-1, 0),
    tcod.event.KeySym.RIGHT: (1, 0),
}


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def move_player(player_x, player_y, key_sym):
    if key_sym not in MOVE_KEYS:
        return player_x, player_y

    dx, dy = MOVE_KEYS[key_sym]
    next_x = clamp(player_x + dx, 0, SCREEN_WIDTH - 1)
    next_y = clamp(player_y + dy, 0, SCREEN_HEIGHT - 1)
    return next_x, next_y


def load_tileset():
    try:
        return tcod.tileset.get_default()
    except RuntimeError:
        font_candidates = (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
            Path("/Library/Fonts/Menlo.ttc"),
            Path("C:/Windows/Fonts/consola.ttf"),
        )
        for font_path in font_candidates:
            if font_path.exists():
                return tcod.tileset.load_truetype_font(str(font_path), 16, 16)
        raise


def main():
    tileset = load_tileset()
    console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")

    with tcod.context.new(
        columns=SCREEN_WIDTH,
        rows=SCREEN_HEIGHT,
        tileset=tileset,
        title="PyRogue2025",
    ) as context:
        player_x = SCREEN_WIDTH // 2
        player_y = SCREEN_HEIGHT // 2

        while True:
            console.clear()
            console.print(player_x, player_y, "@")
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)

                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                if isinstance(event, tcod.event.KeyDown):
                    if event.sym == tcod.event.KeySym.ESCAPE:
                        raise SystemExit()

                    player_x, player_y = move_player(
                        player_x,
                        player_y,
                        event.sym,
                    )


if __name__ == "__main__":
    main()
