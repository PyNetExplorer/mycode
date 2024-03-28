#!/usr/bin/python3
""" Drink your water | Ekaterina Williams """


import time

while True:
    try:
        print("*"*50)
        print("We are about to find out if you drank enough water today!")
        print("*"*50)
        time.sleep(1)

        water = int(input("How many cups of water did you drink today so far?\nAnswer here (numbers only) ==> "))
        if water >= 9:
            print("Oh wow! You really like water!!!")
        elif water >= 5:
            print("Good, keep it up!")
        else:
            print("Dehydration alert! You need to drink more!")

        time.sleep(1)
        
        choice = input("Do you want to enter again? (yes/no): ")
        if choice.lower() != 'yes':
            break

    except:
        print("You did not enter a number")

        choice = input("Do you want to enter again? (yes/no): ")
        if choice.lower() != 'yes':
            break


