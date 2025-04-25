from collections import deque

n = int(input())

def get_last_card(cards):
    deck = deque(range(1, cards + 1))

    # deck = deque()
    # for i in range(1, cards + 1):
    #     deck.append(i)

    while len(deck) > 1:
        deck.popleft()
        get_card = deck.popleft()
        deck.append(get_card)

    return print(deck[0])

get_last_card(n)

