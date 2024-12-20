
#!/usr/bin/env python3

import pathlib
import sys

from heapq import heappush, heappop
from typing import Iterator


Pos = tuple[int, int]

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def moves(pos: Pos, dir: int) -> Iterator[tuple[Pos, int]]:
  for d in ((dir - 1) % 4), dir, ((dir + 1) % 4):
    yield (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1]), d

def shortest_path(corrupted: set[Pos], start: Pos, end: Pos) -> tuple[int, tuple[Pos, ...]]:
  steps, path = 0, (start, )
  q: list[tuple[int, Pos, int, tuple[Pos, ...]]] = [(0, start, 0, path)]
  seen = {start: 0}

  while q:
    steps, (x, y), dir, path = heappop(q)
    if (x, y) == end:
      break

    for (nx, ny), d in moves((x, y), dir):
      if not 0 <= nx <= end[0] or not 0 <= ny <= end[1]:
        continue
      if (nx, ny) in corrupted:
        continue
      if (nx, ny) in seen and seen[nx, ny] <= steps + 1:
        continue

      seen[nx, ny] = steps + 1
      path += ((nx, ny),)
      heappush(q, (steps + 1, (nx, ny), d, path))
  else:
    return 0, tuple()

  return steps, path

def run() -> None:
  mx, my = 70, 70
  initial = 1024

  bytes = []
  with open('input.txt') as f:
    for line in f.readlines():
        x, y = line.strip().split(',')
        bytes.append((int(x), int(y)))


  grid = {n for n in bytes[:initial]}
  steps, path = shortest_path(grid, (0, 0), (mx, my))
  print(f"Shortest path after {initial} bytes: {steps}")

  for byte in bytes[initial:]:
    grid.add(byte)
    if byte in path:
      steps, path = shortest_path(grid, (0, 0), (mx, my))
      if not steps:
        break
  print(f"First blocking byte: {byte}")

if __name__ == '__main__':
  run()
  sys.exit(0)
