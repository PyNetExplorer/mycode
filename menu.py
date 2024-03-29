#!/usr/bin/python3
""" Menu learning """

PI = 3.14159

option_1 = "1. Calculate Area & Circumference of the circle."
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
    # Double star is exponent
    area = PI * r**2
    circ = r*2*PI 
    return area, circ

def eat_lunch():
    pass

def main():
    choice = ' '
    while choice != 4:
        show_menu()
        choice = int(input('Please make a selection. > '))
        if choice == 1:
            a, b = area_circle()
        elif choice ==2:
            eat_lunch()
        print(f'The area is {a} and the circumfrence is {b}.')
    print('Goodbye!')

if __name__ == "__main__":
    main()
