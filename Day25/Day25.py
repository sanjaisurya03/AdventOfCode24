import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = list(map(lambda s: s.split('\n'), '\n'.join(reader()).split('\n\n')))
  L = []
  K = []
  for s in f:
    V = [sum(1 if s[i][j] == '#' else 0 for i in range(1, len(s) - 1))
         for j in range(len(s[0]))]
    if s[0] == '#####':
      L.append(V)
    else:
      K.append(V)
  c = 0
  for l in L:
    for k in K:
      if all(l[i] + k[i] <= len(f[0]) - 2 for i in range(len(l))):
        c += 1
  print(c)


def part2():
  pass


part1()
part2()
