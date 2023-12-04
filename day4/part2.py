total_cards = 0
cards = [] # list of card tuples (lists to keep it mutable) -> [counts, matches]
with open("input.txt") as f:
    for line in f.readlines():
        winning, ours = line[9:].split('|')
        winning = set(winning.split())
        ours = set(ours.split())
        matches = winning.intersection(ours)
        
        cards.append([1, len(matches)])

for i, card in enumerate(cards):
    copies, matches = card
    total_cards += copies
    for x in range(copies):
        for j in range(i+1, i+1+matches):
            if j >= len(cards):
                break
            cards[j][0] += 1

print(total_cards)