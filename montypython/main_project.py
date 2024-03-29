#!/usr/bin/python3

option_1 = "1. Basic Configuration"
option_2 = "2. Web Server"
option_3 = "3. Mail Server"
option_4 = "4. Database Server"
option_5 = "5. Quit."

title = "Quick Linux Configuration"
lines = "*"*50

def show_menu():
    print(lines)
    print(title)
    print(lines)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(lines)

def main():
    choice = ' '
    while choice != 5:
        show_menu()
        choice = int(input('Please make a selection. > '))
        if choice == 1:
            print("Basic configuration is applied to all servers") # apply Basic Config ansible playbook to all servers
            break
        elif choice == 2:
            print("Web Server is created on Bender")# apply Web Server Playbook to bender
        elif choice == 3:
            print("Mail server is created on Fry")# apply Mail Server Playbook to fry
        elif choice == 4:
            print("Database server is created on Indy")# apply Database Server Playbook to indy
    print('Have a nice day!')


if __name__ == "__main__":
    main()

