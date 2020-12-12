def day8():
    game_code = [line.rstrip() for line in open('input.txt')]

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


if __name__ == '__main__':
    day8()