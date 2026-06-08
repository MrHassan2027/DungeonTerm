import random
from dataclasses import dataclass, field


FLOOR = "."
WALL = "#"
STAIRS = ">"
EMPTY = " "


@dataclass
class Room:
    x: int
    y: int
    w: int
    h: int

    def center(self) -> tuple[int, int]:
        return self.x + self.w // 2, self.y + self.h // 2

    def contains(self, x: int, y: int) -> bool:
        return self.x <= x < self.x + self.w and self.y <= y < self.y + self.h


class Dungeon:
    def __init__(self, width: int = 80, height: int = 24, max_rooms: int = 12):
        self.width = width
        self.height = height
        self.tiles: list[list[str]] = [[WALL] * width for _ in range(height)]
        self.rooms: list[Room] = []
        self._generate(max_rooms)

    def _generate(self, max_rooms: int):
        rng = random.Random()
        for _ in range(max_rooms * 5):
            w = rng.randint(4, 12)
            h = rng.randint(3, 8)
            x = rng.randint(1, self.width - w - 1)
            y = rng.randint(1, self.height - h - 1)
            room = Room(x, y, w, h)
            if any(self._overlaps(room, r) for r in self.rooms):
                continue
            self._carve_room(room)
            if self.rooms:
                self._connect(self.rooms[-1].center(), room.center())
            self.rooms.append(room)
            if len(self.rooms) >= max_rooms:
                break

        if self.rooms:
            sx, sy = self.rooms[-1].center()
            self.tiles[sy][sx] = STAIRS

    def _carve_room(self, room: Room):
        for dy in range(room.h):
            for dx in range(room.w):
                self.tiles[room.y + dy][room.x + dx] = FLOOR

    def _connect(self, a: tuple[int, int], b: tuple[int, int]):
        ax, ay = a
        bx, by = b
        x, y = ax, ay
        while x != bx:
            self.tiles[y][x] = FLOOR
            x += 1 if bx > x else -1
        while y != by:
            self.tiles[y][x] = FLOOR
            y += 1 if by > y else -1

    def _overlaps(self, a: Room, b: Room) -> bool:
        return a.x < b.x + b.w and a.x + a.w > b.x and a.y < b.y + b.h and a.y + a.h > b.y

    def start_pos(self) -> tuple[int, int]:
        return self.rooms[0].center() if self.rooms else (1, 1)

    def tile_at(self, x: int, y: int) -> str:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return WALL
