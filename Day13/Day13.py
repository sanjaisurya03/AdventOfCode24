
import re

with open("input.txt") as f:
    machines = []
    regex = re.compile(r"X\+(\d+)|Y\+(\d+)|X=(\d+)|Y=(\d+)")

    for l in f.read().split("\n\n"):
        commands = {}

        ll = l.split("\n")
        r_find = regex.findall(ll[0])
        commands["A"] = {"X": int(r_find[0][0]), "Y": int(r_find[1][1])}
        r_find = regex.findall(ll[1])
        commands["B"] = {"X": int(r_find[0][0]), "Y": int(r_find[1][1])}
        r_find = regex.findall(ll[2])
        commands["results"] = {"X": int(r_find[0][2]), "Y": int(r_find[1][3])}

        machines.append(commands)

already_calc = set()


def calc_cost(machines, part_2=False):
    cost = 0

    if part_2:
        for commands in machines:
            commands["results"]["X"] += 10000000000000
            commands["results"]["Y"] += 10000000000000

    for commands in machines:
        push_b = (
            commands["A"]["X"] * commands["results"]["Y"]
            - commands["A"]["Y"] * commands["results"]["X"]
        ) / (
            commands["A"]["X"] * commands["B"]["Y"]
            - commands["A"]["Y"] * commands["B"]["X"]
        )

        push_a = (commands["results"]["X"] - commands["B"]["X"] * push_b) / commands[
            "A"
        ]["X"]

        if push_a.is_integer() and push_b.is_integer():
            cost += 3 * push_a + push_b

    return int(cost)


print(calc_cost(machines))
print(calc_cost(machines, True))
