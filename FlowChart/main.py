import random 
from replit import clear
from art import logo

def deal_card():
    """Return Random card from deck."""
    cards = [11 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score of cards"""
    card_sum = sum(cards)
         
    if len(cards) == 2 and card_sum == 21:
            return 0
    
    if 11 in cards and card_sum > 21:
        cards.remove(11)
        cards.append(1)
            
                
    return card_sum

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw 😝"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You Win 😃"
    else:
        return "You Loose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
     
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f" Your cards: {user_cards}, Current Score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if user_score == 0 or user_score >= 21 or computer_cards == 0 or user_score >= 21 :
            is_game_over = True
        else:
            user_should_deal = input("Want to draw another card? : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    
            
        
    
    
    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f" Your Final hand: {user_cards}, final Score:{user_score}")
    print(f" Computer's Final hand: {computer_cards}, final Score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a gae of Blackjacj Tyoe 'y' or 'n'") == "y":
    clear()
    play_game()
