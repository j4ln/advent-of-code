#!/usr/bin/python3

from enum import Enum


class MoveScore(Enum):
    X = 1  # rock
    Y = 2  # paper
    Z = 3  # scissors


class OutcomeScore(Enum):
    X = 0  # lose
    Y = 3  # draw
    Z = 6  # win


def select_move(opponent_move, outcome):
    match opponent_move, outcome:
        case ["A", "Y"] | ["B", "X"] | ["C", "Z"]:
            return "X"
        case ["B", "Y"] | ["C", "X"] | ["A", "Z"]:
            return "Y"
        case ["C", "Y"] | ["A", "X"] | ["B", "Z"]:
            return "Z"


with open("d02.input") as file:
    input = file.read().splitlines()

total = 0
for row in input:
    move = row.split()

    desired_move = select_move(move[0], move[1])
    total += MoveScore[desired_move].value
    total += OutcomeScore[move[1]].value

print(total)
