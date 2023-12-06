import re
from math import sqrt

res = 1
with open("input.txt") as f:
    times = re.findall("\d+", f.readline())
    distances = re.findall("\d+", f.readline())
    time = int("".join(times))
    dist = int("".join(distances))

    x1 = int((-time + sqrt(time ** 2 - 4 * -1 * -dist)) / (2 * -1) + 1)
    # need to make sure we aren't on a whole number
    x2 = int((-time - sqrt(time ** 2 - 4 * -1 * -dist)) / (2 * -1) - 0.0001)

    ways_to_win = x2 - x1 + 1
    res *= ways_to_win
print(res)
