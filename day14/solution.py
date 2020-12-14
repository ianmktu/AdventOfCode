import copy


def day14():
    mask_data = [line.rstrip() for line in open('input.txt')]

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


if __name__ == '__main__':
    day14()
