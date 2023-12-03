import re

sum_all = 0
array = []

with open("input.txt") as f:
    for line in f.readlines():
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

def getNumber(coordinate):
    r, c = coordinate
    if not array[r][c].isdigit():
        raise ValueError("Non-digit target in getNumber!")
    
    start_index = c
    while start_index > 0 and array[r][start_index - 1].isdigit():
        start_index -= 1
    return (re.search("\d+", ''.join(array[r][start_index:])).group(), (r, start_index))


for r, line in enumerate(array):
    for c, char in enumerate(line):
        if char == "*":
            neighbors = getDigitNeighbors(getAdjIndexes(r, c))
            neighbor_dict = {}
            for digit, coordinate in [getNumber(neighbor) for neighbor in neighbors]:
                neighbor_dict[coordinate] = int(digit)
            res = 1
            if len(neighbor_dict) == 2:
                for value in neighbor_dict.values():
                    res *= value
                sum_all += res

print(sum_all)
