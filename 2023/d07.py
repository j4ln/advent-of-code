from collections import Counter, defaultdict


def hand_type_strength(cards, joker=False):
    if joker:
        card_counts = Counter(cards)
        top_common = card_counts.most_common()[0][0]
        if top_common == "J" and len(card_counts.most_common()) > 1:
            top_common = card_counts.most_common()[1][0]
        cards = cards.replace("J", top_common)

    card_counts = sorted(Counter(cards).values(), reverse=True)
    return hand_types.index(card_counts)


def group_hand_types(hands, joker=False):
    hand_types = defaultdict(list)
    for hand in hands:
        strength = hand_type_strength(hand[0], joker)
        hand_types[strength].append(hand)

    return [v for k, v in sorted(hand_types.items())]


def sort_hand_types(hand_types, card_power):
    for type_group in hand_types:
        type_group.sort(key=lambda hand: [card_power.index(card) for card in hand[0]])


def total_winnings(hands, card_power, joker=False):
    hand_types = group_hand_types(hands, joker)
    sort_hand_types(hand_types, card_power)
    ranked_hands = [hand for hand_type in hand_types for hand in hand_type]
    return [(int(hand[1]) * (index + 1)) for index, hand in enumerate(ranked_hands)]


with open("d07.input") as file:
    input = file.read().splitlines()

hands = [[line.split()[0], line.split()[1]] for line in input]
hand_types = [
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1],
    [2, 2, 1],
    [3, 1, 1],
    [3, 2],
    [4, 1],
    [5],
]

# part 1
card_power = "23456789TJQKA"
print(sum(total_winnings(hands, card_power)))  # a: 250951660

# part 2
card_power = "J23456789TQKA"
print(sum(total_winnings(hands, card_power, True)))  # a: 251481660
