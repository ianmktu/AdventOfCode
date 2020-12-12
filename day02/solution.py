def day2():
    password_strings = [line.rstrip() for line in open('input.txt')]
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
    print("\n****************************************************")


if __name__ == '__main__':
    day2()