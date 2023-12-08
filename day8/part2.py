import re, math

directions = ""
graph = {}
with open("input.txt") as f:
    directions = f.readline().strip()
    f.readline()
    for line in f.readlines():
        locations = re.findall("\w+", line)
        graph[locations[0]] = (locations[1], locations[2])

step_count = 0
cur_step = [key for key in list(graph.keys()) if key[2] == "A"]
periods = [None for _ in cur_step]

while not all(periods):
    if any([step[2] == "Z" for step in cur_step]):
        for i, step in enumerate(cur_step):
            if step[2] == "Z" and not periods[i]:
                periods[i] = step_count

    direction = directions[step_count % len(directions)]
    if direction == "R":
        cur_step = list(map(lambda step: graph[step][1], cur_step))
    else:
        cur_step = list(map(lambda step: graph[step][0], cur_step))
    step_count += 1

print(math.lcm(*periods))