import anytree
from anytree import Node, RenderTree


def day7():
    bags = [line.rstrip() for line in open('input.txt')]

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
    bags = [line.rstrip() for line in open('input.txt')]

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


if __name__ == '__main__':
    day7()
    day7_alt()