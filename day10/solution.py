def day10():
    jolt_strings = [line.rstrip() for line in open('input.txt')]
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


if __name__ == '__main__':
    day10()