#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

def gen():
    nums = list(range(10))
    random.shuffle(nums)
    return "".join([str(nums.pop()) for i in range(3)])

def analyze(guess, number):
    result = []

    for i in range(3):
        if guess[i] == number[i]:
            result.append("FERMI")

        elif guess[i] in number:
            result.append("PICO")

    if len(result) == 0:
        return "BAGELS"

    else:
        return " ".join(result)

if __name__ == '__main__':
    print("I am thinking of a three-digit number. Try to guess")
    print("my number and I will give you clues as follows:")
    print("   PICO   - One digit correct but in the wrong position")
    print("   FERMI  - One digit correct and in the right position")
    print("   BAGELS - No digits correct")
    print()

    num = gen()
    won = False
    print("O.K. I have a number in mind.")

    for i in range(20):
        guess = input(f"Guess # {i+1}     ? ")
        if guess == num:
            won = True
            break
        else:
            print(analyze(guess, num))

    if won:
        print("You got it!!!")
    else:
        print("Oh well")
        print(f"That's twenty guesses. My number was {num}")
