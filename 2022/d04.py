#!/usr/bin/python3

with open("d04.input") as file:
    input = file.read().splitlines()

contain_count = 0
overlap_count = 0
for line in input:
    pairs = line.split(",")
    numbers = [pairs[0].split("-"), pairs[1].split("-")]

    # Part 1
    if (int(numbers[0][0]) <= int(numbers[1][0]) and int(numbers[0][1]) >= int(numbers[1][1])):
       contain_count += 1
    elif (int(numbers[1][0]) <= int(numbers[0][0]) and int(numbers[1][1]) >= int(numbers[0][1])):
       contain_count += 1

    # Part 2
    if (int(numbers[0][0]) <= int(numbers[1][1]) and int(numbers[0][1]) >= int(numbers[1][1])):
        overlap_count += 1
    elif (int(numbers[1][0]) <= int(numbers[0][1]) and int(numbers[1][1]) >= int(numbers[0][1])):
        overlap_count += 1

print(contain_count)
print(overlap_count)
