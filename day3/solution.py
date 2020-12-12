import numpy as np


def day3():
    geology = [line.rstrip() for line in open('input.txt')]

    print("\n****************************************************")
    print("\nDay 3: Part 1")
    num_trees = 0
    num_open_spaces = 0
    for index, line in enumerate(geology):
        if index == 0:
            continue

        position = index * 3
        if position >= len(line):
            extended_line = line * int(np.ceil((position + 1) / len(line)))
        else:
            extended_line = line

        if extended_line[position] == '#':
            num_trees += 1
        else:
            num_open_spaces += 1

    print("Total Open Spaces: {}".format(num_open_spaces))
    print("Total Trees 3-1: {}".format(num_trees))

    print("\nDay 3: Part 2")
    num_trees_1_1 = 0
    num_trees_3_1 = 0
    num_trees_5_1 = 0
    num_trees_7_1 = 0
    num_trees_1_2 = 0
    for index, line in enumerate(geology):
        if index == 0:
            continue

        position_1_1 = index
        position_3_1 = index * 3
        position_5_1 = index * 5
        position_7_1 = index * 7
        position_1_2 = int(index / 2)

        max_position = max(position_1_1, position_3_1, position_5_1, position_7_1, position_1_2)
        if max_position >= len(line):
            extended_line = line * int(np.ceil((max_position + 1) / len(line)))
        else:
            extended_line = line

        if extended_line[position_1_1] == '#':
            num_trees_1_1 += 1

        if extended_line[position_3_1] == '#':
            num_trees_3_1 += 1

        if extended_line[position_5_1] == '#':
            num_trees_5_1 += 1

        if extended_line[position_7_1] == '#':
            num_trees_7_1 += 1

        if index % 2 == 0 and extended_line[position_1_2] == '#':
            num_trees_1_2 += 1

    print("Total Trees 1-1: {}".format(num_trees_1_1))
    print("Total Trees 3-1: {}".format(num_trees_3_1))
    print("Total Trees 5-1: {}".format(num_trees_5_1))
    print("Total Trees 7-1: {}".format(num_trees_7_1))
    print("Total Trees 1-2: {}".format(num_trees_1_2))

    print("Total Open Spaces: {}".format(num_open_spaces))

    print("Product of Tree Counts: {}".format(
        num_trees_1_1 * num_trees_3_1 * num_trees_5_1 * num_trees_7_1 * num_trees_1_2))
    print("\n****************************************************")


if __name__ == '__main__':
    day3()