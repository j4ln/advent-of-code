with open("d01.input") as file:
    input = file.read().splitlines()

calibration_sum = 0
word_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_word_digits(line: str):
    for key, value in word_digits.items():
        line = line.replace(key, f"{key}{value}{key}")
    return line


for line in input:
    parsed_line = parse_word_digits(line)
    values = "".join(char for char in parsed_line if char.isdigit())
    calibration_sum += int(f"{values[0]}{values[-1]}")

print(calibration_sum)
