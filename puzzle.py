import copy
import data

import numpy as np

import anytree
from anytree import Node, RenderTree


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
                print(earliest_time, timestamp, count, bus_id)
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

    def multiply_list(input):
        result = 1
        for x in input:
            result *= x
        return result

    found_time = 0
    for i in range(1, len(bus_id_min_offset)):
        current_bus_ids = [bus_id for bus_id, _ in bus_id_min_offset[0:i-1]]
        found_time = find_time(input_bus_id_min_offset=bus_id_min_offset[0:i+1],
                               start_time=found_time,
                               increment=multiply_list(current_bus_ids))

        print(i, multiply_list(current_bus_ids), current_bus_ids, found_time)

    print("\n****************************************************")
    print("\nDay 13: Part 1")
    print("Answer: {}".format(earliest_time * found_bus_id))

    print("\nDay 13: Part 2")
    print("Answer: {}".format(found_time))
    print("\n****************************************************")


def day14():
    puzzle_input = data.day14()

    print("\n****************************************************")
    print("\nDay 14: Part 1")
    print("Answer: {}".format(0000))

    print("\nDay 14: Part 2")
    print("Answer: {}".format(0000))
    print("\n****************************************************")


def day15():
    puzzle_input = data.day15()

    print("\n****************************************************")
    print("\nDay 15: Part 1")
    print("Answer: {}".format(0000))

    print("\nDay 15: Part 2")
    print("Answer: {}".format(0000))
    print("\n****************************************************")


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
    day14()
    # day15()
    # day16()
    # day17()
    # day18()
    # day19()
    # day20()
    # day21()
    # day22()
    # day23()
    # day24()
    # day25()