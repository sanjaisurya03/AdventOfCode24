
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

OBSTACLE = "#"

with open("input.txt") as f:
    grid = {}
    for ir, r in enumerate(f.readlines()):
        for ic, c in enumerate(r.strip()):
            grid[(ir, ic)] = c

            if c == "^":
                current_position = (ir, ic)

    ROWS = ir
    COLS = ic


FACES = [UP, RIGHT, DOWN, LEFT]


def walk(grid, current_position, facing):
    visited = set()
    loop = True

    while (current_position, facing) not in visited:
        visited.add((current_position, facing))

        dr = -1 if facing == UP else 1 if facing == DOWN else 0
        dc = -1 if facing == LEFT else 1 if facing == RIGHT else 0

        if (current_position[0] + dr > ROWS or current_position[0] + dr < 0) or (
            current_position[1] + dc > COLS or current_position[1] + dc < 0
        ):
            loop = False
            break

        if grid[(current_position[0] + dr, current_position[1] + dc)] == OBSTACLE:
            facing = FACES[(FACES.index(facing) + 1) % 4]
        else:
            current_position = (current_position[0] + dr, current_position[1] + dc)

    return visited, loop


visited, loop = walk(grid, tuple(current_position), UP)

print(len(set(v[0] for v in visited)))

s = 0

for v in set(v[0] for v in visited):
    grid[v] = OBSTACLE

    visited, loop = walk(grid, tuple(current_position), UP)
    s += loop

    grid[v] = "."

print(s)
