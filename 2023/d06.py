def parse_input(input):
    times = input[0].split(":")[1].split()
    distances = input[1].split(":")[1].split()
    return zip(map(int, times), map(int, distances))


def parse_input_pt2(input):
    time = input[0].split(":")[1].replace(" ", "")
    distance = input[1].split(":")[1].replace(" ", "")
    return [[int(time), int(distance)]]


def get_race_strats(race):
    strats = []
    for i in range(race[0]):
        distance = i * (race[0] - i)
        if distance > race[1]:
            strats.append(i)
    return strats


with open("d06.input") as file:
    input = file.read().splitlines()

# Parse input
races = parse_input(input)
race_strats = [get_race_strats(race) for race in races]

# Part 1
product = 1
for strats in race_strats:
    product *= len(strats)
print(product)  # a: 800280

# Part 2
races = parse_input_pt2(input)
race_strats = [get_race_strats(race) for race in races]
print(len(race_strats[0]))  # a: 45128024
