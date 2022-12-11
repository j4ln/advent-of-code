#!/usr/bin/python3

with open("d08.input") as file:
    input = file.read().splitlines()


def check_visible(trees, index_row, index_column, tree_height):
    trees_column = []
    for row in trees:
        trees_column.append(row[index_column])

    top_trees = trees_column[:index_row]
    bottom_trees = trees_column[index_row + 1 :]
    left_trees = trees[index_row][:index_column]
    right_trees = trees[index_row][index_column + 1 :]

    if (
        max(left_trees, default=-1) < tree_height
        or max(right_trees, default=-1) < tree_height
    ):
        return True

    if (
        max(top_trees, default=-1) < tree_height
        or max(bottom_trees, default=-1) < tree_height
    ):
        return True


def get_viewing_distance(trees, reverse, tree_height):
    if reverse == True:
        trees.reverse()

    if trees == []:
        return 1

    distance = 0
    for tree in trees:
        distance += 1
        if tree >= tree_height:
            break
    return distance


def get_scenic_score(trees, index_row, index_column, tree_height):
    trees_column = []
    for row in trees:
        trees_column.append(row[index_column])

    top_trees = trees_column[:index_row]
    bottom_trees = trees_column[index_row + 1 :]
    left_trees = trees[index_row][:index_column]
    right_trees = trees[index_row][index_column + 1 :]

    top_score = get_viewing_distance(top_trees, True, tree_height)
    bottom_score = get_viewing_distance(bottom_trees, False, tree_height)
    left_score = get_viewing_distance(left_trees, True, tree_height)
    right_score = get_viewing_distance(right_trees, False, tree_height)

    scenic_score = top_score * bottom_score * left_score * right_score
    return scenic_score


trees = []
for line in input:
    trees.append([int(x) for x in line])

visible_tree_count = 0
scenic_scores = []
for row in enumerate(trees):
    index_row = row[0]
    row = row[1]

    for tree in enumerate(row):
        index_column = tree[0]
        tree_height = tree[1]

        # Part 1
        tree_visible = check_visible(trees, index_row, index_column, tree_height)
        if tree_visible:
            visible_tree_count += 1

        # Part 2
        scenic_scores.append(
            get_scenic_score(trees, index_row, index_column, tree_height)
        )

print(visible_tree_count)
print(max(scenic_scores))
