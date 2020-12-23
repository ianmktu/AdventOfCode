import llist
from llist import dllist, dllistnode

def day23():
    cup_string = "925176834"
    starting_cups = [int(i) for i in cup_string]

    def process_cups(starting_cups, number_of_cups, rounds=100):
        cups = [int(i) for i in range(1, number_of_cups + 1)]
        for i in range(len(starting_cups)):
            cups[i] = starting_cups[i]

        cup_linked_list = dllist(cups)

        cup_label_to_node_map = {}
        for i in range(len(cup_linked_list)):
            node = cup_linked_list.nodeat(i)
            cup_label_to_node_map[node.value] = node

        max_label = max(cup_label_to_node_map.keys())

        max_rounds = rounds
        current_cup_node = cup_linked_list.nodeat(0)
        for i in range(max_rounds):
            next_cup_node = current_cup_node        
            for i in range(4):
                next_cup_node = next_cup_node.next
                if next_cup_node is None:
                    next_cup_node = cup_linked_list.nodeat(0)

            picked_cups = []
            picked_cup_nodes = []
            current_picked_node = current_cup_node
            for i in range(3):
                current_picked_node = current_picked_node.next
                if current_picked_node is None:
                    current_picked_node = cup_linked_list.nodeat(0)
                picked_cups.append(current_picked_node.value)
                picked_cup_nodes.append(current_picked_node)
            
            for i in range(3):
                del cup_label_to_node_map[picked_cups[i]]
                cup_linked_list.remove(picked_cup_nodes[i])
                
            label = current_cup_node.value - 1
            if label in picked_cups or label not in cup_label_to_node_map:
                while True:
                    label -= 1
                    if label in cup_label_to_node_map and label != current_cup_node.value:
                        break
                    if label <= 0:
                        label = max_label + 1

            label_node = cup_label_to_node_map[label]
            label_node_next = label_node.next
            if label_node_next is None:
                label_node = None
                label_node_next = cup_linked_list.nodeat(0)

            cup_linked_list.insert(picked_cups[0], label_node_next)
            cup_linked_list.insert(picked_cups[1], label_node_next)
            cup_linked_list.insert(picked_cups[2], label_node_next)

            if label_node is None:
                cup_label_to_node_map[picked_cups[0]] = cup_linked_list.nodeat(0)
                cup_label_to_node_map[picked_cups[1]] = cup_linked_list.nodeat(0).next
                cup_label_to_node_map[picked_cups[2]] = cup_linked_list.nodeat(0).next.next
            else:
                cup_label_to_node_map[picked_cups[0]] = label_node.next
                cup_label_to_node_map[picked_cups[1]] = label_node.next.next
                cup_label_to_node_map[picked_cups[2]] = label_node.next.next.next

            current_cup_node = next_cup_node
        return cup_linked_list, cup_label_to_node_map


    # Part 1
    cup_linked_list, cup_label_to_node_map = process_cups(
        starting_cups, number_of_cups=len(starting_cups), rounds=100
    )
    node = cup_label_to_node_map[1]
    str_num_list = []
    for _ in range(len(cup_linked_list) - 1):
        node = node.next
        if node is None:
            node = cup_linked_list.nodeat(0)
        str_num_list.append(str(node.value))
    part1_string = ("").join(str_num_list)


    # Part 2
    cup_linked_list, cup_label_to_node_map = process_cups(
        starting_cups, number_of_cups=1000000, rounds=10000000
    )
    node1 = cup_label_to_node_map[1]
    first_cup_node = node1.next
    if first_cup_node is None:
        first_cup_node = cup_linked_list.nodeat(0)
    second_cup_node = first_cup_node.next
    if second_cup_node is None:
        second_cup_node = cup_linked_list.nodeat(0)
        

    print("\n****************************************************")
    print("\nDay 23: Part 1")
    print("Answer: {}".format(part1_string))

    print("\nDay 23: Part 2")
    print("Answer: {}".format(first_cup_node.value * second_cup_node.value))
    print("\n****************************************************")


if __name__ == '__main__':
    day23()
