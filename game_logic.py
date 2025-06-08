#import for randomizing card deal
import random as rd

#deal a card to player or dealer
def deal(deck):
    card=rd.choice(deck)    #random choice() between all cards in the list deck[]
    return card             #return the card

#count dealer/player hand value
def cards_logic(card):
    value=0
    aces=0
    for i in card:          #for all cards in list that are passed as arguement 
        if i=="J" or i=="K" or i=="Q":      #if the are Jack King or Queen the count as 10
            value+=10
        elif i=="A":                        #if it's an ace it counts as 11 but we keep track of how many
            value+=11
            aces+=1
        else:                               #if it's number we pass the exact value
            value+=int(i)
    while value>21 and aces:                #implement ace logic to count as 1 if hand exceeds value of 21
        value -= 10
        aces -= 1
    return value

#determine winner
def return_winner(total_dealer,total_player,score):
    if (total_dealer<total_player and total_player<=21) or (total_dealer>21 and total_player<=21):
        print("You won!")
        score["Player"]+=1      #adding to the value of the score dictionary with key "Player"
    elif (total_player<total_dealer and total_dealer<=21) or total_player>21:
        print("Dealer won!")
        score["Dealer"]+=1      #adding to the value of the score dictionary with key "Dealer"
    else:
        print("It's a tie!")
