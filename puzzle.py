import copy
import data

import itertools
import numpy as np

import anytree
from anytree import Node, RenderTree

from math import gcd
from functools import reduce 

def day1():
    digits = data.day1()
    digits = [int(d) for d in digits]
    digits.sort()
    digit_map = dict((digit, index) for index, digit in enumerate(digits))

    print("\n****************************************************")
    print("\nDay 1: Part 1")
    for current_index, current_digit in enumerate(digits):
        if 2020 - current_digit in digit_map and digit_map[2020 - current_digit] != current_index:
            print(current_digit, 2020 - current_digit)
            print("Answer:", current_digit * (2020 - current_digit))
            break

    print("\nDay 1: Part 2")
    digit_pairs_map = {}
    for i, first_num in enumerate(digits):
        for j, second_num in enumerate(digits):
            if i == j:
                continue
            current_sum = first_num + second_num
            if current_sum <= 2020:
                digit_pairs_map[current_sum] = (first_num, second_num, i, j)
            else:
                break

    for k, third_num in enumerate(digits):
        if 2020 - third_num in digit_pairs_map:
            first_index = digit_pairs_map[2020 - third_num][2]
            second_index = digit_pairs_map[2020 - third_num][3]
            if first_index == k or second_index == k:
                continue
            print(digit_pairs_map[2020 - third_num][0], digit_pairs_map[2020 - third_num][1], third_num)
            print("Answer:", digit_pairs_map[2020 - third_num][0] * digit_pairs_map[2020 - third_num][1] * third_num)
            break


def day2():
    password_strings = data.day2()
    passwords = []

    valid_part1 = 0
    invalid_part1 = 0

    valid_part2 = 0
    invalid_both_part2 = 0
    invalid_none_part2 = 0
    for s in password_strings:
        space_split_str = s.split(" ")
        char_limit_arr = space_split_str[0].split("-")

        min_char_limit = int(char_limit_arr[0])
        max_char_limit = int(char_limit_arr[1])
        required_char = space_split_str[1][0]
        password = space_split_str[2]

        current_char_count_in_password = password.count(required_char)
        if min_char_limit <= current_char_count_in_password <= max_char_limit:
            valid_part1 += 1
        else:
            invalid_part1 += 1

        need_char_at_here1 = int(char_limit_arr[0])
        need_char_at_here2 = int(char_limit_arr[1])

        if (need_char_at_here1 - 1 < len(password) and password[need_char_at_here1 - 1] == required_char) and\
                (need_char_at_here2 - 1 < len(password) and password[need_char_at_here2 - 1] == required_char):
            invalid_both_part2 += 1
        elif (need_char_at_here1 - 1 < len(password) and password[need_char_at_here1 - 1] == required_char) or\
                (need_char_at_here2 - 1 < len(password) and password[need_char_at_here2 - 1] == required_char):
            valid_part2 += 1
        else:
            invalid_none_part2 += 1

    print("\n****************************************************")
    print("\nDay 2: Part 1")
    print("Valid: {}".format(valid_part1))
    print("Invalid: {}".format(invalid_part1))
    print("Total: {}".format(len(password_strings)))

    print("\nDay 2: Part 2")
    print("Valid: {}".format(valid_part2))
    print("Invalid Both: {}".format(invalid_both_part2))
    print("Invalid None: {}".format(invalid_none_part2))
    print("Total: {}".format(len(password_strings)))


def day3():
    geology = data.day3()

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


