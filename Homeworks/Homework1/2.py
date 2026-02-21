#Ask user to give the year's income and calculate and print the tax. 
#If income is less than 10000, tax is 8%, if between 10001 and 26000 tax is 12%, otherwise tax is 24%. (obviously these are random and not realistic tax values)

income = int(input("What is your year's income? "))

if income <= 10000:
    incometax = income*0.08
elif income < 26001:
    incometax = income*0.12
else:
    incometax = income*0.24

print("Your tax is: " + str(incometax))