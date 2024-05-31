while True:
    temp = int(input("Enter the unit you wan't choice:\n1. Fahrenheit\n2. Celsius\n3. exit\n"))
    if temp == 1:
        ask_temp = int(input("Enter the value in celsuis: "))
        print("The value in degree celsius is: ",(ask_temp-32)*(5/9),"K")
    elif temp == 2:
        ask_temp = int(input("Enter the value in Fahrenheit: "))
        print("The value in degree celsius is: ",(ask_temp*(9/5))+32,"° C")
    else:
        break