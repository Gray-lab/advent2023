import re

games_sum = 0

limits = {'blue':14, 'green':13, 'red':12}

with open("input.txt") as f:
    for line in f.readlines():
        game = re.search(r'\d+', line).group()
        pulls = line.split(':')[1].split(';')

        possible = True
        for pull in pulls:
            events = sorted([event.split() for event in pull.split(',')], key = lambda x : x[1])
            for value, key in events:
                if limits[key] < int(value):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            games_sum += int(game)

print(games_sum)


