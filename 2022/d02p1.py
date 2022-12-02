#!/usr/bin/python3

from enum import Enum


class MoveScore(Enum):
    X = 1  # rock
    Y = 2  # paper
    Z = 3  # scissors


class OutcomeScore(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


with open("d02.input") as file:
    input = file.read().splitlines()

total = 0
for row in input:
    move = row.split()

    total += MoveScore[move[1]].value
    match move:
        case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
            total += OutcomeScore.DRAW.value
        case ["A", "Z"] | ["B", "X"] | ["C", "Y"]:
            total += OutcomeScore.LOSE.value
        case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
            total += OutcomeScore.WIN.value

print(total)
