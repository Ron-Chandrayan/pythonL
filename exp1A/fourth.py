# #To convert temperature from Fahrenheit to Celsius and Celsius to Fahrenheit
# The basic formula to convert Fahrenheit and Celsius to each other.
# Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
# Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
# Add, subtract, multiply and divide two complex num

while(True):
    choice = input("Celsius or Fahrenheit ")
    if(choice=="Celsius"):
        temp=float(input("Enter temperature in celsius "))
        fintemp = (temp*(9/5))+32
        print("Temperature in fahrenheit is ",fintemp)
    elif(choice=="Fahrenheit"):
        temp=float(input("Enter temperature in fahrenheit "))
        fintemp = (temp-32)*(5/9)
        print("Temperature in fahrenheit is ",fintemp)
    else:
        print("Invalid choice")
    
    choice2=input("type Y to continue , N to not continue")
    if(choice2=="Y"):
        pass
    else:
        break
