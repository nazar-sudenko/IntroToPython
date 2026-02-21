#Question of Celsius to Fahrenheit or Fahrenheit to Celsius?

def converter():
    question = input("Celsius to Fahrenheit(CtF) or Fahrenheit to Celsius(FtC)? ")
    if question == "CtF":
        celsius = float(input("Enter the Celsius: "))
        fahrenheit = ((celsius * 9/5) + 32)
        return fahrenheit
    elif question == "FtC":
        fahrenheit = float(input("Enter the Fahrenheit: "))
        celsius = ((fahrenheit - 32)/1.8)
        return celsius

print(converter())
         
