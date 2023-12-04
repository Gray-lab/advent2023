def getPointValue(matches: int) -> int:
    if matches == 0:
        return 0
    return 2 ** (matches - 1)

total_points = 0
with open("example.txt") as f:
    for line in f.readlines():
        winning, ours = line[9:].split('|')
        winning = set(winning.split())
        ours = set(ours.split())
        matches = winning.intersection(ours)
        
        total_points += getPointValue(len(matches))

print(total_points)
        

