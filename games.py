import random

money = 100

#Write your game of chance functions here

import random

def coin_flip(guess, bet):
    coin = random.randint(1, 2)  # Randomly generate 1 or 2 for coin flip
    if coin == 1:
        result = "Heads"
    elif coin==2 :
        result = "Tails"
    
    if guess == result:  # Player's guess matches the coin flip result
        if guess == "Heads":
            winnings = bet
        if guess== "Tails":
            winnings = bet
            return winnings
    else:
      return -bet



def Cho_han(guess, bet):
    dice_sum = random.randint(2, 12)
    if dice_sum % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    
    if guess == result:
        winnings = bet
        return winnings
    else:
        return -bet


def card_game(bet):
    deck = list(range(1, 14)) * 4  # Create a deck with numbers 1 to 13 (four of each)
    
    # Simulate player 1 drawing a card
    player1_card = random.choice(deck)
    deck.remove(player1_card)
    
    # Simulate player 2 drawing a card
    player2_card = random.choice(deck)
    deck.remove(player2_card)
    
    if player1_card > player2_card:  # Player 1 wins
        return bet
    elif player2_card > player1_card:  # Player 2 wins
        return -bet
    else:  # It's a tie
        return 0
import random

def roulette(guess,bet):
    result = random.randint(0, 36)  # Generate a random number between 0 and 36
    
    if result == 0 or result == 00:  # Handle 0 and 00 spots
        if guess == "0" or guess == "00":  # Player's guess matches the result
            winnings = 35 * bet  # Payout for specific number bet
            return winnings
        else:  # Player's guess does not match the result
            return -bet
    
    if guess.isdigit():  # Player bet on a specific number
        if int(guess) == result:  # Player's guess matches the result
            winnings = 35 * bet  # Payout for specific number bet
            return winnings
        else:  # Player's guess does not match the result
            return -bet
    elif guess == "Even":  # Player bet on "Even"
        if result % 2 == 0 and result != 0:  # Result is an even number (excluding 0)
            return bet
        else:  # Result is an odd number or 0
            return -bet
    elif guess == "Odd":  # Player bet on "Odd"
        if result % 2 == 1 and result != 0:  # Result is an odd number
            return bet
        else:  # Result is an even number or 0
            return -bet
    else:  # Invalid guess
        return 0



#Call your game of chance functions here
money+=coin_flip("Tails",10)+ Cho_han("Odd", 10)+card_game(10)+roulette("Odd",70)
print(money)
