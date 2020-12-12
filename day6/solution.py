def day6():
    customs = [line.rstrip() for line in open('input.txt')]

    current_group = {}
    current_person_count = 0
    answer_count = []
    consensus_count = []
    for index, line in enumerate(customs):
        if line == "":            
            answer_count.append(len(current_group))

            current_consensus_count = 0
            for key, value in current_group.items():
                if value == current_person_count:
                    current_consensus_count += 1            
            consensus_count.append(current_consensus_count)

            current_group.clear()
            current_person_count = 0
        else:
            current_person_count += 1
            for char in line.strip():
                if char == " ":
                    continue
                if char in current_group:
                    current_group[char] += 1
                else:
                    current_group[char] = 1

        if index == len(customs) - 1:
            answer_count.append(len(current_group))

            current_consensus_count = 0
            for key, value in current_group.items():
                if value == current_person_count:
                    current_consensus_count += 1            
            consensus_count.append(current_consensus_count)

            current_group.clear()
            current_person_count = 0

    print("\n****************************************************")
    print("\nDay 6: Part 1")
    print("Answer Count: {}".format(sum(answer_count)))

    print("\nDay 6: Part 2")
    print("Consensus Count: {}".format(sum(consensus_count)))
    print("\n****************************************************")


if __name__ == '__main__':
    day6()