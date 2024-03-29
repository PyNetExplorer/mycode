#!/usr/bin/python3

vampires = 0

foo = open("dracula.txt","r")
fang = open("vampytimex", "w")
for line in foo:
    if "vampire" in line.lower():
        vampires += 1
        fang.write(line)

foo.close()





