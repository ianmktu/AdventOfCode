def day23():
    cup_string = "925176834"
    starting_cups = [int(i) for i in cup_string]

    def process_cups(starting_cups, number_of_cups, rounds=100):
        cups = [int(i) for i in range(1, number_of_cups + 1)]
        for i in range(len(starting_cups)):
            cups[i] = starting_cups[i]

        cup_label_to_next_label_map = {}
        for i in range(len(cups)):
            current_cup_value = cups[i]
            next_cup_value = cups[(i+1) % len(cups)]
            cup_label_to_next_label_map[current_cup_value] = next_cup_value
        max_label = max(cup_label_to_next_label_map.keys())

        max_rounds = rounds
        current_cup_node = cups[0]
        for _ in range(max_rounds):
            next_cup_node = current_cup_node        
            for i in range(4):
                next_cup_node = cup_label_to_next_label_map[next_cup_node]

            picked_cup_nodes = []
            current_picked_node = current_cup_node
            for i in range(3):
                current_picked_node = cup_label_to_next_label_map[current_picked_node]
                picked_cup_nodes.append(current_picked_node)
            
            for i in range(3):
                del cup_label_to_next_label_map[picked_cup_nodes[i]]
                
            label = current_cup_node - 1
            if label in picked_cup_nodes or label not in cup_label_to_next_label_map:
                while True:
                    label -= 1
                    if label in cup_label_to_next_label_map:
                        break
                    if label <= 0:
                        label = max_label + 1

            label_node_next = cup_label_to_next_label_map[label]
            cup_label_to_next_label_map[label] = picked_cup_nodes[0]
            cup_label_to_next_label_map[picked_cup_nodes[0]] = picked_cup_nodes[1]
            cup_label_to_next_label_map[picked_cup_nodes[1]] = picked_cup_nodes[2]
            cup_label_to_next_label_map[picked_cup_nodes[2]] = label_node_next

            cup_label_to_next_label_map[current_cup_node] = next_cup_node
            current_cup_node = next_cup_node

        return cup_label_to_next_label_map


    # Part 1
    cup_label_to_next_label_map = process_cups(
        starting_cups, number_of_cups=len(starting_cups), rounds=100
    )
    str_num_list = []
    node = cup_label_to_next_label_map[1]
    str_num_list.append(str(node))
    for _ in range(len(cup_label_to_next_label_map) - 2):
        node = cup_label_to_next_label_map[node]
        str_num_list.append(str(node))
    part1_string = ("").join(str_num_list)


    # Part 2
    cup_label_to_next_label_map = process_cups(
        starting_cups, number_of_cups=1000000, rounds=10000000
    )
    first_cup_node = cup_label_to_next_label_map[1]
    second_cup_node = cup_label_to_next_label_map[first_cup_node]
        

    print("\n****************************************************")
    print("\nDay 23: Part 1")
    print("Answer: {}".format(part1_string))

    print("\nDay 23: Part 2")
    print("Answer: {}".format(first_cup_node * second_cup_node))
    print("\n****************************************************")


if __name__ == '__main__':
    day23()
