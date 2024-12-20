
with open("input.txt") as f:
    grid = {
        (ir, ic): int(c)
        for ir, r in enumerate(f.readlines())
        for ic, c in enumerate(r.strip())
    }


starts = set()
for c in grid:
    if grid[c] == 0:
        starts.add(c)


def walk(coord, visited):
    if grid[coord] == 9:
        visited.add(coord)

    for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_coord = (coord[0] + n[0], coord[1] + n[1])

        if new_coord in grid and grid[new_coord] == grid[coord] + 1:
            walk(new_coord, visited)

    return len(visited)


print(sum(walk(s, set()) for s in starts))


def walk_p2(coord, good_paths):
    total = 0

    if grid[coord] == 9:
        good_paths += 1

        return good_paths

    for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_coord = (coord[0] + n[0], coord[1] + n[1])

        if new_coord in grid and grid[new_coord] == grid[coord] + 1:
            total += walk_p2(new_coord, good_paths)

    return total


print(sum(walk_p2(s, 0) for s in starts))
