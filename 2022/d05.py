#!/usr/bin/python3

import re

with open("d05.input") as file:
    input = file.read().splitlines()

# Get the arrangement of stacks and moves as seperate lists
split_index = input.index("")
arrangement_input = input[:split_index]
moves_input = input[split_index + 1 :]
arrangement_input.reverse()

# Get number of stacks
stacks = arrangement_input.pop(0).split(" ")
stacks = [x for x in stacks if x.strip()]
stack_total = int(stacks[-1])

# Read arrangement of stacks into a workable state
# Stack stored per index with crates ordered by botom to top within
arrangement = [[] for i in range(stack_total)]
for line in arrangement_input:
    for stack_num in range(stack_total):
        crate = line[1 + (4 * stack_num) : 2 + (4 * stack_num)]
        if crate != " ":
            arrangement[stack_num].append(crate)

# Read moves into list
moves = []
for line in moves_input:
    move = list(map(int, re.findall(r"\d+", line)))
    moves.append(move)


# Part 1
def arrange_part_one():
    for move in moves:
        for i in range(move[0]):
            crate = arrangement[move[1] - 1].pop()
            arrangement[move[2] - 1].append(crate)


# Part 2
def arrange_part_two():
    for move in moves:
        temp_crates = []

        for i in range(move[0]):
            crate = arrangement[move[1] - 1].pop()
            temp_crates.append(crate)

        temp_crates.reverse()
        arrangement[move[2] - 1].extend(temp_crates)


# Solve
# arrange_part_one()
arrange_part_two()

code = ""
for stack in arrangement:
    code += stack[-1]

print(code)
