def day1():
    digits = [line.rstrip() for line in open('input.txt')]
    digits = [int(d) for d in digits]
    digits.sort()
    digit_map = dict((digit, index) for index, digit in enumerate(digits))

    print("\n****************************************************")
    print("\nDay 1: Part 1")
    for current_index, current_digit in enumerate(digits):
        if 2020 - current_digit in digit_map and digit_map[2020 - current_digit] != current_index:
            print(current_digit, 2020 - current_digit)
            print("Answer:",current_digit * (2020 - current_digit))
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
    print("\n****************************************************")


if __name__ == '__main__':
    day1()