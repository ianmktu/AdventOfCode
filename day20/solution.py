import numpy as np
import copy 
import itertools

def day20():
    tile_strings = [line.rstrip() for line in open('input.txt')]

    tiles = {}
    current_id = -1
    current_tile = np.zeros((10,10), dtype=int)
    row_idx = 0
    for index, line in enumerate(tile_strings):
        if "Tile" in line:   
            if index > 0:      
                tiles[current_id] = current_tile
            current_tile = np.zeros((10,10), dtype=int)
            current_id = int(line.split(" ")[1][:-1])
            row_idx = 0
            continue

        if "" == line:  
            continue

        for col_idx, character in enumerate(line):
            if character == ".":      
                current_tile[row_idx, col_idx] = 0
            else:
                current_tile[row_idx, col_idx] = 1
            
        row_idx += 1

    tiles[current_id] = current_tile

    tile_to_side_info_map = {}
    for current_id, tile in tiles.items():
        tile_to_side_info_map[current_id] = {}

        tile_to_side_info_map[current_id]['top bottom'] = {}
        tile_to_side_info_map[current_id]['top bottom']['main side'] = "".join(list(str(i) for i in tile[0, :]))
        tile_to_side_info_map[current_id]['top bottom']['main side matches'] = set()
        tile_to_side_info_map[current_id]['top bottom']['opposite side'] = "".join(list(str(i) for i in tile[-1, :]))
        tile_to_side_info_map[current_id]['top bottom']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['top bottom reversed'] = {}
        tile_to_side_info_map[current_id]['top bottom reversed']['main side'] = "".join(list(str(i) for i in np.flip(tile[0, :])))
        tile_to_side_info_map[current_id]['top bottom reversed']['main side matches'] = set()
        tile_to_side_info_map[current_id]['top bottom reversed']['opposite side'] = "".join(list(str(i) for i in np.flip(tile[-1, :])))
        tile_to_side_info_map[current_id]['top bottom reversed']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['left right'] = {}
        tile_to_side_info_map[current_id]['left right']['main side'] = "".join(list(str(i) for i in tile[:, 0]))
        tile_to_side_info_map[current_id]['left right']['main side matches'] = set()
        tile_to_side_info_map[current_id]['left right']['opposite side'] = "".join(list(str(i) for i in tile[:, -1]))
        tile_to_side_info_map[current_id]['left right']['opposite side matches'] = set()

        tile_to_side_info_map[current_id]['left right reversed'] = {}
        tile_to_side_info_map[current_id]['left right reversed']['main side'] = "".join(list(str(i) for i in np.flip(tile[:, 0])))
        tile_to_side_info_map[current_id]['left right reversed']['main side matches'] = set()
        tile_to_side_info_map[current_id]['left right reversed']['opposite side'] = "".join(list(str(i) for i in np.flip(tile[:, -1])))
        tile_to_side_info_map[current_id]['left right reversed']['opposite side matches'] = set()


    compared_ids = set()
    for current_id1, tile1 in tiles.items():
        for current_id2, tile2 in tiles.items():
            if current_id1 == current_id2:
                continue
            if (current_id1, current_id2) in compared_ids or \
                (current_id2, current_id1) in compared_ids:
                continue

            for side1, side1_to_info_map in tile_to_side_info_map[current_id1].items():
                for side2, side2_to_info_map in tile_to_side_info_map[current_id2].items():
                    if side1_to_info_map['main side'] == side2_to_info_map['main side']:
                        side1_to_info_map['main side matches'].add(current_id2)
                        side2_to_info_map['main side matches'].add(current_id1)

                    if side1_to_info_map['opposite side'] == side2_to_info_map['opposite side']:
                        side1_to_info_map['opposite side matches'].add(current_id2)
                        side2_to_info_map['opposite side matches'].add(current_id1)

                    if side1_to_info_map['main side'] == side2_to_info_map['opposite side']:
                        side1_to_info_map['main side matches'].add(current_id2)
                        side2_to_info_map['opposite side matches'].add(current_id1)

                    if side1_to_info_map['opposite side'] == side2_to_info_map['main side']:
                        side1_to_info_map['opposite side matches'].add(current_id2)
                        side2_to_info_map['main side matches'].add(current_id1)

            compared_ids.update([(current_id1, current_id2), (current_id2, current_id1)])

    corner_ids = []
    for current_id, side_info_map in tile_to_side_info_map.items():
        is_corner = True
        for side_name, info_map in side_info_map.items():
            if len(info_map['main side matches'] | info_map['opposite side matches']) > 1:
                is_corner = False
                break                
        if is_corner:
            corner_ids.append(current_id)
            

    def matches(side_string, tile_id, tile_to_side_info_map):
        for side2, side2_to_info_map in tile_to_side_info_map[tile_id].items():
            if side_string == side2_to_info_map['main side']:
                return True
            if side_string == side2_to_info_map['opposite side']:
                return True        
        return False

    def get_sides(tile):
        top = "".join(list(str(i) for i in tile[0, :]))
        bottom = "".join(list(str(i) for i in tile[-1, :]))
        left = "".join(list(str(i) for i in tile[:, 0]))
        right = "".join(list(str(i) for i in tile[:, -1]))
        return {"top": top, "right":right, "bottom":bottom, "left":left}

    def get_connected_ids(tile_id, tile_to_side_info_map):
        side_to_info_map = tile_to_side_info_map[tile_id]
        set_list = set()
        for side_name, info_map in side_to_info_map.items():
            set_list.update(info_map['main side matches'])
            set_list.update(info_map['opposite side matches'])
        return set_list

    def rotate_flip(tile, transform_id):
        if transform_id == 0:
            return np.rot90(tile, k=1, axes=(1,0))
        elif transform_id == 1:
            return np.rot90(tile, k=2, axes=(1,0))        
        elif transform_id == 2:
            return np.rot90(tile, k=3, axes=(1,0))        
        elif transform_id == 3:
            return np.fliplr(tile)        
        elif transform_id == 4:
            return np.rot90(np.fliplr(tile), k=1, axes=(1,0))
        elif transform_id == 5:
            return np.rot90(np.fliplr(tile), k=2, axes=(1,0))        
        elif transform_id == 6:
            return np.rot90(np.fliplr(tile), k=3, axes=(1,0))        
        else:
            return tile

    def get_corner(
        corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='right', 
        connected_side2='bottom'):
        for i in range(8):
            correct_orientation = False
            current_tile = rotate_flip(
                tile=tiles[corner_id], 
                transform_id=i
            )        
            tile_sides = get_sides(tile=current_tile)

            connected_ids = get_connected_ids(
                tile_id=corner_id, 
                tile_to_side_info_map=tile_to_side_info_map
            )
            connected_ids_permutations = list(itertools.permutations(connected_ids))
            for connected_ids_permutation in connected_ids_permutations:
                connected_side_id1 = connected_ids_permutation[0]
                connected_side_id2 = connected_ids_permutation[1]
                if matches(tile_sides[connected_side1], connected_side_id1, tile_to_side_info_map) and \
                    matches(tile_sides[connected_side2], connected_side_id2, tile_to_side_info_map):
                    correct_orientation = True
                    break
            if correct_orientation:
                return current_tile, connected_side_id1, connected_side_id2
        return None, None, None 

    def get_general_tile(
        tile_id, 
        tiles,
        tile_to_side_info_map, 
        correct_side='left',
        correct_side_string=None,
        connected_side='right'):        
        for i in range(8):
            correct_orientation = False
            current_tile = rotate_flip(
                tile=tiles[tile_id], 
                transform_id=i
            )        
            tile_sides = get_sides(tile=current_tile)
            if tile_sides[correct_side] == correct_side_string:            
                correct_orientation = True        
                connected_ids = get_connected_ids(
                    tile_id=tile_id, 
                    tile_to_side_info_map=tile_to_side_info_map
                )
                side_to_id_map = {}
                for side, side_string in tile_sides.items():
                    for connected_tile_id in connected_ids:
                        if matches(side_string, connected_tile_id, tile_to_side_info_map):
                            side_to_id_map[side] = connected_tile_id
 
            if correct_orientation:
                return current_tile, side_to_id_map
        return None, None

    side_length = int(np.sqrt(len(tiles)))
    tile_id_location = np.full((side_length, side_length), -1, dtype=int)
    final_tiles = {}

    top_left_corner_id = corner_ids[0]
    top_left_corner_tile, right_side_id, bottom_side_id = get_corner(
        top_left_corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='right', 
        connected_side2='bottom'
    )

    final_tiles[top_left_corner_id] = top_left_corner_tile
    tile_id_location[0,0] = top_left_corner_id
    tile_id_location[0,1] = right_side_id
    tile_id_location[1,0] = bottom_side_id

    for i in range(1, side_length-1):
        tile_id = tile_id_location[0, i]
        current_tile, side_to_id_map = get_general_tile(
            tile_id, 
            tiles,
            tile_to_side_info_map, 
            correct_side='left',
            correct_side_string=get_sides(final_tiles[tile_id_location[0, i-1]])['right'],
            connected_side='right'
        )
        final_tiles[tile_id] = current_tile
        tile_id_location[0, i+1] = side_to_id_map['right']
        tile_id_location[1, i] = side_to_id_map['bottom']

    top_right_corner_id = tile_id_location[0, -1]
    top_right_corner_tile, left_side_id, bottom_side_id = get_corner(
        top_right_corner_id, 
        tiles,
        tile_to_side_info_map, 
        connected_side1='left', 
        connected_side2='bottom'
    )

    final_tiles[top_right_corner_id] = top_right_corner_tile
    tile_id_location[1,-1] = bottom_side_id

    for j in range(1,side_length):
        for i in range(0, side_length):
            tile_id = tile_id_location[j, i]
            current_tile, side_to_id_map = get_general_tile(
                tile_id, 
                tiles,
                tile_to_side_info_map, 
                correct_side='top',
                correct_side_string=get_sides(final_tiles[tile_id_location[j-1, i]])['bottom'],
                connected_side='right' if i < side_length - 1 else 'left'
            )
            final_tiles[tile_id] = current_tile
            if j+1 < side_length:
                tile_id_location[j+1, i] = side_to_id_map['bottom']


    # For some reason it needs a transform to match the example
    # This puzzle was a pain, so I'm just going to keep this here as it works
    for current_id, tile in final_tiles.items():
        final_tiles[current_id] = rotate_flip(
            tile=tile[1:-1,1:-1], 
            transform_id=6
        )       

    rows = []
    for j in range(side_length):
        row = []
        for i in range(side_length):
            row.append(final_tiles[tile_id_location[j,i]])
        rows.append(np.concatenate(row, axis=0))
    final_image = np.concatenate(rows, axis=1)

    sea_monster = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]
    ]
    sea_monster = np.array(sea_monster)

    rough_count = []
    for transform_id in range(8):
        current_image = rotate_flip(
            tile=copy.deepcopy(final_image), 
            transform_id=transform_id
        )        

        resulting_image = copy.deepcopy(current_image)
        found_monsters = 0
        for j in range(current_image.shape[0] - sea_monster.shape[0]):
            for i in range(current_image.shape[1] - sea_monster.shape[1]): 
                count = 0           
                for sea_y in range(sea_monster.shape[0]):
                    for sea_x in range(sea_monster.shape[1]):
                        count += current_image[j+sea_y,i+sea_x] * sea_monster[sea_y, sea_x]
                if count == np.sum(sea_monster).astype(int):
                    found_monsters += 1
                    for sea_y in range(sea_monster.shape[0]):
                        for sea_x in range(sea_monster.shape[1]):
                            if sea_monster[sea_y, sea_x] == 1:
                                resulting_image[j+sea_y,i+sea_x] = 0
        if found_monsters > 0:
            rough_count.append(np.sum(resulting_image))    

    print("\n****************************************************")
    print("\nDay 20: Part 1")
    print("Answer: {}".format(np.prod(corner_ids, dtype=np.uint64)))

    print("\nDay 20: Part 2")
    print("Answer: {}".format(max(rough_count)))
    print("\n****************************************************")


if __name__ == '__main__':
    day20()