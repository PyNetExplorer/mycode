#!/usr/bin/env python3


def main():
    # ask for a name
    name = input("What is your name?\n")

    # ask for a day of the week
    day = input("What day of the week it is?\n")

    # sleep function
    import time

    # sleep for 1 second
    time.sleep(1)

    #print statement including user inputs name and day
    print ("Hello, " + name + "! Happy " + day + "!")

    # sleep for 1 second
    time.sleep (1)

main()
