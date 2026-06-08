# DungeonTerm

> Roguelike dungeon crawler in the terminal — procedural generation and fog of war

## What it does
A classic roguelike game that runs entirely in the terminal. Procedurally generates dungeons with rooms and corridors, features fog of war so only explored tiles stay visible, and runs a turn-based game loop. Uses Python's `curses` library for terminal rendering.

## Quick Start
```bash
git clone https://github.com/MrHassan2027/DungeonTerm
cd DungeonTerm
pip install -e .
python -m dungeonterm
```

## Controls
| Key | Action |
|-----|--------|
| `↑↓←→` or `WASD` | Move |
| `>` | Descend stairs to next level |
| `q` | Quit |

## Features
- Procedural dungeon generation (rooms + corridors)
- Fog of war: only explored tiles stay visible
- Turn-based movement
- Stairs to descend to a new dungeon level

## Tech Stack
| Tool | Why |
|------|-----|
| Python 3.11+ | Core game loop |
| `curses` | Terminal rendering + input |
| `random` | Procedural dungeon generation |

## Architecture
```
dungeonterm/
├── __main__.py      # Entry point: game loop, curses init, rendering
└── engine/
    └── world.py     # Dungeon generation: rooms, corridors, stairs
```
