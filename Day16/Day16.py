
import heapq
from typing import List, Tuple, Dict, Set
from collections import defaultdict, deque

class Solution:
    def __init__(self, file_name: str):
        self.grid: List[str] = []
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.start: Tuple[int, int] = (-1, -1)
        self.end: Tuple[int, int] = (-1, -1)
        self.dist: Dict[Tuple[int, int, int], int] = {}
        self.predecessors: Dict[Tuple[int, int, int], List[Tuple[int, int, int]]] = defaultdict(list)
        self._parse(file_name)

    def _parse(self, file_name: str):
        with open(file_name, 'r') as f:
            for r, line in enumerate(f):
                line = line.strip()
                self.grid.append(line)
                for c, char in enumerate(line):
                    if char == 'S':
                        self.start = (r, c)
                    if char == 'E':
                        self.end = (r, c)

        if self.start == (-1, -1) or self.end == (-1, -1):
            raise ValueError("Error: Start (S) or End (E) point not found in the grid.")

    def dijkstra(self) -> int:
        pq = [(0, self.start[0], self.start[1], -1)]  # distance, row, col, direction
        self.dist[(self.start[0], self.start[1], -1)] = 0

        while pq:
            d, r, c, dir = heapq.heappop(pq)
            
            if self.grid[r][c] == 'E':
                return d

            for i, (dr, dc) in enumerate(self.directions):
                nr, nc = r + dr, c + dc
                nd = d + 1
                
                if i != dir and dir != -1:
                    nd += 1000
                
                if (nr < 0 or nc < 0 or 
                    nr >= len(self.grid) or 
                    nc >= len(self.grid[0]) or 
                    self.grid[nr][nc] == '#'):
                    continue

                current = (nr, nc, i)
                
                if current not in self.dist or nd < self.dist[current]:
                    self.dist[current] = nd
                    heapq.heappush(pq, (nd, nr, nc, i))
                    self.predecessors[current].clear()
                    self.predecessors[current].append((r, c, dir))
                elif nd == self.dist[current]:
                    self.predecessors[current].append((r, c, dir))

        return float('inf')

    def backtrack(self) -> int:
        unique_tiles: Set[Tuple[int, int]] = set()
        q = deque([(self.end[0], self.end[1], i) for i in range(4)])

        while q:
            r, c, dir = q.popleft()
            unique_tiles.add((r, c))
            
            for pred in self.predecessors.get((r, c, dir), []):
                q.append(pred)

        return len(unique_tiles)

    def part1(self) -> int:
        return self.dijkstra()

    def part2(self) -> int:
        self.dijkstra()
        return self.backtrack()

def main():
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")

if __name__ == "__main__":
    main()
