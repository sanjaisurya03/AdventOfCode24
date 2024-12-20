
from collections import deque
import uuid

with open("input.txt") as f:
    farm = [list(l.strip()) for l in f.readlines()]

ROWS = len(farm)
COLS = len(farm[0])


def find_region(farm, plots, treated, start_plot, region_id):
    if start_plot in treated:
        return plots

    row, col = start_plot

    plots.add((row, col))
    treated.add((row, col))

    for adj_row, adj_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (
            row + adj_row < ROWS
            and col + adj_col < COLS
            and row + adj_row >= 0
            and col + adj_col >= 0
        ):
            if farm[row + adj_row][col + adj_col] == farm[row][col]:
                find_region(
                    farm,
                    plots,
                    treated,
                    (row + adj_row, col + adj_col),
                    region_id,
                )

    return plots


def get_perimeter(region):
    perimeter = 4 * len(region)

    for row, col in region:
        for adj_row, adj_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            plot = (row + adj_row, col + adj_col)

            if plot in region:
                perimeter -= 1

    return perimeter


def get_sides(region):
    sides = 0

    UL = 0
    UR = 1
    DL = 2
    DR = 3

    LINES = {(-1, 0): [UL, UR], (1, 0): [DL, DR], (0, -1): [UL, DL], (0, 1): [UR, DR]}

    L_LINES = {
        ((1, 0), (0, 1)): DR,
        ((1, 0), (0, -1)): DL,
        ((-1, 0), (0, -1)): UL,
        ((-1, 0), (0, 1)): UR,
    }

    for row, col in region:
        n_corner = [1] * 4

        for adj_row, adj_col in LINES:
            plot = (row + adj_row, col + adj_col)

            if plot in region:
                for corner in LINES[(adj_row, adj_col)]:
                    n_corner[corner] -= 1 if n_corner[corner] > 0 else 0
                    n_corner[corner] -= 1 if n_corner[corner] > 0 else 0

        for (adj_row1, adj_col1), (adj_row2, adj_col2) in L_LINES:
            plot1 = (row + adj_row1, col + adj_col1)
            plot2 = (row + adj_row2, col + adj_col2)

            if plot1 in region and plot2 in region:
                if (row + adj_row1, col + adj_col2) not in region:
                    n_corner[L_LINES[((adj_row1, adj_col1), (adj_row2, adj_col2))]] += 1

        sides += sum(n_corner)

    return sides


treated = set()
regions = []

for irow, row in enumerate(farm):
    for icol, col in enumerate(row):
        if (irow, icol) not in treated:
            regions.append(
                find_region(farm, set(), treated, (irow, icol), str(uuid.uuid4()))
            )

print(sum(len(r) * get_perimeter(r) for r in regions))
print(sum(len(r) * get_sides(r) for r in regions))
