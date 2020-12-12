def day12():
    directions = [line.rstrip() for line in open('input.txt')]
    north = 0
    east = 0
    current_heading = 90
    heading_list = ["N", "E", "S", "W"]
    heading_list_reversed = heading_list[::-1]
    for direction_string in directions:
        direction = direction_string[0]
        direction_value = int(direction_string[1:])
        if direction == "N":
            north += direction_value
        elif direction == "S":
            north -= direction_value
        elif direction == "E":
            east += direction_value
        elif direction == "W":
            east -= direction_value
        elif direction == "R":
            current_heading += direction_value
        elif direction == "L":
            current_heading -= direction_value
        elif direction == "F":
            absolute_heading_index = (current_heading % 360) // 90
            if absolute_heading_index < 0:
                absolute_heading = heading_list_reversed[absolute_heading_index]
            else:
                absolute_heading = heading_list[absolute_heading_index]
            if absolute_heading == "N":
                north += direction_value
            elif absolute_heading == "S":
                north -= direction_value
            elif absolute_heading == "E":
                east += direction_value
            elif absolute_heading == "W":
                east -= direction_value

    waypoint_north = 1
    waypoint_east = 10
    current_north = 0
    current_east = 0
    heading_list = ["N", "E", "S", "W"]
    heading_list_reversed = heading_list[::-1]
    for direction_string in directions:
        direction = direction_string[0]
        direction_value = int(direction_string[1:])
        if direction == "N":
            waypoint_north += direction_value
        elif direction == "S":
            waypoint_north -= direction_value
        elif direction == "E":
            waypoint_east += direction_value
        elif direction == "W":
            waypoint_east -= direction_value
        elif direction == "R":               
            new_waypoint_north = waypoint_north   
            new_waypoint_east = waypoint_east      

            if waypoint_east >= 0:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 1) % 4
                east_new_absolute_heading = heading_list[east_new_absolute_heading_index]
            else:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 3) % 4
                east_new_absolute_heading = heading_list[east_new_absolute_heading_index]
            
            if east_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_east)
            elif east_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_east)
            elif east_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_east)
            elif east_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_east)

            if waypoint_north >= 0:
                north_new_absolute_heading_index = (direction_value % 360) // 90
                north_new_absolute_heading = heading_list[north_new_absolute_heading_index]
            else:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 2) % 4
                north_new_absolute_heading = heading_list[north_new_absolute_heading_index]

            if north_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_north)
            elif north_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_north)
            elif north_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_north)
            elif north_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_north)
            
            waypoint_north = new_waypoint_north
            waypoint_east = new_waypoint_east            
        elif direction == "L":
            new_waypoint_north = waypoint_north   
            new_waypoint_east = waypoint_east      

            if waypoint_east >= 0:
                east_new_absolute_heading_index = (((direction_value % 360) // 90) + 2) % 4
                east_new_absolute_heading = heading_list_reversed[east_new_absolute_heading_index]
            else:
                east_new_absolute_heading_index = ((direction_value % 360) // 90)
                east_new_absolute_heading = heading_list_reversed[east_new_absolute_heading_index]
            if east_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_east)
            elif east_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_east)
            elif east_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_east)
            elif east_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_east)

            if waypoint_north >= 0:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 3) % 4
                north_new_absolute_heading = heading_list_reversed[north_new_absolute_heading_index]
            else:
                north_new_absolute_heading_index = (((direction_value % 360) // 90) + 1) % 4
                north_new_absolute_heading = heading_list_reversed[north_new_absolute_heading_index]

            if north_new_absolute_heading == "N":
                new_waypoint_north = abs(waypoint_north)
            elif north_new_absolute_heading == "S":
                new_waypoint_north = -1 * abs(waypoint_north)
            elif north_new_absolute_heading == "E":
                new_waypoint_east = abs(waypoint_north)
            elif north_new_absolute_heading == "W":
                new_waypoint_east = -1 * abs(waypoint_north)
            
            waypoint_north = new_waypoint_north
            waypoint_east = new_waypoint_east
        elif direction == "F":
            current_north += direction_value * waypoint_north
            current_east += direction_value * waypoint_east

    print("\n****************************************************")
    print("\nDay 12: Part 1")
    print("Answer: {}".format(abs(north) + abs(east)))

    print("\nDay 12: Part 2")
    print("Answer: {}".format(abs(current_north) + abs(current_east)))
    print("\n****************************************************")


if __name__ == '__main__':
    day12()