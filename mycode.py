#!/usr/in/env python3
print("Input 1'st numbers for operation ")
a = int(input())
print("Input 2'nd number for operation ")
b = int(input())
operation = input("Select one the below operation 1. add 2. multiple 3. quit ----- ")
#operation = int(input())
if operation == "1":
    c = a + b
    print("result = " + str(c))
elif operation == "2":
    c = a * b
    print("result = " + str(c))
elif operation == "3":
    print("quit")
