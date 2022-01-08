print("Welcome to Calculator App")
#while loop to keep the calculator running
while 1:
    print("What would you like to do: ") #asking for the calculator function
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. End")
    Selection = int(input("enter your Selection: "))
    if Selection == 1:
        num1= int(input("Enter your first number: "))
        num2= int(input("Enter your second number: "))
        print("Output: ", num1+num2)
    elif Selection == 2:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("Output: ", num1-num2)
    elif Selection == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("Output: ", num1*num2)
    elif Selection == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        print("Output: ", num1/num2)
    elif Selection == 5:
        print("Exiting...")
        break
    else:
        print("you enter wrong selection, please enter Selection from 1 to 5")
    print()