def day4():
    passports = data.day4()

    single_passports = []
    current_passport = {}
    for index, line in enumerate(passports):
        if line == "":
            single_passports.append(current_passport)
            current_passport = {}
        else:
            split_line = line.split(" ")
            for item in split_line:
                info = item.split(":")
                current_passport[info[0]] = info[1]

        if index == len(passports) - 1:
            single_passports.append(current_passport)
            current_passport = {}

    num_valid_passports = 0
    for passport in single_passports:
        if all(k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            num_valid_passports += 1

    print("\n****************************************************")
    print("\nDay 4: Part 1")
    print("Total Passports: {}".format(len(single_passports)))
    print("Valid Passports: {}".format(num_valid_passports))

    num_valid_passports = 0
    for passport in single_passports:
        if all(k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            if len(passport['byr']) == 4 and (int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
                continue
            if len(passport['iyr']) == 4 and (int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
                continue
            if len(passport['eyr']) == 4 and (int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030):
                continue
            if "cm" not in passport['hgt'] and "in" not in passport['hgt']:
                continue
            if "cm" in passport['hgt'] and (int(passport['hgt'].replace("cm", "")) < 150 or int(passport['hgt'].replace("cm", "")) > 193):
                continue
            if "in" in passport['hgt'] and (int(passport['hgt'].replace("in", "")) < 59 or int(passport['hgt'].replace("in", "")) > 76):
                continue
            valid_colour_chars = set('0123456789abcdef')
            if len(passport['hcl']) != 7 or passport['hcl'][0] != '#' or any((c not in valid_colour_chars) for c in passport['hcl'][1:]):
                continue
            if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                continue
            valid_pid_chars = set('0123456789')
            if len(passport['pid']) != 9 or any((c not in valid_pid_chars) for c in passport['pid']):
                continue
            num_valid_passports += 1

    print("\nDay 4: Part 2")
    print("Total Passports: {}".format(len(single_passports)))
    print("Valid Passports: {}".format(num_valid_passports))


def day5():
    seat_strings = data.day5()

    seat_ids = []
    for seat_string in seat_strings:
        start_row = 0
        end_row = 127

        for index, char in enumerate(seat_string[:7]):
            mid_point = int((start_row + end_row) / 2)
            if char == 'F':
                end_row = mid_point
            else:
                start_row = mid_point + 1

        row_id = -1
        if seat_string[6] == 'F':
            row_id = start_row
        else:
            row_id = end_row

        start_col = 0
        end_col = 7
        for index, char in enumerate(seat_string[7:-1]):
            mid_point = int((start_col + end_col) / 2)
            if char == 'L':
                end_col = mid_point
            else:
                start_col = mid_point + 1

        col_id = -1
        if seat_string[-1] == 'L':
            col_id = start_col
        else:
            col_id = end_col

        seat_id = row_id * 8 + col_id
        seat_ids.append(seat_id)

    seat_ids.sort()

    print("\n****************************************************")
    print("\nDay 5: Part 1")
    print("Total Seat IDs: {}".format(len(seat_strings)))
    print("Max Seat ID: {}".format(seat_ids[-1]))
    print("\nDay 5: Part 2")

    all_ids = set([i for i in range(seat_ids[0], seat_ids[-1] + 1)])
    missing_seat_ids = all_ids - set(seat_ids)
    for i, missing_seat_id in enumerate(missing_seat_ids):
        print("Missing Seat ID: {}".format(seat_id))


def day6():
    customs = data.day6()

    current_group = {}
    current_person_count = 0
    answer_count = []
    consensus_count = []
    for index, line in enumerate(customs):
        if line == "":            
            answer_count.append(len(current_group))

            current_consensus_count = 0
            for key, value in current_group.items():
                if value == current_person_count:
                    current_consensus_count += 1            
            consensus_count.append(current_consensus_count)

            current_group.clear()
            current_person_count = 0
        else:
            current_person_count += 1
            for char in line.strip():
                if char == " ":
                    continue
                if char in current_group:
                    current_group[char] += 1
                else:
                    current_group[char] = 1

        if index == len(customs) - 1:
            answer_count.append(len(current_group))

            current_consensus_count = 0
            for key, value in current_group.items():
                if value == current_person_count:
                    current_consensus_count += 1            
            consensus_count.append(current_consensus_count)

            current_group.clear()
            current_person_count = 0

    print("\n****************************************************")
    print("\nDay 6: Part 1")
    print("Answer Count: {}".format(sum(answer_count)))

    print("\nDay 6: Part 2")
    print("Consensus Count: {}".format(sum(consensus_count)))
    print("\n****************************************************")


def day7():
    bags = data.day7()

    bag_dict = {}
    for index, bag_description in enumerate(bags):
        bag_description_space_split = bag_description.split(" ")
        current_bag_name = bag_description_space_split[0] + " " + bag_description_space_split[1]
        bag_contains_list = bag_description.replace(current_bag_name + " bags contain ", "").replace("no other bags", "0 zero things").replace(" bags", "").replace(" bag", "").replace(".", "").split(", ")
        
        if current_bag_name not in bag_dict:
            bag_dict[current_bag_name] = {}
            bag_dict[current_bag_name]['children'] = []
            bag_dict[current_bag_name]['parent'] = []
            bag_dict[current_bag_name]['child_count'] = []

        for inner_bag_description in bag_contains_list:
            inner_bag_description_space_split = inner_bag_description.split(" ")
            current_bag_count = int(inner_bag_description_space_split[0])
            current_inner_bag_name = inner_bag_description_space_split[1] + " " + inner_bag_description_space_split[2]
            
            if current_bag_count > 0:
                bag_dict[current_bag_name]['children'].append(current_inner_bag_name)
                bag_dict[current_bag_name]['child_count'].append(current_bag_count)

            if current_inner_bag_name not in bag_dict:
                bag_dict[current_inner_bag_name] = {}
                bag_dict[current_inner_bag_name]['children'] = []
                bag_dict[current_inner_bag_name]['parent'] = []
                bag_dict[current_inner_bag_name]['child_count'] = []

            bag_dict[current_inner_bag_name]['parent'].append(current_bag_name)


    root_node = Node('root')
    for bag_name, adjacency_set_dict in bag_dict.items():
        parent_node_names = adjacency_set_dict['parent']

        if len(parent_node_names) == 0:
            parent_node = Node(bag_name, parent=root_node, count=1)
            children_node_names = [(child_bag_name, adjacency_set_dict['child_count'][index], parent_node) for index, child_bag_name in enumerate(adjacency_set_dict['children'])]

            while len(children_node_names) > 0:
                current_child_bag_name, current_child_bag_count, current_parent_bag_node = children_node_names.pop(0)
                current_child_node = Node(current_child_bag_name, parent=current_parent_bag_node, count=current_child_bag_count)
                current_child_node_names = [(child_bag_name, bag_dict[current_child_bag_name]['child_count'][index], current_child_node) for index, child_bag_name in enumerate(bag_dict[current_child_bag_name]['children'])]
                children_node_names += current_child_node_names
        else:
            continue
    
    shiny_nodes = anytree.search.findall_by_attr(root_node, 'shiny gold', name='name')
    shiny_names = set()
    for shiny_node in shiny_nodes:
        for shiny_ancestor_node in shiny_node.ancestors:
            shiny_names.add(shiny_ancestor_node.name)
    shiny_names.remove("root")
    
    def get_node_count(current_node):   
        if len(current_node.children) == 0:    
            return current_node.count
        else:
            current_total = 0
            for current_child_node in current_node.children:
                current_total += get_node_count(current_child_node) 
            current_total *= current_node.count
            current_total += current_node.count
            return current_total 

    shiny_count = 0 
    for child_node in shiny_nodes[0].children:
        shiny_count += get_node_count(child_node)

    print("\n****************************************************")
    print("\nDay 7: Part 1")
    print("Contain Shiny Gold Bag Count: {}".format(len(shiny_names)))

    print("\nDay 7: Part 2")
    print("In Shiny Gold Bag Count: {}".format(shiny_count))
    print("\n****************************************************")


def day7_alt():
    bags = data.day7()

    bag_dict = {}
    for index, bag_description in enumerate(bags):
        bag_description_space_split = bag_description.split(" ")
        current_bag_name = bag_description_space_split[0] + " " + bag_description_space_split[1]
        bag_contains_list = bag_description.replace(current_bag_name + " bags contain ", "").replace("no other bags", "0 zero things").replace(" bags", "").replace(" bag", "").replace(".", "").split(", ")
        
        if current_bag_name not in bag_dict:
            bag_dict[current_bag_name] = {}
            bag_dict[current_bag_name]['children'] = []
            bag_dict[current_bag_name]['parent'] = []
            bag_dict[current_bag_name]['child_count'] = {}

        for inner_bag_description in bag_contains_list:
            inner_bag_description_space_split = inner_bag_description.split(" ")
            current_bag_count = int(inner_bag_description_space_split[0])
            current_inner_bag_name = inner_bag_description_space_split[1] + " " + inner_bag_description_space_split[2]
            
            if current_bag_count > 0:
                bag_dict[current_bag_name]['children'].append(current_inner_bag_name)
                bag_dict[current_bag_name]['child_count'][current_inner_bag_name] = current_bag_count

            if current_inner_bag_name not in bag_dict:
                bag_dict[current_inner_bag_name] = {}
                bag_dict[current_inner_bag_name]['children'] = []
                bag_dict[current_inner_bag_name]['parent'] = []
                bag_dict[current_inner_bag_name]['child_count'] = {}

            bag_dict[current_inner_bag_name]['parent'].append(current_bag_name)

    chosen_bag_name = "shiny gold" 
    adjacency_set_dict = bag_dict[chosen_bag_name]
    ascendant_root_node = Node(chosen_bag_name)
    parent_node_names = [(bag_name, ascendant_root_node) for bag_name in adjacency_set_dict['parent']]
    while len(parent_node_names) > 0:
        current_bag_name, current_parent_bag_node = parent_node_names.pop(0)        
        current_node = Node(current_bag_name, parent=current_parent_bag_node)
        current_parent_node_names = [(bag_name, current_node) for bag_name in bag_dict[current_bag_name]['parent']]
        parent_node_names += current_parent_node_names
    shiny_names = set()
    for shiny_node in ascendant_root_node.descendants:
        shiny_names.add(shiny_node.name)
    
    chosen_bag_name = "shiny gold" 
    adjacency_set_dict = bag_dict[chosen_bag_name]
    descendant_root_node = Node(chosen_bag_name)
    children_node_names = [(bag_name, adjacency_set_dict['child_count'][bag_name], descendant_root_node) for bag_name in adjacency_set_dict['children']]
    while len(children_node_names) > 0:
        current_child_bag_name, current_child_bag_count, current_parent_bag_node = children_node_names.pop(0)
        for i in range(current_child_bag_count):
            current_child_node = Node(current_child_bag_name, parent=current_parent_bag_node)
            current_child_node_names = [(bag_name, bag_dict[current_child_bag_name]['child_count'][bag_name], current_child_node) for bag_name in bag_dict[current_child_bag_name]['children']]
            children_node_names += current_child_node_names

    print("\n****************************************************")
    print("\nDay 7: Part 1")
    print("Contain Shiny Gold Bag Count: {}".format(len(shiny_names)))

    print("\nDay 7: Part 2")
    print("In Shiny Gold Bag Count: {}".format(len(descendant_root_node.descendants)))
    print("\n****************************************************")


def day8():
    game_code = data.day8()

    index_count_set = set()
    index = 0
    accumulator_value = 0
    while True:
        if index in index_count_set:
            break
        else:
            index_count_set.add(index)

        instruction, value = game_code[index].split(" ")
        if instruction == "acc":
            index += 1
            accumulator_value += int(value)
        elif instruction == "nop":
            index += 1
        else:
            index += int(value)

    fixed_index = 0
    while True:
        for i in range(fixed_index, len(game_code)):
            if instruction == "nop":
                fixed_index = i 
                break
            elif instruction == "nop":
                fixed_index = i
                break
            else:
                continue

        index_count_set.clear()
        fixed_accumulator_value = 0        
        index = 0
        
        while True:
            if index in index_count_set:
                break
            elif index == len(game_code):
                break
            else:
                index_count_set.add(index)

            instruction, value = game_code[index].split(" ")
            if instruction == "acc":
                index += 1
                fixed_accumulator_value += int(value)
            elif instruction == "nop":
                if index == fixed_index:
                    index += int(value)
                else:
                    index += 1
            else:
                if index == fixed_index:
                    index += 1
                else:
                    index += int(value)


        if index == len(game_code):
            break
        else:
            fixed_index += 1

    print("\n****************************************************")
    print("\nDay 8: Part 1")
    print("Answer: {}".format(accumulator_value))

    print("\nDay 8: Part 2")
    print("Answer: {}".format(fixed_accumulator_value))
    print("\n****************************************************")


def day9():
    xmas_numbers = data.day9()

    rolling_number_dict = {}
    remove_num_at_index = 0
    invalid_number = 0
    for index, current_number in enumerate(xmas_numbers):
        if index < 25:
            if current_number not in rolling_number_dict:
                rolling_number_dict[current_number] = []
            rolling_number_dict[current_number].append(index)
        else:
            sum_exists = False
            for current_dict_number in rolling_number_dict.keys():
                if str(int(current_number) - int(current_dict_number)) in rolling_number_dict:
                    sum_exists = True
                    break            

            if not sum_exists:
                invalid_number = int(current_number)
                break
            else:
                if len(rolling_number_dict[xmas_numbers[remove_num_at_index]]) == 1:
                    del rolling_number_dict[xmas_numbers[remove_num_at_index]]
                else:
                    rolling_number_dict[xmas_numbers[remove_num_at_index]].remove(remove_num_at_index)
                remove_num_at_index += 1
                if current_number not in rolling_number_dict:
                    rolling_number_dict[current_number] = []
                rolling_number_dict[current_number].append(index)

    found_contigious = False
    min_value = 0
    max_value = 0
    for i, current_number1 in enumerate(xmas_numbers):
        current_sum = int(current_number1)
        for j, current_number2 in enumerate(xmas_numbers[i+1:]):
            current_sum += int(current_number2)
            if current_sum < invalid_number:
                continue
            elif current_sum > invalid_number:
                break
            else:
                found_contigious = True
                break
        if found_contigious:
            contigious_array = [int(x) for x in xmas_numbers[i:i+j+2]]
            assert sum(contigious_array) == invalid_number, \
                "\n\nError in Day 9: Part 2. \nFound array does not sum up to invalid number. \n     Got: {} \nExpected: {}".format(sum(contigious_array), invalid_number)
            min_value = min(contigious_array)
            max_value = max(contigious_array)
            break
            
    print("\n****************************************************")
    print("\nDay 9: Part 1")
    print("Answer: {}".format(invalid_number))

    print("\nDay 9: Part 2")
    print("Answer: {}".format(min_value + max_value))
    print("\n****************************************************")


def day10():
    jolt_strings = data.day10()
    jolt_integers =[int(j) for j in jolt_strings]
    jolt_integers.sort()

    jolt_1 = 0
    jolt_3 = 1
    previous_jolt = 0
    for index, jolt in enumerate(jolt_integers):
        if jolt - previous_jolt == 1:
            jolt_1 += 1
        elif jolt - previous_jolt == 3:
            jolt_3 += 1        
        previous_jolt = jolt

    
    jolt_integers.insert(0, 0)
    jolt_dict = {}
    jolt_dict[0] = []
    for index, current_jolt in enumerate(jolt_integers):
        for next_index in range(index + 1, len(jolt_integers)):
            if jolt_integers[next_index] - current_jolt <= 3:
                if jolt_integers[next_index] not in jolt_dict:
                    jolt_dict[jolt_integers[next_index]] = []
                jolt_dict[jolt_integers[next_index]].append(current_jolt)
            else:
                break


    def get_combo_count(connector_list, jolt_combo_count):   
        current_combo_count = 0
        for current_jolt in connector_list:
            if current_jolt in jolt_combo_count:
                current_combo_count += jolt_combo_count[current_jolt]
            else:
                current_combo_count += get_combo_count(jolt_dict[current_jolt], jolt_combo_count) 
        return current_combo_count 


    jolt_combo_count = {}
    jolt_combo_count[0] = 1

    for index, current_jolt in enumerate(jolt_integers[1:]):
        combo_count = 0
        for parent_jolt in jolt_dict[current_jolt]:
            if parent_jolt in jolt_combo_count:
                combo_count += jolt_combo_count[parent_jolt]
            else:
                new_combo_count = get_combo_count(jolt_dict[parent_jolt], jolt_combo_count) 
                jolt_combo_count[parent_jolt] = new_combo_count
                combo_count += jolt_combo_count[parent_jolt]
        jolt_combo_count[current_jolt] = combo_count

    print("\n****************************************************")
    print("\nDay 10: Part 1")
    print("Answer: {}".format(jolt_1 * jolt_3))

    print("\nDay 10: Part 2")
    print("Answer: {}".format(jolt_combo_count[jolt_integers[-1]]))
    print("\n****************************************************")


def day11():
    seating_rows = data.day11()

    seating_array = []
    for index, row in enumerate(seating_rows):
        seating_array.append([])
        for seat in row:
            seating_array[index].append(seat)
    seating_array_original = copy.deepcopy(seating_array)

    while True:
        previous_seating_array = copy.deepcopy(seating_array)
        for row_index, row in enumerate(previous_seating_array):                       
            for col_index, seat in enumerate(row):           
                occupied_count = 0
                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index - 1][col_index - 1] == "#":
                        occupied_count += 1

                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index < len(row) and \
                    previous_seating_array[row_index - 1][col_index] == "#":
                        occupied_count += 1

                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index - 1][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index + 1][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index < len(row) and \
                    previous_seating_array[row_index + 1][col_index] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index + 1][col_index - 1] == "#":
                        occupied_count += 1

                if 0 <= row_index < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index][col_index - 1] == "#":
                        occupied_count += 1

                if seat == "#" and occupied_count >= 4:
                    seating_array[row_index][col_index] = "L"
                elif seat == "L" and occupied_count == 0:
                    seating_array[row_index][col_index] = "#"
            
        stable = True
        final_occupied_count = 0
        for row_index in range(len(seating_array)):            
            for col_index in range(len(seating_array[row_index])):
                if seating_array[row_index][col_index] != previous_seating_array[row_index][col_index]:
                    stable = False
                    break                
                if seating_array[row_index][col_index] == "#":
                    final_occupied_count += 1
            if not stable:
                break

        if stable:
            break

    seating_array = copy.deepcopy(seating_array_original)
    while True:
        previous_seating_array = copy.deepcopy(seating_array)
        for row_index, row in enumerate(previous_seating_array):                       
            for col_index, seat in enumerate(row):           
                occupied_count = 0
                
                def is_occupied(y_dir, x_dir):
                    seeing_step = 1
                    while 0 <= row_index + y_dir * seeing_step < len(seating_array) and 0 <= col_index + x_dir * seeing_step < len(row):
                        if previous_seating_array[row_index + y_dir * seeing_step][col_index + x_dir * seeing_step] == "#":                            
                            return True
                        elif previous_seating_array[row_index + y_dir * seeing_step][col_index + x_dir * seeing_step] == "L":
                            return False
                        else:
                            seeing_step += 1
                    return False

                if is_occupied(y_dir=-1, x_dir=-1):
                    occupied_count += 1

                if is_occupied(y_dir=-1, x_dir=0):
                    occupied_count += 1

                if is_occupied(y_dir=-1, x_dir=1):
                    occupied_count += 1
                
                if is_occupied(y_dir=0, x_dir=1):
                    occupied_count += 1

                if is_occupied(y_dir=1, x_dir=1):
                    occupied_count += 1
                
                if is_occupied(y_dir=1, x_dir=0):
                    occupied_count += 1

                if is_occupied(y_dir=1, x_dir=-1):
                    occupied_count += 1

                if is_occupied(y_dir=0, x_dir=-1):
                    occupied_count += 1

                if seat == "#" and occupied_count >= 5:
                    seating_array[row_index][col_index] = "L"
                elif seat == "L" and occupied_count == 0:
                    seating_array[row_index][col_index] = "#"
            
        stable = True
        final_occupied_count_2 = 0
        for row_index in range(len(seating_array)):            
            for col_index in range(len(seating_array[row_index])):
                if seating_array[row_index][col_index] != previous_seating_array[row_index][col_index]:
                    stable = False
                    break                
                if seating_array[row_index][col_index] == "#":
                    final_occupied_count_2 += 1
            if not stable:
                break

        if stable:
            break

    print("\n****************************************************")
    print("\nDay 11: Part 1")
    print("Answer: {}".format(final_occupied_count))

    print("\nDay 11: Part 2")
    print("Answer: {}".format(final_occupied_count_2))
    print("\n****************************************************")


def day12():
    directions = data.day12()
    north = 0
    east = 0
    current_heading = 90
    heading_list = ["N", "E", "S", "W"]
    heading_list_reversed = heading_list[::-1]
    for direction_string in directions:
        direction = direction_string[0]
        direction_value = int(direction_string[1:])
        if direction == "N":
            north += direction_value
        elif direction == "S":
            north -= direction_value
        elif direction == "E":
            east += direction_value
        elif direction == "W":
            east -= direction_value
        elif direction == "R":
            current_heading += direction_value
        elif direction == "L":
            current_heading -= direction_value
        elif direction == "F":
            absolute_heading_index = (current_heading % 360) // 90
            if absolute_heading_index < 0:
                absolute_heading = heading_list_reversed[absolute_heading_index]
            else:
                absolute_heading = heading_list[absolute_heading_index]
            if absolute_heading == "N":
                north += direction_value
            elif absolute_heading == "S":
                north -= direction_value
            elif absolute_heading == "E":
                east += direction_value
            elif absolute_heading == "W":
                east -= direction_value

    waypoint_north = 1
    waypoint_east = 10
    current_north = 0
    current_east = 0
    heading_list = ["N", "E", "S", "W"]
    heading_list_reversed = heading_list[::-1]
    for direction_string in directions:
        direction = direction_string[0]
        direction_value = int(direction_string[1:])
        if direction == "N":
            waypoint_north += direction_value
        elif direction == "S":
            waypoint_north -= direction_value
        elif direction == "E":
            waypoint_east += direction_value
        elif direction == "W":
            waypoint_east -= direction_value
        elif direction == "R":               
            new_waypoint_north = waypoint_north   
            new_waypoint_east = waypoint_east      

            if waypoint_east >= 0:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 1) % 4
                east_new_absolute_heading = heading_list[east_new_absolute_heading_index]
            else:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 3) % 4
                east_new_absolute_heading = heading_list[east_new_absolute_heading_index]
            
            if east_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_east)
            elif east_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_east)
            elif east_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_east)
            elif east_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_east)

            if waypoint_north >= 0:
                north_new_absolute_heading_index = (direction_value % 360) // 90
                north_new_absolute_heading = heading_list[north_new_absolute_heading_index]
            else:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 2) % 4
                north_new_absolute_heading = heading_list[north_new_absolute_heading_index]

            if north_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_north)
            elif north_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_north)
            elif north_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_north)
            elif north_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_north)
            
            waypoint_north = new_waypoint_north
            waypoint_east = new_waypoint_east            
        elif direction == "L":
            new_waypoint_north = waypoint_north   
            new_waypoint_east = waypoint_east      

            if waypoint_east >= 0:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 2) % 4
                east_new_absolute_heading = heading_list_reversed[east_new_absolute_heading_index]
            else:
                east_new_absolute_heading_index = ((direction_value % 360) // 90)
                east_new_absolute_heading = heading_list_reversed[east_new_absolute_heading_index]
            if east_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_east)
            elif east_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_east)
            elif east_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_east)
            elif east_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_east)

            if waypoint_north >= 0:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 3) % 4
                north_new_absolute_heading = heading_list_reversed[north_new_absolute_heading_index]
            else:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 1) % 4
                north_new_absolute_heading = heading_list_reversed[north_new_absolute_heading_index]

            if north_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_north)
            elif north_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_north)
            elif north_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_north)
            elif north_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_north)
            
            waypoint_north = new_waypoint_north
            waypoint_east = new_waypoint_east
        elif direction == "F":
            current_north += direction_value * waypoint_north
            current_east += direction_value * waypoint_east

    print("\n****************************************************")
    print("\nDay 12: Part 1")
    print("Answer: {}".format(abs(north) + abs(east)))

    print("\nDay 12: Part 2")
    print("Answer: {}".format(abs(current_north) + abs(current_east)))
    print("\n****************************************************")


