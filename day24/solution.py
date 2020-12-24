import copy

def day24():
    tile_strings = [line.rstrip() for line in open('input.txt')]

    tile_directions = []
    for line in tile_strings:
        directions = []
        line_index = 0        
        while line_index < len(line):
            if line[line_index] == "s":
                line_index += 1
                if line[line_index] == "e":
                    directions.append("se")
                else:
                    directions.append("sw")
                line_index += 1
            elif line[line_index] == "n":
                line_index += 1
                if line[line_index] == "e":
                    directions.append("ne")
                else:
                    directions.append("nw")
                line_index += 1
            elif line[line_index] == "e":
                directions.append("e")
                line_index += 1
            elif line[line_index] == "w":
                directions.append("w")
                line_index += 1
        tile_directions.append(directions)
            

    def get_new_direction_key(current_coord_string, direction_string):
        current_coords = [int(i) for i in current_coord_string.split(",")]
        if direction_string == 'e':
            current_coords[0] += 1
            current_coords[1] += -1
            current_coords[2] += 0
        elif direction_string == 'se':
            current_coords[0] += 0
            current_coords[1] += -1
            current_coords[2] += 1
        elif direction_string == 'sw':
            current_coords[0] += -1
            current_coords[1] += 0
            current_coords[2] += 1
        elif direction_string == 'w':
            current_coords[0] += -1
            current_coords[1] += 1
            current_coords[2] += 0
        elif direction_string == 'nw':
            current_coords[0] += 0
            current_coords[1] += 1
            current_coords[2] += -1
        elif direction_string == 'ne':
            current_coords[0] += 1
            current_coords[1] += 0
            current_coords[2] += -1
        return (",").join([str(i) for i in current_coords])


    def get_other_white_tiles_to_flip(white_tile_coord_string_list, current_tile_map):
        flip_tiles = []
        for white_tile_coord_string in white_tile_coord_string_list:
            black_tile_count = 0
            for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
                current_coord_string = get_new_direction_key(white_tile_coord_string, direction)
                if current_coord_string in current_tile_map:
                    black_tile_count += 1
            if black_tile_count == 2:
                flip_tiles.append(white_tile_coord_string)
        return flip_tiles

    tile_map = {}
    for direction_list in tile_directions: 
        current_tile_key = '0,0,0'
        for index, direction in enumerate(direction_list):
            new_tile_key = get_new_direction_key(current_tile_key, direction)

            current_tile_key = new_tile_key
            if index == len(direction_list) - 1:   
                if new_tile_key not in tile_map:
                    tile_map[current_tile_key] = True
                else:
                    del tile_map[current_tile_key]

    current_tile_map = copy.deepcopy(tile_map)

    for i in range(100):
        new_tile_map = {}
        for tile_key in current_tile_map.keys():               
            adjacent_white_tile_keys = []
            for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
                current_coord_string = get_new_direction_key(tile_key, direction)
                if current_coord_string not in current_tile_map:
                    adjacent_white_tile_keys.append(current_coord_string)
            if len(adjacent_white_tile_keys) == 5 or len(adjacent_white_tile_keys) == 4:
                new_tile_map[tile_key] = True
            white_tiles_to_flip = get_other_white_tiles_to_flip(adjacent_white_tile_keys, 
                                                                current_tile_map)
            for white_tile_to_flip in white_tiles_to_flip:
                new_tile_map[white_tile_to_flip] = True

        current_tile_map = copy.deepcopy(new_tile_map)

    print("\n****************************************************")
    print("\nDay 24: Part 1")
    print("Answer: {}".format(len(tile_map)))

    print("\nDay 24: Part 2")
    print("Answer: {}".format(len(current_tile_map)))
    print("\n****************************************************")


if __name__ == '__main__':
    day24()