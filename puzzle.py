import numpy as np
import data


def day1():
    digits = data.day1()
    digits.sort()
    digit_map = dict((digit, index) for index, digit in enumerate(digits))

    print("\n****************************************************")
    print("\nDay 1: Part 1")
    for current_index, current_digit in enumerate(digits):
        if 2020 - current_digit in digit_map and digit_map[2020 - current_digit] != current_index:
            print(current_digit, 2020 - current_digit)
            print(current_digit * (2020 - current_digit))
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
            print(digit_pairs_map[2020 - third_num][0] * digit_pairs_map[2020 - third_num][1] * third_num)
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

    print("Total Trees 3-1: {}".format(num_trees))
    print("Total Open Spaces: {}".format(num_open_spaces))

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
    print("\nDay 5: Part 1")
    print("Answer Count: {}".format(sum(answer_count)))

    print("\nDay 5: Part 2")
    print("Consensus Count: {}".format(sum(consensus_count)))


def day7():
    current = data.day7()


if __name__ == '__main__':
    # day1()
    # day2()
    # day3()
    # day4()
    # day5()
    # day6()
    day7()