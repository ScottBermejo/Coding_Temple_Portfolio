import random

class Players_End:

    def __init__(self):
        ace = 1
        jack, queen, king = 10, 10, 10
        self.cardsuits  = ['Diamond','Spade','Club','Heart']
        self.cardnums   = [ace,2,3,4,5,6,7,8,9,10,jack,queen,king]
        
    def first_two_cards(self):
        suite1 =  random.choice(self.cardsuits)
        num1   =  random.choice(self.cardnums)
        suite2 =  random.choice(self.cardsuits)
        num2   =  random.choice(self.cardnums)
        
        print(f'\nYour first two cards are:\n'
              f'{num1} of {suite1}\n'
              f'{num2} of {suite2}')
        return num1 , num2


class Dealers_End:

    def __init__(self):
        ace = 1
        jack, queen, king = 10, 10, 10
        self.cardsuits  = ['Diamond','Spade','Club','Heart']
        self.cardnums   = [ace,2,3,4,5,6,7,8,9,10,jack,queen,king]
        
    def first_two_cards(self):
        suite1 =  random.choice(self.cardsuits)
        num1   =  random.choice(self.cardnums)
        suite2 =  random.choice(self.cardsuits)
        num2   =  random.choice(self.cardnums)
        
        print(f"\nThe dealer's first card is:\n"
              f'{num1} of {suite1}\n')
              #f'{num2} of {suite2}')
        return num1 , num2

class BlackJack:
    def __init__(self,player_card_1,player_card_2,dealer_card_1,dealer_card_2):
        self.playercard1 = player_card_1
        self.playercard2 = player_card_2
        self.dealercard1 = dealer_card_1
        self.dealercard2 = dealer_card_2
        self.player_sum = player_card_1 + player_card_2
        self.dealer_sum = dealer_card_1 + dealer_card_2

    
    def drawCard(self):
        ace = 1
        jack, queen, king = 10, 10, 10
        cardsuits  = ['Diamond','Spade','Club','Heart']
        cardnums   = [ace,2,3,4,5,6,7,8,9,10,jack,queen,king]
        suite = random.choice(cardsuits)
        num = random.choice(cardnums)
        print(f'\nYou drew {num} of {suite}\n')
        self.player_sum += num
        
    

### REAL GAME ###
def runGame():
    done = False
    while not done:
        game_trial1 = Players_End() 
        game_trial2 = Dealers_End()

        player_card_1, player_card_2 = game_trial1.first_two_cards()
        dealer_card_1, dealer_card_2 = game_trial2.first_two_cards()

        real_game = BlackJack(player_card_1, player_card_2,dealer_card_1, dealer_card_2)
        while real_game.player_sum < 21:    
            user_inp = input("Do you want to hit or stay?: ").lower()
            if user_inp == 'hit':
                real_game.drawCard()
            elif user_inp == 'stay':
                break
            else:
                print("Invalid Input.")
                continue

        if real_game.player_sum > real_game.dealer_sum and real_game.player_sum <= 21:
            print("Congratulations You Won against the dealer. ")   
        else:
            print("The dealer had: ", real_game.dealer_sum)
            print("Sorry the Dealer the Won.")
                    
        u_input = input("Game Over! Do you wanna play again? Yes or No:  ").lower()
        while u_input.lower() != 'yes' and u_input.lower() != 'no':
            print( "Invalid Input. Yes or No.")
            u_input = input("Game Over! Do you wanna play again? Yes or No:  ").lower()
        if u_input == 'yes':
            real_game.player_sum = 0
        if u_input == 'no':
            done = True
runGame()











