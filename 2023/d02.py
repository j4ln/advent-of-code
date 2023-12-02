class Game:
    id: str
    sets: list[dict]


def parse_game_sets(sets):
    parsed_sets = []

    for set in sets.split(";"):
        parsed_set = {}
        for item in set.split(","):
            parts = item.strip().split(" ")
            parsed_set[parts[1]] = int(parts[0])
        parsed_sets.append(parsed_set)

    return parsed_sets


def parse_game(game_line):
    game = Game()

    # Get game id
    game_number = game_line.split(":")[0]  # "Game 1"
    game.id = int("".join(filter(str.isdigit, game_number)))

    # Get sets for game
    sets = game_line.split(":")[1]
    game.sets = parse_game_sets(sets)

    # Return parsed game
    return game


def solve_p1(games):
    max_red = 12
    max_green = 13
    max_blue = 14
    matching_game_ids = []

    for game in games:
        matching = True

        # Check each set is below the max count allowed
        for set in game.sets:
            if (
                set.get("red", 0) > max_red
                or set.get("green", 0) > max_green
                or set.get("blue", 0) > max_blue
            ):
                matching = False

        if matching:
            matching_game_ids.append(game.id)

    print(sum(matching_game_ids))  # a: 2176


def solve_p2(games):
    power = 0
    for game in games:
        max_red_seen = 0
        max_green_seen = 0
        max_blue_seen = 0

        # Get max number of each colour seen in the game
        for set in game.sets:
            red = set.get("red", 0)
            green = set.get("green", 0)
            blue = set.get("blue", 0)
            if red > max_red_seen:
                max_red_seen = red
            if green > max_green_seen:
                max_green_seen = green
            if blue > max_blue_seen:
                max_blue_seen = blue

        # Get power
        power_of_game = max_red_seen * max_green_seen * max_blue_seen
        power += power_of_game
    print(power)  # a: 63700


with open("d02.input") as file:
    input = file.read().splitlines()

games = []
for line in input:
    game = parse_game(line)
    games.append(game)

solve_p1(games)
solve_p2(games)
