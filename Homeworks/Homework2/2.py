#factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Enter number you wanna get a factorial of: "))))
