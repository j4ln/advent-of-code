#!/usr/bin/python3

with open("d06.input") as file:
    input = file.read().splitlines()


def get_stream(marker_count):
    count = 0
    stream = []
    for character in input[0]:
        if len(stream) < marker_count:
            stream.append(character)
        else:
            stream.pop(0)
            stream.append(character)
        count += 1

        if len(set(stream)) == marker_count:
            return count


# Part 1
print(get_stream(4))

# Part 2
print(get_stream(14))
