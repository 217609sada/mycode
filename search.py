#!/usr/bin/env python
counter = 0
with open('romeo.txt') as ip_file:
    lines = ip_file.readlines()
    for x in lines:
        if "romeo" in x.lower(): 
            counter = counter + 1
print(counter)
