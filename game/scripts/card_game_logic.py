import random
from time import sleep

def validate_card_selection(idx, cards, revealed):
    if idx < 0 or idx >= len(cards):
        print("\nInvalid card index. Please try again.")
        return False
    if idx in revealed:
        print("\nYou cannot select a revealed card. Please try again.")
        return False
    return True

def reveal_card(idx, cards, revealed):
    sleep(0.25)
    print(f"\nRevealed the card {cards[idx]} at index {idx+1}.")
    revealed[idx] = cards[idx]

def unreveal_card(idx, cards, revealed):
    del revealed[idx]

def check_match(idx1, idx2, cards, revealed):
    if cards[idx1] == cards[idx2]:
        print(f"\nFound a match! Revealed both cards {cards[idx1]}.")
        return True
    else:
        print("\nNo match found. Switching turns.")
        unreveal_card(idx1, cards, revealed)
        unreveal_card(idx2, cards, revealed)
        return False

def enemy_turn(revealed, cards):
    sleep(0.5)
    print("\nNavi's turn!")
    unrevealed_cards = [idx for idx in range(len(cards)) if idx not in revealed]
    
    idx1 = random.choice(unrevealed_cards)
    reveal_card(idx1, cards, revealed)
    
    idx2 = random.choice([idx for idx in unrevealed_cards if idx != idx1 and cards[idx] != cards[idx1]])
    reveal_card(idx2, cards, revealed)
    
    print("\nNo match found. Switching turns.")
    sleep(0.5)
    unreveal_card(idx1, cards, revealed)
    unreveal_card(idx2, cards, revealed)

def good_end():
    print("\Majority of pairs matched. Triggering good ending (:")

def bad_end():
    print("\nFour turns passed with zero pairs uncovered. Triggering bad ending ):")

def select_card(cards, revealed, cardnum):
    sleep(0.25)
    while True:
        if(cardnum==1):
            print("\nSelect the first card index.")
        else:
            print("\nSelect the second card index.")
        user_input = input("Enter a card index between 1 and 10:  ")

        try:
            idx = int(user_input) - 1
        except ValueError:
            print("\nInvalid input. Please try again.")
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
    print("Beginning the card game!")
    sleep(0.5)
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E']
    random.shuffle(cards)
    revealed = {}
    turns = 0
    run_game=True

    # Game loop
    while run_game:
        print("\nFlayon's turn!")
        sleep(0.25)
        print("\nCards:", end=" ")
        for i, card in enumerate(cards):
            if i in revealed:
                print(card, end=" ")
            else:
                print("?", end=" ")
        sleep(0.25)
        print(f"\nThis is your turn number {turns}.")

        idx1 = select_card(cards, revealed, 1)
        sleep(0.25)
        
        idx2 = select_card(cards, revealed, 2)
        sleep(0.25)
        
        turns += 1
        run_game = handle_selected_pair(idx1, idx2, cards, revealed, turns)
        
        if(run_game):
            enemy_turn(revealed, cards)

if __name__ == "__main__":
    main()