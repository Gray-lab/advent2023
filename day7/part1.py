from collections import defaultdict

def handScore(hand) -> int:
    counts = defaultdict(int)
    for ch in hand:
        counts[ch] += 1

    print(counts)
    if len(counts) == 1:
        # Five of a kind
        return 7
    elif len(counts) == 2:
        if max(counts.values()) == 4:
            # Four of a kind
            return 6
        else:
            # Full House
            return 5
    elif len(counts) == 3:
        if max(counts.values()) == 3:
            # Three of a kind
            return 4
        else:
            # Two pair
            return 3
    elif len(counts) == 4:
        # One pair
        return 2
    elif len(counts) == 5:
        # High card
        return 1
    

def cardScore(card: str) -> int:
    match card:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 11
        case "T":
            return 10
        case _:
            return int(card)
        

hands_bids = []
total = 0
with open("input.txt") as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands_bids.append((hand, int(bid)))
hands_bids.sort(key = lambda x: (handScore(x[0]), 
                                 cardScore(x[0][0]), 
                                 cardScore(x[0][1]), 
                                 cardScore(x[0][2]), 
                                 cardScore(x[0][3]), 
                                 cardScore(x[0][4])))
for i, item in enumerate(hands_bids):
    total += item[1] * (i + 1)

print(total)
