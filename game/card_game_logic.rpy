label card_game:
    init python:    
        import random
        from time import sleep

        def validate_card_selection(idx, cards, revealed):
            if idx < 0 or idx >= len(cards):
                renpy.say(None,"Invalid card index. Please try again.")
                return False
            if idx in revealed:
                renpy.say(None,"You cannot select a revealed card. Please try again.")
                return False
            return True

        def reveal_card(idx, cards, revealed):
            
            renpy.say(None,"Revealed the card %s at index %i."%(cards[idx],idx+1))
            revealed[idx] = cards[idx]

        def unreveal_card(idx, cards, revealed):
            del revealed[idx]

        def check_match(idx1, idx2, cards, revealed):
            if cards[idx1] == cards[idx2]:
                renpy.say(None,"Found a match! Revealed both cards %s."%(cards[idx1]))
                return True
            else:
                renpy.say(None,"\nNo match found. Switching turns.")
                unreveal_card(idx1, cards, revealed)
                unreveal_card(idx2, cards, revealed)
                return False

        def enemy_turn(revealed, cards):
            
            renpy.say(None, "Navi's turn!")
            unrevealed_cards = [idx for idx in range(len(cards)) if idx not in revealed]
            
            idx1 = random.choice(unrevealed_cards)
            reveal_card(idx1, cards, revealed)
            
            idx2 = random.choice([idx for idx in unrevealed_cards if idx != idx1 and cards[idx] != cards[idx1]])
            reveal_card(idx2, cards, revealed)
            
            renpy.say(None,"No match found. Switching turns.")
            
            unreveal_card(idx1, cards, revealed)
            unreveal_card(idx2, cards, revealed)

        def good_end():
            renpy.say(None,"Majority of pairs matched. Triggering good ending (:")

        def bad_end():
            renpy.say(None,"Four turns passed with zero pairs uncovered. Triggering bad ending ):")

        def select_card(cards, revealed, cardnum):

            while True:
                if(cardnum==1):
                    renpy.say(None,"Select the first card index.")
                else:
                    renpy.say(None,"Select the second card index.")
                user_input =  renpy.input("Enter a card index between 1 and 10:",length=32)
                

                try:
                    idx = int(user_input) - 1
                except ValueError:
                    renpy.say(None,"Invalid input. Please try again.")
                    continue

                if not validate_card_selection(idx, cards, revealed):
                    continue
                else:
                    reveal_card(idx, cards, revealed)    
                    return idx

        def handle_selected_pair(idx1, idx2, cards, revealed, turns):
            if check_match(idx1, idx2, cards, revealed):
                if len(revealed) > len(cards)/2 and len(revealed) % 2 == 0:
                    good_end()
                    return False
            else:
                if turns >= 4 and len(revealed) == 0:
                    bad_end()
                    return False      
                
            return True

        def main():
            
            renpy.say(None,"Beginning the card game!")
            cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E']
            #random.shuffle(cards)
            revealed = {}
            turns = 0
            run_game=True

            # Game loop
            while run_game:
                renpy.say(None,"Flayon's turn!")
                out=""
                i=0
                for i, card in enumerate(cards):
                    if i in revealed:
                        out+=" "+cards[i]   
                    else:
                        out+=' ?'
                renpy.say(None,"Cards: %s"%(out))
                renpy.say(None,"This is your turn number %i."%(turns))

                idx1 = select_card(cards, revealed, 1)
                
                idx2 = select_card(cards, revealed, 2)
                
                turns += 1
                run_game = handle_selected_pair(idx1, idx2, cards, revealed, turns)
                
                if(run_game):
                    enemy_turn(revealed, cards)

    python:
            main()
    "it works"