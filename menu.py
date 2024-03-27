#!/usr/bin/python3
""" Menu learning """

option_1 = "1. Walk the dog."
option_2 = "2. Eat lunch."
option_3 = "3. Launch all the missiles."
option_4 = "4. Quit."

title = "Math Helper 3000"
lines = "*"*50

def show_menu():
    print(lines)
    print(title)
    print(lines)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(lines)

def main():
    show_menu()

if __name__ == "__main__":
    main()
