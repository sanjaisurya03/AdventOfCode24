
import heapq
from collections import defaultdict
import time

def dijkstra(map, start, end):
    maxr = len(map)
    maxc = len(map[0])
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    visited = set()
    in_heap = set()
    rstart,cstart = start
    pq = []
    heapq.heappush(pq, (0,rstart,cstart))
    in_heap.add((0, rstart, cstart))

    dist_from_start = [[-1 for _ in range(maxr)] for _ in range(maxc)]
    dist_from_start[rstart][cstart] = 0

    while pq:
        dist, r, c = heapq.heappop(pq)
        visited.add((r,c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < maxr and 0 <= nc < maxc and (nr,nc) not in visited:
                if map[nr][nc] == '#':
                    continue
                if (dist+1, nr, nc) in in_heap:
                    continue
                dist_from_start[nr][nc] = dist + 1
                if (nr, nc) == end:
                    break
                heapq.heappush(pq, (dist+1, nr, nc))
                in_heap.add((dist+1, nr, nc))
    return dist_from_start


def solve(map, manhattan_dist, lower_savings_limit=100):
    maxr = len(map)
    maxc = len(map[0])
    normal_time = 1
    freq_time_saved = defaultdict(int)
    for r in range(maxr):
        for c in range(maxc):
            if map[r][c] == 'S':
                start = (r,c)
            elif map[r][c] == 'E':
                end = (r,c)
            elif map[r][c] == '.':
                normal_time += 1
    dist_from_start = dijkstra(map, start, end)
    dist_from_end = [[normal_time - cell if cell > -1 else -1 for cell in row] for row in dist_from_start]

    for r in range(maxr):
        for c in range(maxc):
            if map[r][c] == '#':
                continue
            for dr in range(-manhattan_dist, manhattan_dist+1):
                for dc in range(-manhattan_dist, manhattan_dist+1):
                    if abs(dr) + abs(dc) > manhattan_dist:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < maxr and 0 <= nc < maxc and map[nr][nc] != "#":
                        new_time = dist_from_start[r][c] + abs(dr) + abs(dc) + dist_from_end[nr][nc]
                        if new_time >= normal_time:
                            continue
                        freq_time_saved[normal_time - new_time] += 1
    
    savings_cheats = 0
    for key in freq_time_saved.keys():
        if key >= lower_savings_limit:
            savings_cheats += freq_time_saved[key]
    return savings_cheats


if __name__=="__main__":
    print("\n--- Day 20: Race Condition ---")
    file = open("input.txt","r")
    data = [x.strip() for x in file.readlines()]
    # print(data)

    print("Part 1:")
    start1 = time.time()
    print(solve(data, 2))
    end1 = time.time()
    print(f"Elapsed time: {end1-start1:.4f} seconds")

    print("Part 2:")
    start2 = time.time()
    print(solve(data, 20))
    end2 = time.time()
    print(f"Elapsed time: {end2-start2:.4f} seconds")
    print()
