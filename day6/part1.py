import re
from math import sqrt

res = 1
with open("input.txt") as f:
    times = [int(x) for x in re.findall("\d+", f.readline())]
    distances = [int(x) for x in re.findall("\d+", f.readline())]

    for time, dist in zip(times, distances):
        # dist = x * (time - x)
        # 0 = - x ^ 2 + x * time - dist
        # (-b +/- sqrt(b^2 -4ac)) / 2a
        x1 = int((-time + sqrt(time ** 2 - 4 * -1 * -dist)) / (2 * -1) + 1)
        # need to make sure we aren't on a whole number
        x2 = int((-time - sqrt(time ** 2 - 4 * -1 * -dist)) / (2 * -1) - 0.0001)

        ways_to_win = x2 - x1 + 1
        res *= ways_to_win
print(res)