def day13():
    bus_info = data.day13()

    timestamp = int(bus_info[0])
    bus_ids = [b for b in bus_info[1].split(",")]

    earliest_time = np.inf
    found_bus_id = -1
    for bus_id in bus_ids:
        if bus_id == "x":
            continue
        bus_id = int(bus_id)
        count = 0
        while True:
            if (timestamp + count) % bus_id == 0:
                if count < earliest_time:
                    earliest_time = count
                    found_bus_id = bus_id
                break
            else:
                count += 1

    bus_ids_only = []
    bus_id_min_offset = []
    bus_id_min_offset_map = {}
    bus_id_and_offset = []
    for minute, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        else:
            bus_id_min_offset.append((int(bus_id), minute))
            bus_id_min_offset_map[int(bus_id)] = minute
            bus_ids_only.append(int(bus_id))
            bus_id_and_offset.append(int(bus_id) + minute)

    def find_time(input_bus_id_min_offset, start_time=0, increment=None):
        found_time = start_time
        if increment is None:
            increment = min([bus_id for bus_id, _ in input_bus_id_min_offset])
        while True:
            aligns = True
            for bus_id, minute in input_bus_id_min_offset:
                if (found_time + minute) % bus_id != 0:
                    aligns = False
                    break

            if aligns:
                return found_time

            found_time += increment
        return -1

    def lcm(denominators):
        return reduce(lambda a,b: a*b // gcd(a,b), denominators)

    found_time = 0
    for i in range(1, len(bus_id_min_offset)):
        current_bus_ids = [bus_id for bus_id, _ in bus_id_min_offset[0:i]]
        if len(current_bus_ids) == 1:
            current_bus_ids *= 2 
        found_time = find_time(input_bus_id_min_offset=bus_id_min_offset[0:i+1],
                               start_time=found_time,
                               increment=lcm(current_bus_ids))

    print("\n****************************************************")
    print("\nDay 13: Part 1")
    print("Answer: {}".format(earliest_time * found_bus_id))

    print("\nDay 13: Part 2")
    print("Answer: {}".format(found_time))
    print("\n****************************************************")


def day14():
    mask_data = data.day14()

    current_mask = ""
    mem_dict = {}
    for line in mask_data:
        if line.startswith("mask = "):
            current_mask = line.replace("mask = ", "")
        else:
            space_split = line.split(" ")
            mem_location_index = int(space_split[0][4:-1])
            unmasked_decimal_value = int(space_split[-1])
            unmasked_binary_value = "{0:#b}".format(unmasked_decimal_value)[2:].zfill(36)
            masked_binary_value_char_list = [""] * len(unmasked_binary_value)
            for index, mask_char in enumerate(current_mask):
                if mask_char == "X":
                    masked_binary_value_char_list[index] = unmasked_binary_value[index]
                elif mask_char == "0":
                    masked_binary_value_char_list[index] = "0"
                elif mask_char == "1":
                    masked_binary_value_char_list[index] = "1"
            masked_binary_value = ("").join(masked_binary_value_char_list)
            masked_decimal_value = int(masked_binary_value, 2)
            mem_dict[mem_location_index] = masked_decimal_value

    final_sum = sum([x for x in mem_dict.values()])

    current_mask = ""
    mem_dict_2 = {}
    for line in mask_data:
        if line.startswith("mask = "):
            current_mask = line.replace("mask = ", "")
        else:
            space_split = line.split(" ")
            mem_location_index_string = space_split[0][4:-1]
            decimal_value = int(space_split[-1])
            unmasked_binary_mem_location_index = "{0:#b}".format(int(mem_location_index_string))[2:].zfill(36)
            masked_binary_mem_location_index_char_list = [""] * len(unmasked_binary_mem_location_index)
            for index, mask_char in enumerate(current_mask):
                if mask_char == "X":
                    masked_binary_mem_location_index_char_list[index] = "X"
                elif mask_char == "0":
                    masked_binary_mem_location_index_char_list[index] = unmasked_binary_mem_location_index[index]
                elif mask_char == "1":
                    masked_binary_mem_location_index_char_list[index] = "1"

            masked_binary_mem_location_indices_string_list = []

            def get_all_binary_possibilities(index, binary_char_list, store_list):
                if index == len(binary_char_list):
                    store_list.append(binary_char_list)

                elif binary_char_list[index] == "X":
                    binary_char_list_0 = copy.deepcopy(binary_char_list)
                    binary_char_list_0[index] = "0"
                    get_all_binary_possibilities(index + 1, binary_char_list_0, store_list)

                    binary_char_list_1 = copy.deepcopy(binary_char_list)
                    binary_char_list_1[index] = "1"
                    get_all_binary_possibilities(index + 1, binary_char_list_1, store_list)
                else:
                    get_all_binary_possibilities(index + 1, binary_char_list, store_list)
            get_all_binary_possibilities(0,
                                         masked_binary_mem_location_index_char_list,
                                         masked_binary_mem_location_indices_string_list)
            for mem_index_char_list in masked_binary_mem_location_indices_string_list:
                masked_binary_mem_location_index = ("").join(mem_index_char_list)
                masked_mem_location_index_decimal_value = int(masked_binary_mem_location_index, 2)
                mem_dict_2[masked_mem_location_index_decimal_value] = decimal_value

    final_sum_2 = sum([x for x in mem_dict_2.values()])

    print("\n****************************************************")
    print("\nDay 14: Part 1")
    print("Answer: {}".format(final_sum))

    print("\nDay 14: Part 2")
    print("Answer: {}".format(final_sum_2))
    print("\n****************************************************")


def day15():
    game = data.day15()
    
    result = []
    for i in [2020, 30000000]:
        game_dict = {}
        for index, num in enumerate(game):
            game_dict[num] = index
        start_index = len(game)  
        previous_value = game[-1]

        for index in range(start_index, i):      
            if previous_value in game_dict:
                new_value = index - 1 - game_dict[previous_value]   
                game_dict[previous_value] = index - 1
                previous_value = new_value
            else:
                game_dict[previous_value] = index - 1
                previous_value = 0
                        
        result.append(previous_value)
    
    print("\n****************************************************")
    print("\nDay 15: Part 1")
    print("Answer: {}".format(result[0]))

    print("\nDay 15: Part 2")
    print("Answer: {}".format(result[1]))
    print("\n****************************************************")


def day16():
    ticket_data = data.day16()

    separator_count = 0
    rules = {}
    my_ticket = None
    nearby_tickets = []
    for line in ticket_data:
        if line == "":
            separator_count += 1
            continue

        if separator_count == 0:
            colon_split = line.split(":")
            rule_name = colon_split[0]    
            or_split = colon_split[1].split("or")

            first_range_split = or_split[0].strip().split("-")
            first_range_min = int(first_range_split[0])
            first_range_max = int(first_range_split[1])

            second_range_split = or_split[1].strip().split("-")
            second_range_min = int(second_range_split[0])
            second_range_max = int(second_range_split[1])

            current_rule_set = set()
            current_rule_set.update(range(first_range_min, first_range_max + 1))
            current_rule_set.update(range(second_range_min, second_range_max + 1))

            rules[rule_name] = current_rule_set
        elif separator_count == 1:
            if line == "your ticket:":
                continue
            my_ticket = [int(x) for x in line.split(",")]
        else:
            if line == "nearby tickets:":
                continue
            current_nearby_ticket = [int(x) for x in line.split(",")]
            nearby_tickets.append(current_nearby_ticket)
        
    error_sum = 0
    fixed_nearby_tickets =[]
    for current_nearby_ticket in nearby_tickets:
        valid_ticket = True
        for num in current_nearby_ticket:
            in_a_rule = False
            for rule_set in rules.values():
                if num in rule_set:
                    in_a_rule = True
                    break
            if not in_a_rule:
                error_sum += num
                valid_ticket = False
        if valid_ticket:
            fixed_nearby_tickets.append(current_nearby_ticket)

    rule_deduction_list = []
    for _ in range(len(my_ticket)):
        rule_deduction_list.append(set(rules.keys()))

    for current_nearby_ticket in fixed_nearby_tickets:
        for index, num in enumerate(current_nearby_ticket):   
            remove_rules = set()        
            for rule_name in rule_deduction_list[index]:
                if num not in rules[rule_name]:
                    remove_rules.add(rule_name)
            rule_deduction_list[index] -= remove_rules

    found_rules = {}
    while True:
        for i, current_rules in enumerate(rule_deduction_list):
            if len(current_rules) == 1:
                found_rules[list(current_rules)[0]] = i
            else:
                rule_deduction_list[i] -= set(found_rules.keys())
        if len(found_rules) == len(my_ticket):
            break

    departure_product = 1
    for rule_name, index in found_rules.items():
        if 'departure' in rule_name:
            departure_product *= my_ticket[index]

    print("\n****************************************************")
    print("\nDay 16: Part 1")
    print("Answer: {}".format(error_sum))

    print("\nDay 16: Part 2")
    print("Answer: {}".format(departure_product))
    print("\n****************************************************")


def day17():
    cube_locations = data.day17()

    original_cube_map = {}
    for y, line in enumerate(cube_locations):
        for x, character in enumerate(line):
            if character == "#":
                if x not in original_cube_map:
                    original_cube_map[x] = {}
                if y not in original_cube_map[x]:
                    original_cube_map[x][y] = {}
                original_cube_map[x][y][0] = True


    def get_cube_active_count(x, y, z, current_cube_map):
        on_count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    else:
                        if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j]:
                            on_count += 1
        return on_count

    def get_coords_of_cubes_to_turn_on(x, y, z, current_cube_map):
        open_space_coord_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    else:
                        if x + i in current_cube_map \
                            and y + j in current_cube_map[x + i] \
                            and z + k in current_cube_map[x + i][y + j]:
                            continue
                        else:
                            open_space_coord_list.append((x + i, y + j, z + k))

        coords_to_turn_on_list = []
        for open_space_coords in open_space_coord_list:
            x_current = open_space_coords[0]
            y_current = open_space_coords[1]
            z_current = open_space_coords[2]
            active_count = get_cube_active_count(x_current, y_current, z_current, current_cube_map)
            if active_count == 3:
                coords_to_turn_on_list.append(open_space_coords)
        return coords_to_turn_on_list
            
    current_cube_map = copy.deepcopy(original_cube_map)
    for cycle_index in range(6):
        next_cube_map = {}
        for x, y_map in current_cube_map.items():
            for y, z_map in y_map.items():
                for z in z_map.keys():
                    active_count = get_cube_active_count(
                        x, y, z, current_cube_map
                    )
                    if active_count == 2 or active_count == 3:
                        if x not in next_cube_map:
                            next_cube_map[x] = {}
                        if y not in next_cube_map[x]:
                            next_cube_map[x][y] = {}
                        next_cube_map[x][y][z] = True

                    coords_of_cubes_to_turn_on = get_coords_of_cubes_to_turn_on(
                        x, y, z, current_cube_map
                    )
                    for coords in coords_of_cubes_to_turn_on:
                        x_coord = coords[0]
                        y_coord = coords[1]
                        z_coord = coords[2]
                        if x_coord not in next_cube_map:
                            next_cube_map[x_coord] = {}
                        if y_coord not in next_cube_map[x_coord]:
                            next_cube_map[x_coord][y_coord] = {}
                        next_cube_map[x_coord][y_coord][z_coord] = True

        current_cube_map = copy.deepcopy(next_cube_map)

    cube_count_3d = 0
    for y_map in current_cube_map.values():        
        for z_map in y_map.values():
            for z in z_map.values():
                cube_count_3d += 1


    original_cube_map_4d = {}
    for y, line in enumerate(cube_locations):
        for x, character in enumerate(line):
            if character == "#":
                if x not in original_cube_map_4d:
                    original_cube_map_4d[x] = {}
                if y not in original_cube_map_4d[x]:
                    original_cube_map_4d[x][y] = {}
                if 0 not in original_cube_map_4d[x][y]:
                    original_cube_map_4d[x][y][0] = {}
                original_cube_map_4d[x][y][0][0] = True

    def get_cube_active_count_4d(x, y, z, w, current_cube_map):
        on_count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        else:
                            if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j] \
                                and w + l in current_cube_map[x + i][y + j][z + k]:
                                on_count += 1
        return on_count

    def get_coords_of_cubes_to_turn_on_4d(x, y, z, w, current_cube_map):
        open_space_coord_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        else:
                            if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j] \
                                and w + l in current_cube_map[x + i][y + j][z + k]:
                                continue
                            else:
                                open_space_coord_list.append((x + i, y + j, z + k, w + l))

        coords_to_turn_on_list = []
        for open_space_coords in open_space_coord_list:
            x_current = open_space_coords[0]
            y_current = open_space_coords[1]
            z_current = open_space_coords[2]
            w_current = open_space_coords[3]
            active_count = get_cube_active_count_4d(x_current, y_current, z_current, w_current, current_cube_map)
            if active_count == 3:
                coords_to_turn_on_list.append(open_space_coords)
        return coords_to_turn_on_list
            
    current_cube_map = copy.deepcopy(original_cube_map_4d)
    for cycle_index in range(6):
        next_cube_map = {}
        for x, y_map in current_cube_map.items():
            for y, z_map in y_map.items():
                for z, w_map in z_map.items():
                    for w in w_map.keys():
                        active_count = get_cube_active_count_4d(
                            x, y, z, w, current_cube_map
                        )
                        if active_count == 2 or active_count == 3:
                            if x not in next_cube_map:
                                next_cube_map[x] = {}
                            if y not in next_cube_map[x]:
                                next_cube_map[x][y] = {}
                            if z not in next_cube_map[x][y]:
                                next_cube_map[x][y][z] = {}
                            next_cube_map[x][y][z][w] = True

                        coords_of_cubes_to_turn_on = get_coords_of_cubes_to_turn_on_4d(
                            x, y, z, w, current_cube_map
                        )
                        for coords in coords_of_cubes_to_turn_on:
                            x_coord = coords[0]
                            y_coord = coords[1]
                            z_coord = coords[2]
                            w_coord = coords[3]
                            if x_coord not in next_cube_map:
                                next_cube_map[x_coord] = {}
                            if y_coord not in next_cube_map[x_coord]:
                                next_cube_map[x_coord][y_coord] = {}
                            if z_coord not in next_cube_map[x_coord][y_coord]:
                                next_cube_map[x_coord][y_coord][z_coord] = {}
                            next_cube_map[x_coord][y_coord][z_coord][w_coord] = True

        current_cube_map = copy.deepcopy(next_cube_map)

    cube_count_4d = 0
    for y_map in current_cube_map.values():        
        for z_map in y_map.values():
            for w_map in z_map.values():
                for w in w_map.values():
                    cube_count_4d += 1

    print("\n****************************************************")
    print("\nDay 17: Part 1")
    print("Answer: {}".format(cube_count_3d))

    print("\nDay 17: Part 2")
    print("Answer: {}".format(cube_count_4d))
    print("\n****************************************************")


