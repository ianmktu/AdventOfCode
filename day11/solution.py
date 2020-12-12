import copy

def day11():
    seating_rows = [line.rstrip() for line in open('input.txt')]

    seating_array = []
    for index, row in enumerate(seating_rows):
        seating_array.append([])
        for seat in row:
            seating_array[index].append(seat)
    seating_array_original = copy.deepcopy(seating_array)

    while True:
        previous_seating_array = copy.deepcopy(seating_array)
        for row_index, row in enumerate(previous_seating_array):                       
            for col_index, seat in enumerate(row):           
                occupied_count = 0
                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index - 1][col_index - 1] == "#":
                        occupied_count += 1

                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index < len(row) and \
                    previous_seating_array[row_index - 1][col_index] == "#":
                        occupied_count += 1

                if 0 <= row_index - 1 < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index - 1][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index + 1 < len(row) and \
                    previous_seating_array[row_index + 1][col_index + 1] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index < len(row) and \
                    previous_seating_array[row_index + 1][col_index] == "#":
                        occupied_count += 1

                if 0 <= row_index + 1 < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index + 1][col_index - 1] == "#":
                        occupied_count += 1

                if 0 <= row_index < len(seating_array) and 0 <= col_index - 1 < len(row) and \
                    previous_seating_array[row_index][col_index - 1] == "#":
                        occupied_count += 1

                if seat == "#" and occupied_count >= 4:
                    seating_array[row_index][col_index] = "L"
                elif seat == "L" and occupied_count == 0:
                    seating_array[row_index][col_index] = "#"
            
        stable = True
        final_occupied_count = 0
        for row_index in range(len(seating_array)):            
            for col_index in range(len(seating_array[row_index])):
                if seating_array[row_index][col_index] != previous_seating_array[row_index][col_index]:
                    stable = False
                    break                
                if seating_array[row_index][col_index] == "#":
                    final_occupied_count += 1
            if not stable:
                break

        if stable:
            break

    seating_array = copy.deepcopy(seating_array_original)
    while True:
        previous_seating_array = copy.deepcopy(seating_array)
        for row_index, row in enumerate(previous_seating_array):                       
            for col_index, seat in enumerate(row):           
                occupied_count = 0
                
                def is_occupied(y_dir, x_dir):
                    seeing_step = 1
                    while 0 <= row_index + y_dir * seeing_step < len(seating_array) and 0 <= col_index + x_dir * seeing_step < len(row):
                        if previous_seating_array[row_index + y_dir * seeing_step][col_index + x_dir * seeing_step] == "#":                            
                            return True
                        elif previous_seating_array[row_index + y_dir * seeing_step][col_index + x_dir * seeing_step] == "L":
                            return False
                        else:
                            seeing_step += 1
                    return False

                if is_occupied(y_dir=-1, x_dir=-1):
                    occupied_count += 1

                if is_occupied(y_dir=-1, x_dir=0):
                    occupied_count += 1

                if is_occupied(y_dir=-1, x_dir=1):
                    occupied_count += 1
                
                if is_occupied(y_dir=0, x_dir=1):
                    occupied_count += 1

                if is_occupied(y_dir=1, x_dir=1):
                    occupied_count += 1
                
                if is_occupied(y_dir=1, x_dir=0):
                    occupied_count += 1

                if is_occupied(y_dir=1, x_dir=-1):
                    occupied_count += 1

                if is_occupied(y_dir=0, x_dir=-1):
                    occupied_count += 1

                if seat == "#" and occupied_count >= 5:
                    seating_array[row_index][col_index] = "L"
                elif seat == "L" and occupied_count == 0:
                    seating_array[row_index][col_index] = "#"
            
        stable = True
        final_occupied_count_2 = 0
        for row_index in range(len(seating_array)):            
            for col_index in range(len(seating_array[row_index])):
                if seating_array[row_index][col_index] != previous_seating_array[row_index][col_index]:
                    stable = False
                    break                
                if seating_array[row_index][col_index] == "#":
                    final_occupied_count_2 += 1
            if not stable:
                break

        if stable:
            break

    print("\n****************************************************")
    print("\nDay 11: Part 1")
    print("Answer: {}".format(final_occupied_count))

    print("\nDay 11: Part 2")
    print("Answer: {}".format(final_occupied_count_2))
    print("\n****************************************************")


if __name__ == '__main__':
    day11()