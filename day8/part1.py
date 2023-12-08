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
cur_step = "AAA"
while True:
    if cur_step == "ZZZ": 
        print(step)
        break
    direction = directions[step % len(directions)]
    if direction == "R":
        cur_step = graph[cur_step][1]
    else:
        cur_step = graph[cur_step][0]
    step += 1