def day18():
    expressions = data.day18()


    def evaluate(expression_list, in_brackets=False, previous_len=-1):
        token_list = []        
        broke_at_index = -1
        for current_token_index, token in enumerate(expression_list):
            if broke_at_index > 0 and current_token_index <= broke_at_index:
                continue

            if token.isnumeric() or isinstance(token, int) or token in ["+", "*"]:
                token_list.append(token)
            elif token == "(":
                current_token, broke_at_index = evaluate(
                    expression_list[current_token_index + 1:], 
                    in_brackets=True, 
                    previous_len=current_token_index + 1
                )
                token_list.append(current_token)
            elif token == ")":
                if in_brackets:
                    break
                else:
                    continue

        broke_at_index = current_token_index + previous_len

        current_value = None
        current_operator = None
        for current_token_index, token in enumerate(token_list):
            if current_token_index == 0:
                current_value = int(token)
            elif token in ["+", "*"]:
                current_operator = token
            elif isinstance(token, int) or token.isnumeric():
                if current_operator == "+":
                    current_value += int(token)
                elif current_operator == "*":
                    current_value *= int(token)

        return current_value, broke_at_index


    def evaluate2(expression_list, in_brackets=False, previous_len=-1):
        token_list = []        
        broke_at_index = -1
        for current_token_index, token in enumerate(expression_list):
            if broke_at_index > 0 and current_token_index <= broke_at_index:
                continue

            if token.isnumeric() or isinstance(token, int) or token in ["+", "*"]:
                token_list.append(token)
            elif token == "(":
                current_token, broke_at_index = evaluate2(
                    expression_list[current_token_index + 1:], 
                    in_brackets=True, 
                    previous_len=current_token_index + 1
                )
                token_list.append(current_token)
            elif token == ")":
                if in_brackets:
                    break
                else:
                    continue

        broke_at_index = current_token_index + previous_len

        current_token_index = 0
        while True:                
            if token_list[current_token_index] == "+":
                next_value = token_list.pop(current_token_index + 1)
                token_list.pop(current_token_index)
                previous_value = token_list.pop(current_token_index - 1)
                new_value = int(previous_value) + int(next_value)
                token_list.insert(current_token_index - 1, new_value)
            else:
                current_token_index += 1
            
            if current_token_index == len(token_list):
                break

        current_value = None
        current_operator = None
        for current_token_index, token in enumerate(token_list):
            if current_token_index == 0:
                current_value = int(token)
            elif token in ["+", "*"]:
                current_operator = token
            elif isinstance(token, int) or token.isnumeric():
                if current_operator == "+":
                    print(current_token_index, current_operator, current_value, token)
                    current_value += int(token)
                    print(current_token_index, current_value)
                elif current_operator == "*":
                    current_value *= int(token)

        return current_value, broke_at_index


    sum_of_answers_part_1 = 0
    sum_of_answers_part_2 =0
    for current_expression_index, expression in enumerate(expressions):
        expression_list = expression.replace("(", "( ").replace(")", " )").split(" ")        
        answer, _ = evaluate(expression_list)
        sum_of_answers_part_1 += answer

        answer, _ = evaluate2(expression_list)
        sum_of_answers_part_2 += answer        

    print("\n****************************************************")
    print("\nDay 18: Part 1")
    print("Answer: {}".format(sum_of_answers_part_1))

    print("\nDay 18: Part 2")
    print("Answer: {}".format(sum_of_answers_part_2))
    print("\n****************************************************")


