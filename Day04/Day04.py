
with open("input.txt") as f:
    letters = {}
    for ir, r in enumerate(f.readlines()):
        for ic, c in enumerate(r.strip()):
            letters[(ir, ic)] = c

    ROWS = ir + 1
    COLS = ic + 1


def check_p1(r, c, dr, dc, word):
    return (
        letters.get((r, c)) == word[0]
        and letters.get((r + dr, c + dc)) == word[1]
        and letters.get((r + 2 * dr, c + 2 * dc)) == word[2]
        and letters.get((r + 3 * dr, c + 3 * dc)) == word[3]
    )


counter = 0
counter2 = 0

patterns = {"X": ["X", "M", "A", "S"], "S": ["S", "A", "M", "X"]}


for r, c in letters:
    if letters[r, c] in patterns:
        word = patterns[letters[r, c]]

        if c + 3 < COLS and check_p1(r, c, 0, 1, word):
            counter += 1

        if r + 3 < ROWS:
            if check_p1(r, c, 1, 0, word):
                counter += 1

            if c + 3 < COLS:
                if check_p1(r, c, 1, 1, word):
                    counter += 1

            if c - 3 >= 0:
                if check_p1(r, c, 1, -1, word):
                    counter += 1
    elif letters[r, c] == "A":
        if r - 1 >= 0 and c - 1 >= 0 and r + 1 < ROWS and c + 1 < COLS:
            if (letters[r - 1, c - 1] == "M" and letters[r + 1, c + 1] == "S") or (
                letters[r - 1, c - 1] == "S" and letters[r + 1, c + 1] == "M"
            ):
                if (letters[r - 1, c + 1] == "M" and letters[r + 1, c - 1] == "S") or (
                    letters[r - 1, c + 1] == "S" and letters[r + 1, c - 1] == "M"
                ):
                    counter2 += 1

print(counter)
print(counter2)
