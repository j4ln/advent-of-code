from itertools import pairwise


def next_value(numbers):
    distances = [b - a for (a, b) in pairwise(numbers)]
    if sum(distances) != 0:
        increment = next_value(distances)
        return increment + numbers[-1]
    else:
        return numbers[-1]


def prev_value(numbers):
    distances = [b - a for (a, b) in pairwise(numbers)]
    if sum(distances) != 0:
        reduction = prev_value(distances)
        return numbers[0] - reduction
    else:
        return numbers[0]


with open("d09.input") as file:
    input = file.read().splitlines()

for i, line in enumerate(input):
    input[i] = list(int(num) for num in line.split())

# part 1
next = [next_value(line) for line in input]
print(sum(next))  # a: 1762065988

# part 2
prev = [prev_value(line) for line in input]
print(sum(prev))  # a: 1066
