def day5():
    seat_strings = [line.rstrip() for line in open('input.txt')]

    seat_ids = []
    for seat_string in seat_strings:
        start_row = 0
        end_row = 127

        for index, char in enumerate(seat_string[:7]):
            mid_point = int((start_row + end_row) / 2)
            if char == 'F':
                end_row = mid_point
            else:
                start_row = mid_point + 1

        row_id = -1
        if seat_string[6] == 'F':
            row_id = start_row
        else:
            row_id = end_row

        start_col = 0
        end_col = 7
        for index, char in enumerate(seat_string[7:-1]):
            mid_point = int((start_col + end_col) / 2)
            if char == 'L':
                end_col = mid_point
            else:
                start_col = mid_point + 1

        col_id = -1
        if seat_string[-1] == 'L':
            col_id = start_col
        else:
            col_id = end_col

        seat_id = row_id * 8 + col_id
        seat_ids.append(seat_id)

    seat_ids.sort()

    print("\n****************************************************")
    print("\nDay 5: Part 1")
    print("Total Seat IDs: {}".format(len(seat_strings)))
    print("Max Seat ID: {}".format(seat_ids[-1]))
    print("\nDay 5: Part 2")

    all_ids = set([i for i in range(seat_ids[0], seat_ids[-1] + 1)])
    missing_seat_ids = all_ids - set(seat_ids)
    for i, missing_seat_id in enumerate(missing_seat_ids):
        print("Missing Seat ID: {}".format(seat_id))

    print("\n****************************************************")

if __name__ == '__main__':
    day5()