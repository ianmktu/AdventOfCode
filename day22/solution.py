import copy 

def day22():
    crab_game = [line.rstrip() for line in open('input.txt')]
    current_player = ""
    current_deck = []
    decks = {}
    for line in crab_game:
        if "Player" in line:
            if current_player != "":
                decks[current_player] = current_deck
                current_deck = []
            current_player = line.split(":")[0]
            continue
        if line == "":
            continue
        current_deck.append(int(line))
    decks[current_player] = current_deck
    decks_original = copy.deepcopy(decks)

    round_no = 0
    winning_deck = []
    while True:       
        round_no += 1 

        card1 = decks['Player 1'][0]
        card2 = decks['Player 2'][0]
 
        if card1 > card2:
            decks['Player 1'] = decks['Player 1'][1:] + [card1, card2]
            decks['Player 2'] = decks['Player 2'][1:]
        else:
            decks['Player 1'] = decks['Player 1'][1:]
            decks['Player 2'] = decks['Player 2'][1:] + [card2, card1]


        if len(decks['Player 1']) == 0:
            winning_deck = decks['Player 2']
            break        
        
        if len(decks['Player 2']) == 0:
            winning_deck = decks['Player 1']
            break

    score_normal = 0
    for index, value in enumerate(winning_deck):
        score_normal += (len(winning_deck) - index) * value

    decks = copy.deepcopy(decks_original)

    round_no = 0
    winning_deck = []
    while True:       
        round_no += 1

        card1 = decks['Player 1'][0]
        card2 = decks['Player 2'][0]
 
        if card1 <= len(decks['Player 1'][1:]) and card2 <= len(decks['Player 2'][1:]):
            def recursive_game_outcome(deck1, deck2):
                deck1 = copy.deepcopy(deck1)
                deck2 = copy.deepcopy(deck2)
                save_states = set()
                save_states.add((tuple(deck1), tuple(deck2)))

                while True:  
                    card1 = deck1[0]
                    card2 = deck2[0]
                    
                    if card1 <= len(deck1[1:]) and card2 <= len(deck2[1:]):
                        if recursive_game_outcome(deck1=deck1[1:1+card1], 
                                                  deck2=deck2[1:1+card2]):                            
                            deck1 = deck1[1:] + [card1, card2]
                            deck2 = deck2[1:]
                        else:                            
                            deck2 = deck2[1:] + [card2, card1]
                            deck1 = deck1[1:]
                    elif card1 > card2:
                        deck1 = deck1[1:] + [card1, card2]
                        deck2 = deck2[1:]
                    else:
                        deck1 = deck1[1:]
                        deck2 = deck2[1:] + [card2, card1]

                    if (tuple(deck1), tuple(deck2)) in save_states:
                        return True
                    else:
                        save_states.add((tuple(deck1), tuple(deck2)))

                    if len(deck1) == 0:
                        return False                                
                    
                    if len(deck2) == 0:
                        return True
                
            if recursive_game_outcome(deck1=decks['Player 1'][1:1+card1], 
                                      deck2=decks['Player 2'][1:1+card2]):
                decks['Player 1'] = decks['Player 1'][1:] + [card1, card2]
                decks['Player 2'] = decks['Player 2'][1:]
            else:
                decks['Player 2'] = decks['Player 2'][1:] + [card2, card1]
                decks['Player 1'] = decks['Player 1'][1:]

        elif card1 > card2:
            decks['Player 1'] = decks['Player 1'][1:] + [card1, card2]
            decks['Player 2'] = decks['Player 2'][1:]
        else:
            decks['Player 1'] = decks['Player 1'][1:]
            decks['Player 2'] = decks['Player 2'][1:] + [card2, card1]

        if len(decks['Player 1']) == 0:
            winning_deck = decks['Player 2']
            break        
        
        if len(decks['Player 2']) == 0:
            winning_deck = decks['Player 1']
            break

    score_recursive = 0
    for index, value in enumerate(winning_deck):
        score_recursive += (len(winning_deck) - index) * value

    print("\n****************************************************")
    print("\nDay 22: Part 1")
    print("Answer: {}".format(score_normal))

    print("\nDay 22: Part 2")
    print("Answer: {}".format(score_recursive))
    print("\n****************************************************")


if __name__ == '__main__':
    day22()