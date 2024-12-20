
from collections import deque


equations = []

with open("input.txt") as f:
    for l in f.readlines():
        l_spl = l.split(": ")
        equations.append((int(l_spl[0]), deque(map(int, l_spl[1].split(" ")))))


def calc_p1(acc, numbers, result, part_2=False):
    if acc > result:
        return False

    if not numbers:
        return acc == result

    numbers_cln = numbers.copy()
    n = numbers_cln.popleft()

    c1 = calc_p1(acc * n, numbers_cln, result)
    c2 = calc_p1(acc + n, numbers_cln, result)

    return c1 or c2


def calc_p2(acc, numbers, result, part_2=False):
    if acc > result:
        return False

    if not numbers:
        return acc == result

    numbers_cln = numbers.copy()
    n = numbers_cln.popleft()

    c1 = calc_p2(acc * n, numbers_cln, result)
    c2 = calc_p2(acc + n, numbers_cln, result)
    c3 = calc_p2(int(f"{acc}{n}"), numbers_cln, result)

    return c1 or c2 or c3


s = 0
s2 = 0

for eq in equations:
    result, numbers = eq

    acc = numbers.popleft()

    if calc_p1(acc, numbers, result):
        s += result

    if calc_p2(acc, numbers, result):
        s2 += result


print(s)
print(s2)
