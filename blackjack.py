import art
import random

dealer=[]
player=[]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_result(p_score,d_score):
    print(f"    Your final hand: {player}, final score: {p_score}")
    print(f"    Computer's final hand: {dealer}, final score: {d_score}")
    if (p_score > 21):
        print("You went over. You lose.")
    elif (d_score > 21):
        print("Computer went over. You Win!")
    elif (p_score == d_score or (p_score>21 and d_score>21)):
        print("It's a Draw......")
    elif (d_score > p_score):
        print("Computer's Score is higher. You lose.")
    elif (p_score > d_score):
        print("Your Score is higher. You Win!")



def blackjack():
    print(art.logo)
    p_score=0
    d_score=0

    for i in range(0,2):
        y = random.randint(0, len(cards) - 1)
        dealer.append(cards[y])
        d_score += cards[y]
        x = random.randint(0, len(cards) - 1)
        player.append(cards[x])
        p_score += cards[x]

    is_play=True

    while is_play:
        print(f"    Your cards: {player}, current score is: {p_score}")
        print(f"    Computer first card: {dealer[0]}")
        if p_score>21 or d_score>21:
            is_play=False
            print_result(p_score,d_score)
        else:
            cont = input("Type 'y' to get another card , type 'n' to pass: ")
            if cont== "n":
                is_play=False
                print_result(p_score,d_score)
            elif cont=="y":
                if d_score<17:
                    y = random.randint(0, len(cards) - 1)
                    dealer.append(cards[y])
                    d_score += cards[y]
                x = random.randint(0, len(cards) - 1)
                player.append(cards[x])
                p_score += cards[x]


is_playing=True
answer = input("Do you want to play a game of BlackJack? yes or no  ")
while is_playing:
    if answer == "yes":
        dealer=[]
        player=[]
        blackjack()
        answer=input("\n\nDo you want to play another game? yes or no ")
        if answer=="no":
            is_playing=False
    elif answer=="no":
        is_playing=False



