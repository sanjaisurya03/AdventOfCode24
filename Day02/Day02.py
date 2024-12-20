
def check_levels(levels):
    return all(
        [
            (
                z[0] < z[1]
                if levels[0] < levels[1]
                else z[0] > z[1]
                if levels[0] > levels[1]
                else False
            )
            and 0 < abs(z[0] - z[1]) <= 3
            for z in zip(levels[:-1], levels[1:])
        ]
    )


with open("input.txt") as f:
    safe = 0
    safe2 = 0

    for line in f:
        levels = list(map(int, line.split(" ")))

        if check_levels(levels):
            safe += 1
            safe2 += 1
        else:
            for i in range(len(levels)):
                if check_levels(levels[:i] + levels[i + 1 :]):
                    safe2 += 1
                    break

    print(safe)
    print(safe2)
