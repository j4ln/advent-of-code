def parse_input_map(input_map):
    map_lines = input_map.split(":")[1].strip().split("\n")
    ranges = []
    for line in map_lines:
        line_numbers = line.split()
        ranges.append(
            {
                "src_value": int(line_numbers[1]),
                "dst_value": int(line_numbers[0]),
                "range": int(line_numbers[2]),
            }
        )
    return ranges


def get_map_value(value, src_dst_map, reverse=False):
    for range in src_dst_map:
        if reverse:
            if (
                value >= range["dst_value"]
                and value <= range["dst_value"] + range["range"]
            ):
                pos = value - range["dst_value"]
                return range["src_value"] + pos
        else:
            if (
                value >= range["src_value"]
                and value <= range["src_value"] + range["range"]
            ):
                pos = value - range["src_value"]
                return range["dst_value"] + pos

    return value  # unmapped src values remain same for the dst


def get_location_value(seed):
    value = seed
    for range_map in range_maps:
        value = get_map_value(value, range_map)
    return value


def get_seed_value(location):
    value = location
    for range_map in reversed(range_maps):
        value = get_map_value(value, range_map, True)
    return value


with open("d05.input") as file:
    input_groups = file.read().split("\n\n")

# Parse input
seeds = input_groups[0].split(":")[1].split()
seeds = [int(seed) for seed in seeds]
range_maps = [
    parse_input_map(input_groups[1]),
    parse_input_map(input_groups[2]),
    parse_input_map(input_groups[3]),
    parse_input_map(input_groups[4]),
    parse_input_map(input_groups[5]),
    parse_input_map(input_groups[6]),
    parse_input_map(input_groups[7]),
]

# Part 1
locations = [get_location_value(seed) for seed in seeds]
print(min(locations))  # a: 177942185

# Part 2 (To revisit and optimise)
seed_pairs = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

location = 0
unmatched = True
while unmatched:
    seed = get_seed_value(location)
    for pair in seed_pairs:
        if seed >= pair[0] and seed <= pair[0] + pair[1]:
            unmatched = False
            break
    else:
        location += 1
print(location)  # a: 69841803
