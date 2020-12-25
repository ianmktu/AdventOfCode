def day25():
    public_keys = [line.rstrip() for line in open('input.txt')]
    card_public_key = int(public_keys[0])
    door_public_key = int(public_keys[1])
    
    loop_size = 20000000000
    subject_number = 7
    value = 1
    card_loop_size = 0
    door_loop_size = 0
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
        if value == card_public_key:
            card_loop_size = i+1
        if value == door_public_key:
            door_loop_size = i+1
        if card_loop_size > 0 and door_loop_size > 0:
            break
        
    subject_number = door_public_key
    encryption_key = 1
    for i in range(card_loop_size):
        encryption_key *= subject_number
        encryption_key %= 20201227
              
    print("\n****************************************************")
    print("\nDay 25")
    print("Answer: {}".format(encryption_key))


if __name__ == '__main__':
    day25()