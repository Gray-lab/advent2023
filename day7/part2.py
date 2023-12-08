from collections import defaultdict

def handScore(hand) -> int:
    # Five of a kind: 7
    # Four of a kind: 6
    # Full House: 5
    # Three of a kind: 4
    # Two pair: 3
    # One pair: 2
    # High card: 1

    counts = defaultdict(int)
    joker_count = 0
    for ch in hand:
        if ch != "J":
            counts[ch] += 1
        else:
            joker_count += 1

    # next, figure out where to put the joker to maximize result ?
    # or just make the scoring logic really complex :P
    if joker_count == 0:
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
    else:
        if len(counts) == 0 or len(counts) == 1:
            # all jokers or jokers and one other card
            return 7
        elif len(counts) == 2:
            # could be either a full house or 4 of a kind:
            if max(counts.values()) + joker_count == 4:
                return 6
            else:
                return 5
        elif len(counts) == 3:
            # has to be 3 of a kind - 2 pair isn't possible
            # J ABCC
            # JJ ABC
            return 4
        elif len(counts) == 4:
            # J ABCD
            return 2
        # and finally, high card isn't possible since the J can pair with anything


def cardScore(card: str) -> int:
    match card:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "T":
            return 10
        case "J":
            return 1
        case _:
            return int(card)


hands_bids = []
total = 0
with open("input.txt") as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands_bids.append((hand, int(bid)))
hands_bids.sort(key = lambda x: (handScore(x[0]), cardScore(x[0][0]), cardScore(x[0][1]), cardScore(x[0][2]), cardScore(x[0][3]), cardScore(x[0][4])))
for i, item in enumerate(hands_bids):
    total += item[1] * (i + 1)

print(total)
