def day18():
    expressions = [line.rstrip() for line in open('input.txt')]

    def evaluate(expression_list, in_brackets=False, previous_len=-1):
        token_list = []        
        broke_at_index = -1
        for current_token_index, token in enumerate(expression_list):
            if broke_at_index > 0 and current_token_index <= broke_at_index:
                continue

            if token.isnumeric() or isinstance(token, int) or token in ["+", "*"]:
                token_list.append(token)
            elif token == "(":
                current_token, broke_at_index = evaluate(
                    expression_list[current_token_index + 1:], 
                    in_brackets=True, 
                    previous_len=current_token_index + 1
                )
                token_list.append(current_token)
            elif token == ")":
                if in_brackets:
                    break
                else:
                    continue

        broke_at_index = current_token_index + previous_len

        current_value = None
        current_operator = None
        for current_token_index, token in enumerate(token_list):
            if current_token_index == 0:
                current_value = int(token)
            elif token in ["+", "*"]:
                current_operator = token
            elif isinstance(token, int) or token.isnumeric():
                if current_operator == "+":
                    current_value += int(token)
                elif current_operator == "*":
                    current_value *= int(token)

        return current_value, broke_at_index


    def evaluate2(expression_list, in_brackets=False, previous_len=-1):
        token_list = []        
        broke_at_index = -1
        for current_token_index, token in enumerate(expression_list):
            if broke_at_index > 0 and current_token_index <= broke_at_index:
                continue

            if token.isnumeric() or isinstance(token, int) or token in ["+", "*"]:
                token_list.append(token)
            elif token == "(":
                current_token, broke_at_index = evaluate2(
                    expression_list[current_token_index + 1:], 
                    in_brackets=True, 
                    previous_len=current_token_index + 1
                )
                token_list.append(current_token)
            elif token == ")":
                if in_brackets:
                    break
                else:
                    continue

        broke_at_index = current_token_index + previous_len

        current_token_index = 0
        while True:                
            if token_list[current_token_index] == "+":
                next_value = token_list.pop(current_token_index + 1)
                token_list.pop(current_token_index)
                previous_value = token_list.pop(current_token_index - 1)
                new_value = int(previous_value) + int(next_value)
                token_list.insert(current_token_index - 1, new_value)
            else:
                current_token_index += 1
            
            if current_token_index == len(token_list):
                break

        current_value = None
        current_operator = None
        for current_token_index, token in enumerate(token_list):
            if current_token_index == 0:
                current_value = int(token)
            elif token in ["+", "*"]:
                current_operator = token
            elif isinstance(token, int) or token.isnumeric():
                if current_operator == "+":
                    print(current_token_index, current_operator, current_value, token)
                    current_value += int(token)
                    print(current_token_index, current_value)
                elif current_operator == "*":
                    current_value *= int(token)

        return current_value, broke_at_index


    sum_of_answers_part_1 = 0
    sum_of_answers_part_2 =0
    for current_expression_index, expression in enumerate(expressions):
        expression_list = expression.replace("(", "( ").replace(")", " )").split(" ")        
        answer, _ = evaluate(expression_list)
        sum_of_answers_part_1 += answer

        answer, _ = evaluate2(expression_list)
        sum_of_answers_part_2 += answer        

    print("\n****************************************************")
    print("\nDay 18: Part 1")
    print("Answer: {}".format(sum_of_answers_part_1))

    print("\nDay 18: Part 2")
    print("Answer: {}".format(sum_of_answers_part_2))
    print("\n****************************************************")


if __name__ == '__main__':
    day18()