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
                if( len(revealed) == 0):
                    renpy.say(FLAY,"Yes! One win for me!")
                    renpy.say(NAVI,"Simple beginner’s luck.{p}Don’t get overconfident over a single win.")
                elif (len(revealed)==2):
                    
                    renpy.say(FLAY,"Another victory!")
                    renpy.say(NAVI, "Oh, please.{p}I’ll be sorely disappointed if this is enough to give you a big head")
                    renpy.say(FLAY,"(Says the person who never lets go of a single win.)")
                elif(len(revealed)==4):
                    renpy.say(FLAY,"Oh hey, would you look at that.")
                    renpy.say(NAVI,"...")
                    renpy.say(FLAY,"If I’m doing my math correctly, there’s not enough pairs left for you to still win.")
                    renpy.say(NAVI,"...")
                    renpy.say(FLAY,"What?{p}Roon got your tongue?")
                return True
            else:
                renpy.say(None,"\nNo match found. Switching turns.")
                renpy.say(FLAY,"No! That’s the wrong pair!")
                renpy.say(NAVI,"Ohoho! All talk, are we?")
                unreveal_card(idx1, cards, revealed)
                unreveal_card(idx2, cards, revealed)
                return False

        def enemy_turn(revealed, cards):
            
            renpy.say(None, "Navi's turn!")
            renpy.say(NAVI,"Hmph.{p}Nothing for you to get worked up about.{p}My time will come.")
            renpy.say(FLAY,"Sounds like something a loser would say.")
            renpy.say(NAVI,"Why, you—!")
            unrevealed_cards = [idx for idx in range(len(cards)) if idx not in revealed]
            
            idx1 = random.choice(unrevealed_cards)
            reveal_card(idx1, cards, revealed)
            
            idx2 = random.choice([idx for idx in unrevealed_cards if idx != idx1 and cards[idx] != cards[idx1]])
            reveal_card(idx2, cards, revealed)

            renpy.say(None,"No match found. Switching turns.")
            
            unreveal_card(idx1, cards, revealed)
            unreveal_card(idx2, cards, revealed)

        def good_end():
            renpy.jump("good_end")

        def bad_end():
            renpy.say(None,"Four turns passed with zero pairs uncovered. Triggering bad ending ):")
            renpy.jump("bad_end")

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
                if turns >= 4  and len(revealed) == 0: 
                    bad_end()
                    return False      
                
            return True

        def main():
            
            renpy.say(None,"Beginning the card game!")
            cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E']
            random.shuffle(cards)

            revealed = {}
            turns = 0
            run_game=True
            renpy.say(NAVI,"Whoever matches the most pairs wins. Easy, yes?")
            renpy.say(FLAY,"Getting a little cocky, aren’t you?{p}Sure you don’t want to make it best of three?{p}Might actually give you a winning chance if you do.")
            renpy.say(NAVI,"Hah! Bold of you to assume I need more than one round to defeat you!")
            renpy.say(NAVI,"I’ll even be generous and let you go first.{p}Do your worst, Machina!")

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