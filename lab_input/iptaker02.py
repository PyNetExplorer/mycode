#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # ask for a name
    name = input("What is your name?\n")

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:\n")
    
    # the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    # print() can be given a series of objects separated by a comma
    print("Hi, " + name + ". You told me the IPv4 address is:", user_input)

    #collect and print vendor name
    vendor_name = input ("Please enter your vendor name:\n")
    print("You told me your vendor name is: " + vendor_name)

main()

