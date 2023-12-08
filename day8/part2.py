import re

directions = ""
graph = {}
with open("input.txt") as f:
    directions = f.readline().strip()
    f.readline()
    for line in f.readlines():
        locations = re.findall("\w+", line)
        graph[locations[0]] = (locations[1], locations[2])

print(graph)
print(directions)

step = 0
cur_step = [key for key in list(graph.keys()) if key[2] == "A"]
print(cur_step)

while True:
    if all([step[2] == "Z" for step in cur_step]):
        print(cur_step)
        print(step)
        break
    direction = directions[step % len(directions)]
    if direction == "R":
        cur_step = list(map(lambda step : graph[step][1], cur_step))
    else:
        cur_step = list(map(lambda step : graph[step][0], cur_step))
    step += 1