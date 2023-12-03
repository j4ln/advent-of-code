class SchematicNumber:
    def __init__(self, row, number, start_pos, end_pos):
        self.row = row
        self.number = number
        self.start_pos = start_pos
        self.end_pos = end_pos


def parse_numbers(line, row_index):
    numbers = []
    start_pos = 0
    number = ""
    for char_pos, char in enumerate(line):
        if char.isdigit():
            if number == "":
                start_pos = char_pos
            number = f"{number}{char}"

        if (not char.isdigit() and number != "") or (
            char_pos == len(line) - 1 and char.isdigit()
        ):
            schematic_number = SchematicNumber(
                row_index, int(number), start_pos, char_pos
            )
            numbers.append(schematic_number)
            start_pos = 0
            number = ""

    return numbers


def get_schematic_numbers(schematic):
    schematic_numbers = []
    for row_index, line in enumerate(schematic):
        line_numbers = parse_numbers(line, row_index)
        schematic_numbers.extend(line_numbers)
    return schematic_numbers


def get_part_numbers(schematic, schematic_numbers):
    def has_symbol(rows):
        for row in rows:
            for char in row:
                if not (char.isdigit()) and char != ".":
                    # Symbol found
                    return True

    part_numbers = []
    for number in schematic_numbers:
        row = number.row
        start_check_pos = max(number.start_pos - 1, 0)
        end_check_pos = min(number.end_pos + 1, len(schematic[row]))

        # Get adjacent strings from surrounding area for checking
        rows_to_check = []
        rows_to_check.append(schematic[row][start_check_pos:end_check_pos])
        if row != 0:
            rows_to_check.append(schematic[row - 1][start_check_pos:end_check_pos])
        if row != (len(schematic) - 1):
            rows_to_check.append(schematic[row + 1][start_check_pos:end_check_pos])

        # If symbol is adjacent then we have found a part number
        if has_symbol(rows_to_check):
            part_numbers.append(int(number.number))
    return part_numbers


def get_gear_ratios(schematic, schematic_numbers):
    gear_ratios = []
    for row_index, line in enumerate(schematic):
        for char_pos, char in enumerate(line):
            if char == "*":
                # Search adjacent of possible gear for part numbers
                matching_numbers = [
                    number.number
                    for number in schematic_numbers
                    if set(range(number.start_pos, number.end_pos))
                    & set([char_pos - 1, char_pos, char_pos + 1])
                    and number.row in [row_index - 1, row_index, row_index + 1]
                ]

                # If two part numbers are adjacent then we have found a gear
                if len(matching_numbers) == 2:
                    gear_ratios.append(matching_numbers[0] * matching_numbers[1])
    return gear_ratios


def main():
    with open("d03.input") as file:
        input = file.read().splitlines()

    # part 1
    schematic_numbers = get_schematic_numbers(input)
    part_numbers = get_part_numbers(input, schematic_numbers)
    print(sum(part_numbers))  # a: 514969

    # part 2
    gear_ratios = get_gear_ratios(input, schematic_numbers)
    print(sum(gear_ratios))  # a: 78915902


if __name__ == "__main__":
    main()
