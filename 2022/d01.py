#!/bin/python3

# calories each elf is carrying (input)
# each inventory is seperated by a new line
# find elf with most calories

# get top x elves carrying calories
top = 3

with open("d01.input") as file:
    calories = file.read().splitlines()

total = []
current = 0
for row in calories:
    if row == "":
        total.append(current)
        current = 0
    else:
        current += int(row)

total.sort(reverse=True)

# part 1
print(f"Elf with most has '{total[0]}' calories")

# part 2
top_total = 0
for x in range(top):
    top_total += total[x]
print(f"Top {top} elves have '{top_total}' calories")
