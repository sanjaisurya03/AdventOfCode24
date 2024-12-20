
from math import floor
from itertools import repeat

# read input_data from file
with open("input.txt") as file:
  input_data = file.read()
disk_map = list(map(int, input_data.strip()))

# convert disk_map to memory list
memory = []
block = 0
for i in range(len(disk_map)):
  if i % 2 == 0:
    memory += list(repeat(int(block), disk_map[i]))
  else:
    memory += list(repeat('.', disk_map[i]))
  block += .5

num_idx = [i for i in range(len(memory) - 1, -1, -1) if memory[i] != '.']
for idx in num_idx:
  # if gap left of number, swap them
  gap = memory.index('.')
  if gap < idx:
    memory[idx], memory[gap] = memory[gap], memory[idx]

# calculate checksum
total = 0
for i in range(len(memory)):
  val = memory[i]
  if val != '.':
    total += i * val

print(total)

# read input_data from file
with open("input.txt") as file:
  input_data = file.read()
disk_map = list(map(int, input_data.strip()))

# convert disk_map to memory list
memory = []
block = 0
for i in range(len(disk_map)):
  if i % 2 == 0:
    memory += list(repeat(int(block), disk_map[i]))
  else:
    memory += list(repeat('.', disk_map[i]))
  block += .5

for i in range(floor(block), -1, -1):
  idx = memory.index(i)  # index of number in memory
  count = memory.count(i)  # length of file

  # find gap left of idx if exists
  gap = None
  for j in range(idx - count + 1):
    if memory[j:j + count] == list(repeat('.', count)):
      gap = j
      break

  # if gap found, swap file into gap in memory
  if gap != None:
    memory[idx:idx + count], memory[j:j + count] = memory[j:j + count], memory[idx:idx + count]

# calculate checksum
total = 0
for i in range(len(memory)):
  val = memory[i]
  if val != '.':
    total += i * val

print(total)

