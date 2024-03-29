#!/usr/bin/python3

beer = "bottles of beer"
wall = "bottles of beer on the wall!"
take = "Take one down, pass it around!"
no_more = "No more bottles of beer on the wall!"

count = int(input("How many beers to count down from?\n> "))

if count > 100:
    print("Sorry, maximum number allowed is 100. Exiting.")
    exit()

for i in range(count, 0, -1):
    print(f"{i} {wall} {i} {beer}!")
    print(f"{take} {i - 1 if i > 1 else no_more}\n")