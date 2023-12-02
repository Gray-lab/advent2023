import re

powers_sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        # get game number
        # get array of games
        # for each game, get max count of r, g, b
        power = 1
        pulls = line.split(':')[1].split(';')
        maximums = {'blue':0, 'green':0, 'red':0}
        for pull in pulls:
            events = sorted([event.split() for event in pull.split(',')], key = lambda x : x[1])
            for value, key in events:
                maximums[key] = max(maximums[key], int(value))
        for value in maximums.values():
            power *= value
        powers_sum += power

print(powers_sum)

