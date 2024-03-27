#!/usr/bin/python3

import time

marvelchars = {
    "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
    "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
}

while True:
    char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk)\nType here: ')
    time.sleep(1)

    char_stat = input('Great choice! What statistic do you want to know about? (real name, powers, archenemy)\nType here: ')
    time.sleep(1)
   
    
    value = marvelchars[char_name.title()][char_stat.lower()]
    
    print("Let's go!")
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

        
    print(char_name.title() + "'s " + char_stat.lower() + " is: " + value.title())
    
    # Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        break

