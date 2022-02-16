#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, time, sys

COLORS = ["Hearts","Diamonds","Spade","Clubs"]

money = 100
cards = []
card1, card2 = None, None

def print(text=""):
    text += "\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)

def generate_cards():
    global cards
    cards = []
    for i in range(13):
        for j in range(4):
            cards.append((i, j))

    random.shuffle(cards)

def get_card():
    global cards
    return cards.pop()

def card_name(card):
    name = str(card[0]+1)

    if card[0] == 0:
        name = "Ace"
    elif card[0] >= 10:
        name = ["Jack","Queen","King"][card[0]-10]

    color = COLORS[card[1]]

    return f"{name} of {color}"

if __name__ == "__main__":
    running = True
    print("       ----- Welcome to Acey Ducey -----       ")
    print("You will be presented two cards. You can then")
    print("bet some of your money if you think the next")
    print("card will have a value between those cards.")
    print("The game stops when you have no more money or")
    print("if you type 'stop'.")
    print()
    print()
    print("Press Enter to begin")
    input()
    print()

    generate_cards()

    while running:
        card1 = get_card()
        card2 = get_card()

        print(f"The first card is: "+card_name(card1))
        time.sleep(1)
        print(f"The second card is: "+card_name(card2))
        time.sleep(1)
        print(f"Current balance: {money}")
        time.sleep(1)

        print("How much money do you want to bet ? ")
        while True:
            bet = input()
            if bet == "stop":
                running = False
                break

            if not bet.isdecimal():
                print("Please enter a valid number")
                time.sleep(0.5)
                continue

            bet = int(bet)
            if bet > money:
                print("You can't bet more than you have !")
                time.sleep(0.5)
                continue
            break

        if running == False:
            break

        card3 = get_card()
        time.sleep(1)
        print(f"And the third card is: "+card_name(card3))
        time.sleep(0.5)
        if bet == 0:
            print("No change to your balance")

        else:
            if (card1[0] < card3[0] < card2[0]) or (card2[0] < card3[0] < card1[0]):
                print(f"Well done ! You won {bet}")
                money += bet
            else:
                print(f"Oh no, you lost {bet}")
                money -= bet

        print()
        print()
        time.sleep(1)

        if money == 0:
            print("It seems you've spent all your money")
            print("Maybe next time you'll be more lucky")
            running = False

        elif len(cards) < 3:
            print("Reshuffling the deck")
            generate_cards()
