
from re import findall
from math import prod

# read input data from file
with open("input.txt") as file:
  robots = file.readlines()
width = 101
height = 103
x_mid = width // 2
y_mid = height // 2

# hashmap of all possible positions initialized to 0 count
facility = {}
for i in range(width):
  for j in range(height):
    facility[i, j] = 0

for robot in robots:
  p_x, p_y, v_x, v_y = map(int, findall(r"-?\d+", robot))

  # run 100 iterations
  p_x = (p_x + 100 * v_x) % width
  p_y = (p_y + 100 * v_y) % height

  # record final position of robot
  facility[p_x, p_y] += 1

quadrants = [0, 0, 0, 0]
for position in facility.keys():
  x = position[0]
  y = position[1]
  count = facility[x, y]

  # quadrants going clockwise starting in top left
  if count > 0:
    if x < x_mid and y < y_mid:
      quadrants[0] += count
    elif x > x_mid and y < y_mid:
      quadrants[1] += count
    elif x > x_mid and y > y_mid:
      quadrants[2] += count
    elif x < x_mid and y > y_mid:
      quadrants[3] += count

# output product of quadrant counts
print(prod(quadrants))

from re import findall
from PIL import Image

# convert map to image
def print_map(m, w, h):
  image = Image.new("1", (w, h))

  for x in range(w):
    for y in range(h):
      if m[y][x] == 0:
        image.putpixel((x, y), 0)
      else:
        image.putpixel((x, y), 1)

  image.save("tree.bmp")

# read input data from file
with open("input.txt") as file:
  robots = file.readlines()
robots = [list(map(int, findall(r"-?\d+", robot))) for robot in robots]

width = 101
height = 103
x_mid = width // 2
y_mid = height // 2

facility = [[0 for x in range(width)] for y in range(height)]

for robot in robots:
  p_x, p_y, v_x, v_y = robot
  facility[p_y][p_x] += 1

i = 1
while True:
  for j in range(len(robots)):
    p_x, p_y, v_x, v_y = robots[j]

    # remove current robot position
    facility[p_y][p_x] -= 1

    # calculate new robot position
    p_x = (p_x + v_x) % width
    p_y = (p_y + v_y) % height

    # update robot position
    robots[j] = [p_x, p_y, v_x, v_y]

    # record new robot position
    facility[p_y][p_x] += 1

  # if all robots in unique positions, found the tree
  if max([facility[y][x] for y in range(height) for x in range(width)]) == 1:
    break

  i += 1

# create tree image file
print_map(facility, width, height)
print(i)  # print iteration count until tree