def day19():
    rules_and_messages = data.day19()

    rules = {}
    for line in rules_and_messages:
        if line == "":
            break
        colon_split = line.split(":")
        rule_number = int(colon_split[0])
        rule_string = colon_split[1]
        if '"' in rule_string:
            speech_mark_split = rule_string.split('"')
            character = speech_mark_split[1]
            rules[rule_number] = character
        elif '|' in rule_string:
            pipe_split = rule_string.split('|')
            first_rule_options = pipe_split[0].strip().split(" ")
            second_rule_options = pipe_split[1].strip().split(" ")
            if len(first_rule_options) == 2 and len(second_rule_options) == 2:
                rules[rule_number] = [
                    [int(first_rule_options[0]), int(first_rule_options[1])], 
                    [int(second_rule_options[0]), int(second_rule_options[1])]
                ]
            elif len(first_rule_options) == 1 and len(second_rule_options) == 1:
                rules[rule_number] = [
                    [int(first_rule_options[0])], 
                    [int(second_rule_options[0])]
                ]
        else:
            space_split = rule_string.strip().split(' ')
            rules[rule_number] = [[int(n) for n in space_split]]


    def valid_message(message, rule_nos, next_rule_nos, rules, verbose=False):
        next_rule_nos = copy.deepcopy(next_rule_nos)
        if verbose:
            print(message, rule_nos, next_rule_nos)
        if isinstance(rule_nos, int):            
            return valid_message(message, rules[rule_nos], next_rule_nos, rules, verbose)
        if isinstance(rule_nos, list):           
            if isinstance(rule_nos[0], list):  
                if len(rule_nos) == 2:                     
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose) or \
                        valid_message(message, rule_nos[1], next_rule_nos, rules, verbose)
                else:
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose)
            else:
                if len(rule_nos) > 1: 
                    new_next_rule_nos = next_rule_nos + [x for x in rule_nos[1:][::-1]]
                    return valid_message(message, rule_nos[0], new_next_rule_nos, rules, verbose)
                else:
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose)
        if isinstance(rule_nos, str):   
            if not message.startswith(rule_nos):
                return False
            else:
                if len(message) == 1 and len(next_rule_nos) == 0:
                    return True
                else:
                    if len(message) == 1 and len(next_rule_nos) > 0:
                        return False
                    if len(next_rule_nos) == 0:
                        return False
                    else: 
                        new_rule_nos = next_rule_nos[-1]
                        new_next_rule_nos = next_rule_nos[:-1]
                        return valid_message(message[1:], new_rule_nos, new_next_rule_nos, rules, verbose)
        return False

    messages = []
    skip = True
    for line in rules_and_messages:
        if line == "":
            skip = False
            continue
        if skip:
            continue        
        messages.append(line)
        
    match_count = 0
    for message in messages:      
        if valid_message(message, 0, [], rules, False):
            match_count += 1
            
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    match_count2 = 0
    for message in messages:      
        if valid_message(message, 0, [], rules, False):
            match_count2 += 1
                          
    print("\n****************************************************")
    print("\nDay 19: Part 1")
    print("Answer: {}".format(match_count))

    print("\nDay 19: Part 2")
    print("Answer: {}".format(match_count2))
    print("\n****************************************************")


