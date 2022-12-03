#!/usr/bin/python3

with open("d03.input") as file:
    input = file.read().splitlines()


def get_priority(item):
    # Get item priority value
    if item.islower():
        # a-z = 1-26
        priority = ord(item) - 96
    elif item.isupper():
        # A-Z = 27-52
        priority = ord(item) - 38

    return priority


# Part 1

# Find duplicate items between compartments
total_duplicate = []
for line in input:
    length = len(line) // 2
    rucksack = [line[:length], line[length:]]

    duplicate = []
    for item in rucksack[0]:
        priority = get_priority(item)
        if priority not in duplicate and item in rucksack[1]:
            duplicate.append(priority)
    total_duplicate.append(sum(duplicate))

print(sum(total_duplicate))


# Part 2

# Group input
group_input = []
group = []
for line in input:
    if len(group) < 3:
        group.append(line)

    if len(group) == 3:
        group_input.append(group)
        group = []

# Find common group item
total_common = []
for group in group_input:

    # Inner function so we can exit early one matched
    def find_common_item():
        for item in group[0]:
            if item in group[1] and item in group[2]:
                return item

    common_item = find_common_item()
    total_common.append(get_priority(common_item))

print(sum(total_common))
