# DungeonTerm

> Roguelike dungeon crawler in the terminal — procedural generation, fog of war, inventory system

## What it does
A classic roguelike game that runs entirely in the terminal. Procedurally generates dungeons with rooms, corridors, enemies, and loot. Features fog of war, turn-based combat, item pickup/usage, and permadeath. Built using ANSI escape codes — no ncurses dependency.

## Quick Start
```bash
git clone https://github.com/yourusername/DungeonTerm
cd DungeonTerm
pip install -r requirements.txt
python -m dungeonterm
```

## Controls
| Key | Action |
|-----|--------|
| `↑↓←→` or `WASD` | Move |
| `i` | Open inventory |
| `g` | Pick up item |
| `u` | Use item |
| `>` | Descend stairs |
| `?` | Help |

## Features
- Procedural dungeon generation (BSP room splitting)
- Fog of war: only explored tiles stay visible
- Turn-based combat with attack/defense stats
- Enemy AI: patrol, chase, attack
- Items: health potions, weapons, armor, scrolls
- Inventory system with item equipping
- 10 dungeon levels with scaling difficulty
- High score board (local SQLite)
- Permadeath — save state clears on death

## Tech Stack
| Tool | Why |
|------|-----|
| Python 3.11+ | Core game loop |
| `curses` | Terminal rendering + input |
| `random` / BSP | Procedural dungeon generation |
| `aiosqlite` | High score persistence |

## Architecture
```
dungeonterm/
├── engine/
│   ├── world.py       # Dungeon generation (BSP)
│   ├── fov.py         # Field-of-view / fog of war
│   ├── combat.py      # Turn-based combat
│   └── ai.py          # Enemy pathfinding (A*)
├── entities/
│   ├── player.py
│   ├── enemy.py
│   └── item.py
└── render/
    └── terminal.py    # ANSI/curses renderer
```
