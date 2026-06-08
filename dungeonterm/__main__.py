import curses
from .engine.world import Dungeon, FLOOR, STAIRS, WALL

def main():
    curses.wrapper(_run)

def _run(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE,  curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN,   curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN,  curses.COLOR_BLACK)

    h, w = stdscr.getmaxyx()
    dungeon = Dungeon(width=min(w - 1, 80), height=min(h - 4, 24))
    px, py = dungeon.start_pos()
    fog: set[tuple[int, int]] = set()
    message = "Arrow keys to move | Q to quit | R to new dungeon"

    def reveal(x, y, radius=6):
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                if dx*dx + dy*dy <= radius*radius:
                    fog.add((x + dx, y + dy))

    reveal(px, py)

    while True:
        stdscr.clear()
        for row in range(dungeon.height):
            for col in range(dungeon.width):
                if (col, row) not in fog:
                    continue
                tile = dungeon.tiles[row][col]
                if col == px and row == py:
                    stdscr.addch(row, col, "@", curses.color_pair(1) | curses.A_BOLD)
                elif tile == FLOOR:
                    stdscr.addch(row, col, ".", curses.color_pair(2))
                elif tile == STAIRS:
                    stdscr.addch(row, col, ">", curses.color_pair(3) | curses.A_BOLD)
                elif tile == WALL:
                    stdscr.addch(row, col, "#", curses.color_pair(4))

        stdscr.addstr(dungeon.height + 1, 0, message[:w-1])
        stdscr.refresh()

        key = stdscr.getch()
        dx, dy = 0, 0
        if key in (curses.KEY_UP,    ord("w"), ord("k")): dy = -1
        elif key in (curses.KEY_DOWN,  ord("s"), ord("j")): dy = 1
        elif key in (curses.KEY_LEFT,  ord("a"), ord("h")): dx = -1
        elif key in (curses.KEY_RIGHT, ord("d"), ord("l")): dx = 1
        elif key in (ord("q"), ord("Q")): break
        elif key in (ord("r"), ord("R")):
            dungeon = Dungeon(width=min(w-1,80), height=min(h-4,24))
            px, py = dungeon.start_pos()
            fog.clear()
            reveal(px, py)
            continue

        nx, ny = px + dx, py + dy
        if dungeon.tile_at(nx, ny) != WALL:
            px, py = nx, ny
            reveal(px, py)
            if dungeon.tiles[py][px] == STAIRS:
                dungeon = Dungeon(width=min(w-1,80), height=min(h-4,24))
                px, py = dungeon.start_pos()
                fog.clear()
                reveal(px, py)
                message = "New level! Keep exploring..."

if __name__ == "__main__":
    main()
