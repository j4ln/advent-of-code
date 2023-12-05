with open("d04.input") as file:
    input = file.read().splitlines()

# Parse each line
cards = []
for line in input:
    card_details = line.split(":")[1]
    winning_numbers = list(filter(None, card_details.split("|")[0].split(" ")))
    chosen_numbers = list(filter(None, card_details.split("|")[1].split(" ")))
    cards.append({"winning": winning_numbers, "chosen": chosen_numbers})

for card in cards:
    # Get matched numbers for card
    matched_numbers = []
    for winning_num in card["winning"]:
        if winning_num in card["chosen"]:
            matched_numbers.append(winning_num)
    card["matched"] = matched_numbers

    # Get points for card
    points = 0
    for i in range(1, len(card["matched"]) + 1):
        if i == 1:
            points = 1
        else:
            points = points * 2
    card["points"] = points

# Part 1
print(sum([card["points"] for card in cards]))  # a: 20829

# Part 2
cards = [{"owned": 1, **card} for card in cards]
for card_index, card in enumerate(cards):
    # Increment owned count on won card copies
    won_copy_count = len(card["matched"]) + 1
    for pos_ahead in range(1, won_copy_count):
        cards[card_index + pos_ahead]["owned"] += card["owned"]

print(sum([card["owned"] for card in cards]))  # a: 12648035
