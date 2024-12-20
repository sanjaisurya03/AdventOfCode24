
from collections import defaultdict

with open("input.txt") as f:
    grid = {}
    pairs = defaultdict(list)

    for ir, r in enumerate(f.readlines()):
        for ic, c in enumerate(r.strip()):
            if c != ".":
                pairs[c].append((ir, ic))

    ROWS = ir + 1
    COLS = ic + 1

pairs = [
    (p, p1)
    for positions in pairs.values()
    for i, p in enumerate(positions)
    for p1 in positions[i + 1 :]
]

antinodes_p1 = set()
antinodes_p2 = set()

for p in pairs:
    (dr, dc) = (p[0][0] - p[1][0], p[0][1] - p[1][1])

    for new in [[p[0][0] + dr, p[0][1] + dc], [p[1][0] - dr, p[1][1] - dc]]:
        i = 0
        while 0 <= new[0] < ROWS and 0 <= new[1] < ROWS:
            if i == 0:
                antinodes_p1.add(tuple(new))

            antinodes_p2.add(tuple(new))

            new[0] += dr
            new[1] += dc

            i += 1

        dr = -dr
        dc = -dc

    antinodes_p2.add(p[0])
    antinodes_p2.add(p[1])

print(len(antinodes_p1))
print(len(antinodes_p2))