def day20():
    tile_strings = data.day20()

    tiles = {}
    current_id = -1
    current_tile = np.zeros((10,10), dtype=int)
    row_idx = 0
    for index, line in enumerate(tile_strings):
        if "Tile" in line:   
            if index > 0:      
                tiles[current_id] = current_tile
            current_tile = np.zeros((10,10), dtype=int)
            current_id = int(line.split(" ")[1][:-1])
            row_idx = 0
            continue

        if "" == line:  
            continue

        for col_idx, character in enumerate(line):
            if character == ".":      
                current_tile[row_idx, col_idx] = 0
            else:
                current_tile[row_idx, col_idx] = 1
            
        row_idx += 1

    tiles[current_id] = current_tile

    tile_to_side_info_map = {}
    for current_id, tile in tiles.items():
        tile_to_side_info_map[current_id] = {}

        tile_to_side_info_map[current_id]['top bottom'] = {}
        tile_to_side_info_map[current_id]['top bottom']['main side'] = "".join(list(str(i) for i in tile[0, :]))
        tile_to_side_info_map[current_id]['top bottom']['main side matches'] = set()
        tile_to_side_info_map[current_id]['top bottom']['opposite side'] = "".join(list(str(i) for i in tile[-1, :]))
        tile_to_side_info_map[current_id]['top bottom']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['top bottom reversed'] = {}
        tile_to_side_info_map[current_id]['top bottom reversed']['main side'] = "".join(list(str(i) for i in np.flip(tile[0, :])))
        tile_to_side_info_map[current_id]['top bottom reversed']['main side matches'] = set()
        tile_to_side_info_map[current_id]['top bottom reversed']['opposite side'] = "".join(list(str(i) for i in np.flip(tile[-1, :])))
        tile_to_side_info_map[current_id]['top bottom reversed']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['left right'] = {}
        tile_to_side_info_map[current_id]['left right']['main side'] = "".join(list(str(i) for i in tile[:, 0]))
        tile_to_side_info_map[current_id]['left right']['main side matches'] = set()
        tile_to_side_info_map[current_id]['left right']['opposite side'] = "".join(list(str(i) for i in tile[:, -1]))
        tile_to_side_info_map[current_id]['left right']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['left right reversed'] = {}
        tile_to_side_info_map[current_id]['left right reversed']['main side'] = "".join(list(str(i) for i in np.flip(tile[:, 0])))
        tile_to_side_info_map[current_id]['left right reversed']['main side matches'] = set()
        tile_to_side_info_map[current_id]['left right reversed']['opposite side'] = "".join(list(str(i) for i in np.flip(tile[:, -1])))
        tile_to_side_info_map[current_id]['left right reversed']['opposite side matches'] = set()


    compared_ids = set()
    for current_id1, tile1 in tiles.items():
        for current_id2, tile2 in tiles.items():
            if current_id1 == current_id2:
                continue
            if (current_id1, current_id2) in compared_ids or \
                (current_id2, current_id1) in compared_ids:
                continue

            for side1, side1_to_info_map in tile_to_side_info_map[current_id1].items():
                for side2, side2_to_info_map in tile_to_side_info_map[current_id2].items():
                    if side1_to_info_map['main side'] == side2_to_info_map['main side']:
                        side1_to_info_map['main side matches'].add(current_id2)
                        side2_to_info_map['main side matches'].add(current_id1)

                    if side1_to_info_map['opposite side'] == side2_to_info_map['opposite side']:
                        side1_to_info_map['opposite side matches'].add(current_id2)
                        side2_to_info_map['opposite side matches'].add(current_id1)

                    if side1_to_info_map['main side'] == side2_to_info_map['opposite side']:
                        side1_to_info_map['main side matches'].add(current_id2)
                        side2_to_info_map['opposite side matches'].add(current_id1)

                    if side1_to_info_map['opposite side'] == side2_to_info_map['main side']:
                        side1_to_info_map['opposite side matches'].add(current_id2)
                        side2_to_info_map['main side matches'].add(current_id1)

            compared_ids.update([(current_id1, current_id2), (current_id2, current_id1)])

    corner_ids = []
    for current_id, side_info_map in tile_to_side_info_map.items():
        is_corner = True
        for side_name, info_map in side_info_map.items():
            if len(info_map['main side matches'] | info_map['opposite side matches']) > 1:
                is_corner = False
                break                
        if is_corner:
            corner_ids.append(current_id)
            

    def matches(side_string, tile_id, tile_to_side_info_map):
        for side2, side2_to_info_map in tile_to_side_info_map[tile_id].items():
            if side_string == side2_to_info_map['main side']:
                return True
            if side_string == side2_to_info_map['opposite side']:
                return True        
        return False

    def get_sides(tile):
        top = "".join(list(str(i) for i in tile[0, :]))
        bottom = "".join(list(str(i) for i in tile[-1, :]))
        left = "".join(list(str(i) for i in tile[:, 0]))
        right = "".join(list(str(i) for i in tile[:, -1]))
        return {"top": top, "right":right, "bottom":bottom, "left":left}

    def get_connected_ids(tile_id, tile_to_side_info_map):
        side_to_info_map = tile_to_side_info_map[tile_id]
        set_list = set()
        for side_name, info_map in side_to_info_map.items():
            set_list.update(info_map['main side matches'])
            set_list.update(info_map['opposite side matches'])
        return set_list

    def rotate_flip(tile, transform_id):
        if transform_id == 0:
            return np.rot90(tile, k=1, axes=(1,0))
        elif transform_id == 1:
            return np.rot90(tile, k=2, axes=(1,0))        
        elif transform_id == 2:
            return np.rot90(tile, k=3, axes=(1,0))        
        elif transform_id == 3:
            return np.fliplr(tile)        
        elif transform_id == 4:
            return np.rot90(np.fliplr(tile), k=1, axes=(1,0))
        elif transform_id == 5:
            return np.rot90(np.fliplr(tile), k=2, axes=(1,0))        
        elif transform_id == 6:
            return np.rot90(np.fliplr(tile), k=3, axes=(1,0))        
        else:
            return tile

    def get_corner(
        corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='right', 
        connected_side2='bottom'):
        for i in range(8):
            correct_orientation = False
            current_tile = rotate_flip(
                tile=tiles[corner_id], 
                transform_id=i
            )        
            tile_sides = get_sides(tile=current_tile)

            connected_ids = get_connected_ids(
                tile_id=corner_id, 
                tile_to_side_info_map=tile_to_side_info_map
            )
            connected_ids_permutations = list(itertools.permutations(connected_ids))
            for connected_ids_permutation in connected_ids_permutations:
                connected_side_id1 = connected_ids_permutation[0]
                connected_side_id2 = connected_ids_permutation[1]
                if matches(tile_sides[connected_side1], connected_side_id1, tile_to_side_info_map) and \
                    matches(tile_sides[connected_side2], connected_side_id2, tile_to_side_info_map):
                    correct_orientation = True
                    break
            if correct_orientation:
                return current_tile, connected_side_id1, connected_side_id2
        return None, None, None 

    def get_general_tile(
        tile_id, 
        tiles,
        tile_to_side_info_map, 
        correct_side='left',
        correct_side_string=None,
        connected_side='right'):        
        for i in range(8):
            correct_orientation = False
            current_tile = rotate_flip(
                tile=tiles[tile_id], 
                transform_id=i
            )        
            tile_sides = get_sides(tile=current_tile)
            if tile_sides[correct_side] == correct_side_string:            
                correct_orientation = True        
                connected_ids = get_connected_ids(
                    tile_id=tile_id, 
                    tile_to_side_info_map=tile_to_side_info_map
                )
                side_to_id_map = {}
                for side, side_string in tile_sides.items():
                    for connected_tile_id in connected_ids:
                        if matches(side_string, connected_tile_id, tile_to_side_info_map):
                            side_to_id_map[side] = connected_tile_id
 
            if correct_orientation:
                return current_tile, side_to_id_map
        return None, None

    side_length = int(np.sqrt(len(tiles)))
    tile_id_location = np.full((side_length, side_length), -1, dtype=int)
    final_tiles = {}

    top_left_corner_id = corner_ids[0]
    top_left_corner_tile, right_side_id, bottom_side_id = get_corner(
        top_left_corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='right', 
        connected_side2='bottom'
    )

    final_tiles[top_left_corner_id] = top_left_corner_tile
    tile_id_location[0,0] = top_left_corner_id
    tile_id_location[0,1] = right_side_id
    tile_id_location[1,0] = bottom_side_id

    for i in range(1, side_length-1):
        tile_id = tile_id_location[0, i]
        current_tile, side_to_id_map = get_general_tile(
            tile_id, 
            tiles,
            tile_to_side_info_map, 
            correct_side='left',
            correct_side_string=get_sides(final_tiles[tile_id_location[0, i-1]])['right'],
            connected_side='right'
        )
        final_tiles[tile_id] = current_tile
        tile_id_location[0, i+1] = side_to_id_map['right']
        tile_id_location[1, i] = side_to_id_map['bottom']

    top_right_corner_id = tile_id_location[0, -1]
    top_right_corner_tile, left_side_id, bottom_side_id = get_corner(
        top_right_corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='left', 
        connected_side2='bottom'
    )

    final_tiles[top_right_corner_id] = top_right_corner_tile
    tile_id_location[1,-1] = bottom_side_id

    for j in range(1,side_length):
        for i in range(0, side_length):
            tile_id = tile_id_location[j, i]
            current_tile, side_to_id_map = get_general_tile(
                tile_id, 
                tiles,
                tile_to_side_info_map, 
                correct_side='top',
                correct_side_string=get_sides(final_tiles[tile_id_location[j-1, i]])['bottom'],
                connected_side='right' if i < side_length - 1 else 'left'
            )
            final_tiles[tile_id] = current_tile
            if j+1 < side_length:
                tile_id_location[j+1, i] = side_to_id_map['bottom']


    # For some reason it needs a transform to match the example
    # This puzzle was a pain, so I'm just going to keep this here as it works
    for current_id, tile in final_tiles.items():
        final_tiles[current_id] = rotate_flip(
            tile=tile[1:-1,1:-1], 
            transform_id=6
        )       

    rows = []
    for j in range(side_length):
        row = []
        for i in range(side_length):
            row.append(final_tiles[tile_id_location[j,i]])
        rows.append(np.concatenate(row, axis=0))
    final_image = np.concatenate(rows, axis=1)

    sea_monster = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]
    ]
    sea_monster = np.array(sea_monster)

    rough_count = []
    for transform_id in range(8):
        current_image = rotate_flip(
            tile=copy.deepcopy(final_image), 
            transform_id=transform_id
        )        

        resulting_image = copy.deepcopy(current_image)
        found_monsters = 0
        for j in range(current_image.shape[0] - sea_monster.shape[0]):
            for i in range(current_image.shape[1] - sea_monster.shape[1]): 
                count = 0           
                for sea_y in range(sea_monster.shape[0]):
                    for sea_x in range(sea_monster.shape[1]):
                        count += current_image[j+sea_y,i+sea_x] * sea_monster[sea_y, sea_x]
                if count == np.sum(sea_monster).astype(int):
                    found_monsters += 1
                    for sea_y in range(sea_monster.shape[0]):
                        for sea_x in range(sea_monster.shape[1]):
                            if sea_monster[sea_y, sea_x] == 1:
                                resulting_image[j+sea_y,i+sea_x] = 0
        if found_monsters > 0:
            rough_count.append(np.sum(resulting_image))    

    print("\n****************************************************")
    print("\nDay 20: Part 1")
    print("Answer: {}".format(np.prod(corner_ids, dtype=np.uint64)))

    print("\nDay 20: Part 2")
    print("Answer: {}".format(max(rough_count)))
    print("\n****************************************************")


def day21():
    current_data = data.day21()


def day22():
    current_data = data.day22()


def day23():
    current_data = data.day23()


def day24():
    current_data = data.day24()


def day25():
    current_data = data.day25()


if __name__ == '__main__':
    # day1()
    # day2()
    # day3()
    # day4()
    # day5()
    # day6()
    # day7()
    # day7_alt()
    # day8()
    # day9()
    # day10()
    # day11()
    # day12()
    # day13()
    # day14()
    # day15()
    # day16()
    # day17()
    # day18()
    day19()
    day20()
    # day21()
    # day22()
    # day23()
    # day24()
    # day25()