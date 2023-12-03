import re

sum_not_parts = 0
sum_all = 0
array = []
symbols = set(['$', '@', '%', '-', '#', '=', '*', '&', '/', '+'])

with open("input.txt") as f:
    for line in f.readlines():
        all_nums = re.findall("\d+", line)
        for num in all_nums:
            sum_all += int(num)
        array.append(list(line.strip("\n")))

cols = len(array[0])
rows = len(array)

def getAdjIndexes(r, c):
    return [(r+1, c), (r+1, c+1), (r, c+1), (r-1, c+1), (r-1, c), (r-1, c-1), (r, c-1), (r+1, c-1)]

def getDigitNeighbors(indexes):
    neighbors = []
    for r, c in indexes:
        if r < 0 or r > rows - 1 or c < 0 or c > cols - 1:
            continue
        if not array[r][c].isdigit():
            continue 
        neighbors.append((r, c))
    return neighbors

def deleteDigit(coordinate):
    r, c = coordinate
    if not array[r][c].isdigit():
        return
    
    array[r][c] = "."
    if c > 0:
        deleteDigit((r, c-1))
    if c < cols - 1:
        deleteDigit((r, c+1))

for r, line in enumerate(array):
    for c, char in enumerate(line):
        if char in symbols:
            for neighbor in getDigitNeighbors(getAdjIndexes(r, c)):
                deleteDigit(neighbor)

for line in array:
    res = re.findall("\d+", "".join(line))
    for num in res:
        sum_not_parts += int(num)

print(sum_all - sum_not_parts)
