def day15():
    game = [0,1,4,13,15,12,16]
    
    game_dict = {}
    for index, num in enumerate(game):
        game_dict[num] = [index, -1]

    index = len(game)
    previous_value = game[-1]
    while True:        
        if index % 10000 == 0:
            print()
            print(index)
        if previous_value in game_dict and game_dict[previous_value][1] != -1:
            new_value = game_dict[previous_value][1] - game_dict[previous_value][0]
            if new_value not in game_dict:
                game_dict[new_value] = [index, -1]
            else:
                if game_dict[new_value][1] == -1:
                    game_dict[new_value][1] = index
                else:
                    game_dict[new_value][0] = game_dict[new_value][1]
                    game_dict[new_value][1] = index 
            previous_value = new_value
        else:
            if game_dict[0][1] == -1:
                game_dict[0][1] = index
            else:
                game_dict[0][0] = game_dict[0][1]
                game_dict[0][1] = index
            previous_value = 0
                     
        if index == 2020 - 1:
            part1 = previous_value
        elif index == 30000000 - 1:
            part2 = previous_value
            break
        
        index += 1


    print("\n****************************************************")
    print("\nDay 15: Part 1")
    print("Answer: {}".format(part1))

    print("\nDay 15: Part 2")
    print("Answer: {}".format(part2))
    print("\n****************************************************")


if __name__ == '__main__':
    day15()