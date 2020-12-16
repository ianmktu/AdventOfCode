def day16():
    ticket_data = [line.rstrip() for line in open('input.txt')]

    separator_count = 0
    rules = {}
    my_ticket = None
    nearby_tickets = []
    for line in ticket_data:
        if line == "":
            separator_count += 1
            continue

        if separator_count == 0:
            colon_split = line.split(":")
            rule_name = colon_split[0]    
            or_split = colon_split[1].split("or")

            first_range_split = or_split[0].strip().split("-")
            first_range_min = int(first_range_split[0])
            first_range_max = int(first_range_split[1])

            second_range_split = or_split[1].strip().split("-")
            second_range_min = int(second_range_split[0])
            second_range_max = int(second_range_split[1])

            current_rule_set = set()
            current_rule_set.update(range(first_range_min, first_range_max + 1))
            current_rule_set.update(range(second_range_min, second_range_max + 1))

            rules[rule_name] = current_rule_set
        elif separator_count == 1:
            if line == "your ticket:":
                continue
            my_ticket = [int(x) for x in line.split(",")]
        else:
            if line == "nearby tickets:":
                continue
            current_nearby_ticket = [int(x) for x in line.split(",")]
            nearby_tickets.append(current_nearby_ticket)
        
    error_sum = 0
    fixed_nearby_tickets =[]
    for current_nearby_ticket in nearby_tickets:
        valid_ticket = True
        for num in current_nearby_ticket:
            in_a_rule = False
            for rule_set in rules.values():
                if num in rule_set:
                    in_a_rule = True
                    break
            if not in_a_rule:
                error_sum += num
                valid_ticket = False
        if valid_ticket:
            fixed_nearby_tickets.append(current_nearby_ticket)

    rule_deduction_list = []
    for _ in range(len(my_ticket)):
        rule_deduction_list.append(set(rules.keys()))

    for current_nearby_ticket in fixed_nearby_tickets:
        for index, num in enumerate(current_nearby_ticket):   
            remove_rules = set()        
            for rule_name in rule_deduction_list[index]:
                if num not in rules[rule_name]:
                    remove_rules.add(rule_name)
            rule_deduction_list[index] -= remove_rules

    found_rules = {}
    while True:
        for i, current_rules in enumerate(rule_deduction_list):
            if len(current_rules) == 1:
                found_rules[list(current_rules)[0]] = i
            else:
                rule_deduction_list[i] -= set(found_rules.keys())
        if len(found_rules) == len(my_ticket):
            break

    departure_product = 1
    for rule_name, index in found_rules.items():
        if 'departure' in rule_name:
            departure_product *= my_ticket[index]

    print("\n****************************************************")
    print("\nDay 16: Part 1")
    print("Answer: {}".format(error_sum))

    print("\nDay 16: Part 2")
    print("Answer: {}".format(departure_product))
    print("\n****************************************************")


if __name__ == '__main__':
    day16()