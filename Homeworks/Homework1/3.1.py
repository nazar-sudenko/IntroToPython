#Write a program to ask 2 numbers, a and b, from the user. Then print all the numbers from a to b. 
#Examples:

#Give a: 8
#Give b: 12
#8 9 10 11 12

#Give a: 10
#Give b: 5
#Error, a must be less than b

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if a > b:
    print("Error, a must be less than b")
else:
    for i in range(a, b+1):
        print(i, end=" ")
