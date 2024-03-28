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

def area_circle():
    r = int(input('Type the radius of the circle. > '))
    area = 3.14 * r**2
    return area

def eat_lunch():
    pass

def main():
    show_menu()
    choice = int(input('Please make a selection. > '))
    if choice == 1:
        answer = area_circle()
    print(answer)

if __name__ == "__main__":
    main()
