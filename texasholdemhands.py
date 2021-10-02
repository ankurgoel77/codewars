#https://www.codewars.com/kata/524c74f855025e2495000262/train/python

from collections import Counter

rank_values = {"A":14, "K":13, "Q":12, "J":11, "10":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
cards = {14:"A", 13:"K", 12:"Q", 11:"J", 10:"10", 9:"9", 8:"8", 7:"7", 6:"6", 5:"5", 4:"4", 3:"3", 2:"2"}

def is4(cnt_ranks):
    if cnt_ranks[-1][1] == 4:
        return (True, cnt_ranks[-1][0])
    else:
        return (False,)

def isFullHouse(cnt_ranks):
    if cnt_ranks[-1][1] == 3 and cnt_ranks[-2][1] == 2:
        return (True, cnt_ranks[-1][0], cnt_ranks[-2][0])
    else:
        return (False,)

def is3(cnt_ranks):
    if cnt_ranks[-1][1] == 3:
        return (True, cnt_ranks[-1][0])
    else:
        return (False,)

def isFlush(cnt_suits):
    return cnt_suits[-1][1] >= 5

def is2Pair(cnt_ranks):
    if cnt_ranks[-1][1] == 2 and cnt_ranks[-2][1] == 2:
        high = max(cnt_ranks[-1][0], cnt_ranks[-2][0], key=lambda x: rank_values[x])
        low = min(cnt_ranks[-1][0], cnt_ranks[-2][0], key=lambda x: rank_values[x])
        return (True, high, low)
    else:
        return (False,)

def isPair(cnt_ranks):
    if cnt_ranks[-1][1] == 2 and cnt_ranks[-2][1] == 1:
        return (True, cnt_ranks[-1][0])
    else:
        return (False,)
    
def isStraight(val_ranks):
    val = val_ranks[0]
    val2 = val_ranks[1]
    val3 = val_ranks[2]
    if len(val_ranks) >= 5 and val_ranks[1] == val-1 and val_ranks[2] == val-2 and val_ranks[3] == val-3 and val_ranks[4] == val-4:
        return (True, [cards[val_ranks[i]] for i in range(0,5)])
    elif len(val_ranks) >= 6 and val_ranks[2] == val2-1 and val_ranks[3] == val2-2 and val_ranks[4] == val2-3 and val_ranks[5] == val2-4:
        return (True, [cards[val_ranks[i]] for i in range(1,6)])
    elif len(val_ranks) >= 7 and val_ranks[3] == val3-1 and val_ranks[4] == val3-2 and val_ranks[5] == val3-3 and val_ranks[6] == val3-4:
        return (True, [cards[val_ranks[i]] for i in range(2,7)])
    else:
        return (False,)


def hand(hole_cards, community_cards):
    ranks= [cards[:-1] for cards in hole_cards+community_cards]
    suits = [cards[-1] for cards in hole_cards+community_cards]
    cnt_ranks = sorted(Counter(ranks).items(), key=lambda x: x[1])
    cnt_suits = sorted(Counter(suits).items(), key = lambda x: x[1])
    val_ranks = sorted(set([rank_values[i] for i in ranks]), reverse=True)


    if isFlush(cnt_suits):
        flush_ranks = sorted(set([rank_values[ranks[i]] for i in range(0,7) if suits[i] == cnt_suits[-1][0] ]), reverse=True)
        straight_flush = isStraight(flush_ranks)
        if straight_flush[0]:
            return ("straight-flush",straight_flush[1])
    
    four = is4(cnt_ranks)
    if four[0]:
        remaining_ranks = [rank for rank in ranks if not rank == four[1]]
        remaining_ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
        return ("four-of-a-kind", [four[1], remaining_ranks[0]])

    full = isFullHouse(cnt_ranks)
    if full[0]:
        return ("full house", [full[1], full[2]])

    if isFlush(cnt_suits):
        remaining_ranks = [ranks[i] for i in range(0,7) if suits[i] == cnt_suits[-1][0]]
        remaining_ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
        return ("flush", remaining_ranks[:5])

    straight = isStraight(val_ranks)
    if straight[0]:
        return ("straight", straight[1])

    three = is3(cnt_ranks)
    if three[0]:
        remaining_ranks = [rank for rank in ranks if not rank == three[1]]
        remaining_ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
        return ("three-of-a-kind", [three[1], remaining_ranks[0], remaining_ranks[1]])

    twopair = is2Pair(cnt_ranks)
    if twopair[0]:
        remaining_ranks = [rank for rank in ranks if not rank == twopair[1] and not rank==twopair[2]]
        remaining_ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
        return ("two pair", [twopair[1],twopair[2],remaining_ranks[0]])

    pair = isPair(cnt_ranks)
    if pair[0]:
        remaining_ranks = [rank for rank in ranks if not rank == pair[1]]
        remaining_ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
        return ("pair", [pair[1], remaining_ranks[0], remaining_ranks[1], remaining_ranks[2]])

    ranks.sort(key=lambda rank: rank_values[rank], reverse=True)
    return ("nothing", ranks[:5])


hole = ["A♠", "K♦"]
comm = ["J♥", "5♥", "10♥", "Q♥", "3♥"]

hole = ["8♠", "6♠"] 
comm= ["7♠", "5♠", "9♠", "J♠", "10♠"]

# hole = ["2♠", "3♦"] 
# comm =  ["2♣", "2♥", "3♠", "3♥", "2♦"]

# hole = ["A♠", "A♦"]
# comm = ["K♣", "K♥", "A♥", "Q♥", "3♦"]

# hole = ["A♠", "K♦"]
# comm = ["J♥", "5♥", "10♥", "Q♥", "3♥"]

# hole = ["Q♠", "2♦"]
# comm= ["J♣", "10♥", "9♥", "K♥", "3♦"]

# hole = ["4♠", "9♦"]
# comm = ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]

# hole = ["K♠", "Q♦"]
# comm= ["J♣", "Q♥", "9♥", "2♥", "3♦"]

# hole = ["K♠", "J♦"]
# comm= ["J♣", "K♥", "9♥", "2♥", "3♦"]

print(hand(hole,comm))