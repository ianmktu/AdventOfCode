import copy


def example():
    return [
        ".#.",
        "..#",
        "###",
    ]


def day17():
    cube_locations = [line.rstrip() for line in open('input.txt')]

    original_cube_map = {}
    for y, line in enumerate(cube_locations):
        for x, character in enumerate(line):
            if character == "#":
                if x not in original_cube_map:
                    original_cube_map[x] = {}
                if y not in original_cube_map[x]:
                    original_cube_map[x][y] = {}
                original_cube_map[x][y][0] = True


    def get_cube_active_count(x, y, z, current_cube_map):
        on_count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    else:
                        if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j]:
                            on_count += 1
        return on_count

    def get_coords_of_cubes_to_turn_on(x, y, z, current_cube_map):
        open_space_coord_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    else:
                        if x + i in current_cube_map \
                            and y + j in current_cube_map[x + i] \
                            and z + k in current_cube_map[x + i][y + j]:
                            continue
                        else:
                            open_space_coord_list.append((x + i, y + j, z + k))

        coords_to_turn_on_list = []
        for open_space_coords in open_space_coord_list:
            x_current = open_space_coords[0]
            y_current = open_space_coords[1]
            z_current = open_space_coords[2]
            active_count = get_cube_active_count(x_current, y_current, z_current, current_cube_map)
            if active_count == 3:
                coords_to_turn_on_list.append(open_space_coords)
        return coords_to_turn_on_list
            
    current_cube_map = copy.deepcopy(original_cube_map)
    for cycle_index in range(6):
        next_cube_map = {}
        for x, y_map in current_cube_map.items():
            for y, z_map in y_map.items():
                for z in z_map.keys():
                    active_count = get_cube_active_count(
                        x, y, z, current_cube_map
                    )
                    if active_count == 2 or active_count == 3:
                        if x not in next_cube_map:
                            next_cube_map[x] = {}
                        if y not in next_cube_map[x]:
                            next_cube_map[x][y] = {}
                        next_cube_map[x][y][z] = True

                    coords_of_cubes_to_turn_on = get_coords_of_cubes_to_turn_on(
                        x, y, z, current_cube_map
                    )
                    for coords in coords_of_cubes_to_turn_on:
                        x_coord = coords[0]
                        y_coord = coords[1]
                        z_coord = coords[2]
                        if x_coord not in next_cube_map:
                            next_cube_map[x_coord] = {}
                        if y_coord not in next_cube_map[x_coord]:
                            next_cube_map[x_coord][y_coord] = {}
                        next_cube_map[x_coord][y_coord][z_coord] = True

        current_cube_map = copy.deepcopy(next_cube_map)

    cube_count_3d = 0
    for y_map in current_cube_map.values():        
        for z_map in y_map.values():
            for z in z_map.values():
                cube_count_3d += 1


    original_cube_map_4d = {}
    for y, line in enumerate(cube_locations):
        for x, character in enumerate(line):
            if character == "#":
                if x not in original_cube_map_4d:
                    original_cube_map_4d[x] = {}
                if y not in original_cube_map_4d[x]:
                    original_cube_map_4d[x][y] = {}
                if 0 not in original_cube_map_4d[x][y]:
                    original_cube_map_4d[x][y][0] = {}
                original_cube_map_4d[x][y][0][0] = True

    def get_cube_active_count_4d(x, y, z, w, current_cube_map):
        on_count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        else:
                            if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j] \
                                and w + l in current_cube_map[x + i][y + j][z + k]:
                                on_count += 1
        return on_count

    def get_coords_of_cubes_to_turn_on_4d(x, y, z, w, current_cube_map):
        open_space_coord_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        else:
                            if x + i in current_cube_map \
                                and y + j in current_cube_map[x + i] \
                                and z + k in current_cube_map[x + i][y + j] \
                                and w + l in current_cube_map[x + i][y + j][z + k]:
                                continue
                            else:
                                open_space_coord_list.append((x + i, y + j, z + k, w + l))

        coords_to_turn_on_list = []
        for open_space_coords in open_space_coord_list:
            x_current = open_space_coords[0]
            y_current = open_space_coords[1]
            z_current = open_space_coords[2]
            w_current = open_space_coords[3]
            active_count = get_cube_active_count_4d(x_current, y_current, z_current, w_current, current_cube_map)
            if active_count == 3:
                coords_to_turn_on_list.append(open_space_coords)
        return coords_to_turn_on_list
            
    current_cube_map = copy.deepcopy(original_cube_map_4d)
    for cycle_index in range(6):
        next_cube_map = {}
        for x, y_map in current_cube_map.items():
            for y, z_map in y_map.items():
                for z, w_map in z_map.items():
                    for w in w_map.keys():
                        active_count = get_cube_active_count_4d(
                            x, y, z, w, current_cube_map
                        )
                        if active_count == 2 or active_count == 3:
                            if x not in next_cube_map:
                                next_cube_map[x] = {}
                            if y not in next_cube_map[x]:
                                next_cube_map[x][y] = {}
                            if z not in next_cube_map[x][y]:
                                next_cube_map[x][y][z] = {}
                            next_cube_map[x][y][z][w] = True

                        coords_of_cubes_to_turn_on = get_coords_of_cubes_to_turn_on_4d(
                            x, y, z, w, current_cube_map
                        )
                        for coords in coords_of_cubes_to_turn_on:
                            x_coord = coords[0]
                            y_coord = coords[1]
                            z_coord = coords[2]
                            w_coord = coords[3]
                            if x_coord not in next_cube_map:
                                next_cube_map[x_coord] = {}
                            if y_coord not in next_cube_map[x_coord]:
                                next_cube_map[x_coord][y_coord] = {}
                            if z_coord not in next_cube_map[x_coord][y_coord]:
                                next_cube_map[x_coord][y_coord][z_coord] = {}
                            next_cube_map[x_coord][y_coord][z_coord][w_coord] = True

        current_cube_map = copy.deepcopy(next_cube_map)

    cube_count_4d = 0
    for y_map in current_cube_map.values():        
        for z_map in y_map.values():
            for w_map in z_map.values():
                for w in w_map.values():
                    cube_count_4d += 1

    print("\n****************************************************")
    print("\nDay 17: Part 1")
    print("Answer: {}".format(cube_count_3d))

    print("\nDay 17: Part 2")
    print("Answer: {}".format(cube_count_4d))
    print("\n****************************************************")


if __name__ == '__main__':
    day17()
