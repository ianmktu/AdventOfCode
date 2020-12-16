def day15():
    game = [0,1,4,13,15,12,16]
          
    result = []
    for i in [2020, 30000000]:
        game_dict = {}
        for index, num in enumerate(game):
            game_dict[num] = index
        start_index = len(game)  
        previous_value = game[-1]

        for index in range(start_index, i):      
            if previous_value in game_dict:
                new_value = index - 1 - game_dict[previous_value]   
                game_dict[previous_value] = index - 1
                previous_value = new_value
            else:
                game_dict[previous_value] = index - 1
                previous_value = 0
                        
        result.append(previous_value)
    
    print("\n****************************************************")
    print("\nDay 15: Part 1")
    print("Answer: {}".format(result[0]))

    print("\nDay 15: Part 2")
    print("Answer: {}".format(result[1]))
    print("\n****************************************************")


if __name__ == '__main__':
    day15()