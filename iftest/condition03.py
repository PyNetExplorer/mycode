#!/usr/bin/env python3
""" Katya | If statements"""


hostname = input("What value should we set for hostname?")
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")

# letting the user know that program ends
print("Exiting the script")
