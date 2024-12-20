
import re

with open("input.txt") as f:
    input = f.read().strip()

    s = 0
    s2 = 0

    program_regex = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

    do = True

    for r in program_regex.finditer(input):
        if "mul" in r.group(0):
            s += int(r.group(1)) * int(r.group(2))

            if do:
                s2 += int(r.group(1)) * int(r.group(2))

        elif "don't" in r.group(0):
            do = False
        else:
            do = True

    print(s)
    print(s2)
