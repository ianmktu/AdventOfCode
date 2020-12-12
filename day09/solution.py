def day9():
    xmas_numbers = [line.rstrip() for line in open('input.txt')]

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


if __name__ == '__main__':
    day9()