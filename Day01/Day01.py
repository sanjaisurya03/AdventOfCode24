
with open("input.txt") as f:
    l1 = []
    l2 = []

    for line in f:
        (a, b) = line.strip().split("   ")
        l1.append(int(a))
        l2.append(int(b))

    print(sum([abs(z[0] - z[1]) for z in zip(sorted(l1), sorted(l2))]))
    print(sum([z[0] * z[1] for z in zip(l1, [l2.count(c) for c in l1])]))
