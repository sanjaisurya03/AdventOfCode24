
import functools

with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")

    rules = set([(r.split("|")[0], r.split("|")[1]) for r in rules.splitlines()])
    updates = [u.split(",") for u in updates.splitlines()]


s = 0
s2 = 0


def cmp(a, b):
    if (a, b) in rules:
        return -1
    elif (b, a) in rules:
        return 1
    else:
        return 0


for u in updates:
    for iu in range(len(u) - 1):
        if (u[iu], u[iu + 1]) not in rules:
            u.sort(key=functools.cmp_to_key(cmp))
            s2 += int(u[len(u) // 2])

            break
    else:
        s += int(u[len(u) // 2])

print(s)
print(s2)
