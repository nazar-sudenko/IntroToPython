#Write a program that prints all the even numbers from 2 to a number given by the user.
#Example output:

#Give a number: 14
#2 4 6 8 10 12 14

number = int(input("Give a number: "))
a = 2

while a <= number:
    print(a, end=" ")
    a += 2
