import copy

def day19():
    rules_and_messages = [line.rstrip() for line in open('input.txt')]

    rules = {}
    for line in rules_and_messages:
        if line == "":
            break
        colon_split = line.split(":")
        rule_number = int(colon_split[0])
        rule_string = colon_split[1]
        if '"' in rule_string:
            speech_mark_split = rule_string.split('"')
            character = speech_mark_split[1]
            rules[rule_number] = character
        elif '|' in rule_string:
            pipe_split = rule_string.split('|')
            first_rule_options = pipe_split[0].strip().split(" ")
            second_rule_options = pipe_split[1].strip().split(" ")
            if len(first_rule_options) == 2 and len(second_rule_options) == 2:
                rules[rule_number] = [
                    [int(first_rule_options[0]), int(first_rule_options[1])], 
                    [int(second_rule_options[0]), int(second_rule_options[1])]
                ]
            elif len(first_rule_options) == 1 and len(second_rule_options) == 1:
                rules[rule_number] = [
                    [int(first_rule_options[0])], 
                    [int(second_rule_options[0])]
                ]
        else:
            space_split = rule_string.strip().split(' ')
            rules[rule_number] = [[int(n) for n in space_split]]


    def valid_message(message, rule_nos, next_rule_nos, rules, verbose=False):
        next_rule_nos = copy.deepcopy(next_rule_nos)
        if verbose:
            print(message, rule_nos, next_rule_nos)
        if isinstance(rule_nos, int):            
            return valid_message(message, rules[rule_nos], next_rule_nos, rules, verbose)
        if isinstance(rule_nos, list):           
            if isinstance(rule_nos[0], list):  
                if len(rule_nos) == 2:                     
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose) or \
                        valid_message(message, rule_nos[1], next_rule_nos, rules, verbose)
                else:
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose)
            else:
                if len(rule_nos) > 1: 
                    new_next_rule_nos = next_rule_nos + [x for x in rule_nos[1:][::-1]]
                    return valid_message(message, rule_nos[0], new_next_rule_nos, rules, verbose)
                else:
                    return valid_message(message, rule_nos[0], next_rule_nos, rules, verbose)
        if isinstance(rule_nos, str):   
            if not message.startswith(rule_nos):
                return False
            else:
                if len(message) == 1 and len(next_rule_nos) == 0:
                    return True
                else:
                    if len(message) == 1 and len(next_rule_nos) > 0:
                        return False
                    if len(next_rule_nos) == 0:
                        return False
                    else: 
                        new_rule_nos = next_rule_nos[-1]
                        new_next_rule_nos = next_rule_nos[:-1]
                        return valid_message(message[1:], new_rule_nos, new_next_rule_nos, rules, verbose)
        return False

    messages = []
    skip = True
    for line in rules_and_messages:
        if line == "":
            skip = False
            continue
        if skip:
            continue        
        messages.append(line)
        
    match_count = 0
    for message in messages:      
        if valid_message(message, 0, [], rules, False):
            match_count += 1
            
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    match_count2 = 0
    for message in messages:      
        if valid_message(message, 0, [], rules, False):
            match_count2 += 1
                          
    print("\n****************************************************")
    print("\nDay 19: Part 1")
    print("Answer: {}".format(match_count))

    print("\nDay 19: Part 2")
    print("Answer: {}".format(match_count2))
    print("\n****************************************************")


if __name__ == '__main__':
    day19()