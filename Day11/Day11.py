from collections import defaultdict

with open("input.txt") as f:
    stones = f.readline().split(" ")


numbers = defaultdict(int)

for s in stones:
    numbers[s] += 1

s = 0

for i in range(75):
    next_numbers = []

    new_numbers = defaultdict(int)

    for n in numbers:
        if numbers[n] > 0:
            if int(n) == 0:
                new_numbers["1"] += numbers[n]
            elif len(n) % 2 == 0:
                new_numbers[str(int(n[: len(n) // 2]))] += numbers[n]
                new_numbers[str(int(n[len(n) // 2 :]))] += numbers[n]
            else:
                new_numbers[str(int(n) * 2024)] += numbers[n]

            numbers[n] -= numbers[n]

    numbers.update(new_numbers)

    if i == 24:
        print(sum(numbers.values()))


print(sum(numbers.values()))
