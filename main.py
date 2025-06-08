#external Python imports for functions
from game_logic import deal, cards_logic,return_winner

#main function
def main():
    score={"Dealer":0,
        "Player":0}      #score represented as dictionary with keys being the dealer and player
                         #and the value being their total score each
    print("Welcome to Python BlackJack!\n------------------------------------------------")
    ans=input("Wanna play? Yes(y) or no(n):")
    deck=["2","3","4","5","6","7","8","9","10","J","Q","K","A",]    #deck represented as list 
    dealers_hand=[]
    players_hand=[]
    total_dealer=0
    total_player=0


    while ans.lower()=="y":         #finish game when user types "n" as an answer
        dealers_hand.append(deal(deck))     #dealing first 2 cards for dealer and player
        players_hand.append(deal(deck))
        dealers_hand.append(deal(deck))
        players_hand.append(deal(deck))
        print("Dealer has: ",dealers_hand[0],"and one card face down and you have ",players_hand[0],players_hand[1])
        total_dealer=cards_logic(dealers_hand)      #counting each hand so far
        total_player=cards_logic(players_hand)

        hit=input("Do you want to hit? Yes(y) or no(n):")
        while hit.lower()=="y" and total_player<=21:     #if the player wants to hit and has less than 21
            print(total_player)
            players_hand.append(deal(deck))              #deal 1 more card
            total_player=cards_logic(players_hand)       #count current hand value
            print("You got,",players_hand,"total",total_player)
            if total_player>21:                         #check if player has more than 21
                print("You Busted")
                break
            hit=input("Do you want to hit?(y)(n)")      #condition for dealing more cards to the player
        while total_dealer<=17:                         #dealer deals while their hand is less/equal than 17
            dealers_hand.append(deal(deck))
            total_dealer=cards_logic(dealers_hand)
            if total_dealer>21:
                print("Dealer Busted")
                break
            elif total_dealer==17:
                break
        print("Dealer had ", total_dealer,"and you had ", total_player)
        print(dealers_hand,players_hand)
        return_winner(total_dealer,total_player,score)   #function determining the winner
        dealers_hand.clear()        #cleaning both hands for next game
        players_hand.clear()
        total_dealer=0              #cleaning total value for next game
        total_player=0
        ans=input("Next game?(y)(n)")   #if "y" proceeds to the next game if "n" program terminates
    print(f"The final score of the game is:\n Dealer: {score['Dealer']}\tPlayer: {score['Player']}")


#main call
if __name__=="__main__":
    main()