from math import lcm


def traverse_route(route, paths, start_node, part2=False):
    node = start_node
    steps = 0
    while not node.endswith("Z") if part2 else node != "ZZZ":
        if route[0] == "L":
            node = paths[node][0]
        elif route[0] == "R":
            node = paths[node][1]

        route.append(route.pop(0))
        steps += 1
    return steps


with open("d08.input") as file:
    input = list(filter(None, file.read().split("\n")))

route = list(input[0])
paths = {}
for path in input[1:]:
    path = (
        path.replace(" =", "")
        .replace("(", "")
        .replace(",", "")
        .replace(")", "")
        .split()
    )
    paths[path[0]] = [path[1], path[2]]

# part 1
steps = traverse_route(route, paths, "AAA")
print(steps)  # a: 20513

# part 2
travel_nodes = [path for path in paths if path.endswith("A")]
steps = []
for i, node in enumerate(travel_nodes):
    steps.append(traverse_route(route, paths, node, True))
print(lcm(*steps))  # a: 15995167053923
