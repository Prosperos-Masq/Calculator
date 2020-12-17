calculator = True
while calculator:
    start = input("Hello! I'm your calculator would you like to use me (y/n)?: ").strip().lower()
    if start == "y" or "yes":
        calculate = input("Would you like to Multiply/Divide/Add/Subtract/Power? :").strip().lower()
        if calculate == "add":
            num1 = input("To add please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            add = int(num1) + int(num2)
            print("{} + {} is {}!".format(num1, num2, add))
        elif calculate == "subtract":
            num1 = input("To subtract a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            subtract = int(num1) - int(num2)
            print("{} - {} is {}!".format(num1, num2, subtract))
        elif calculate == "multiply":
            num1 = input("To multiply a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            multiply = int(num1) * int(num2)
            print("{} x {} is {}!".format(num1, num2, multiply))
        elif calculate == "divide":
            num1 = input("To divide a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            divide = int(num1) / int(num2)
            print("{} / {} is {}!".format(num1, num2, divide))
        elif calculate == "power":
            num1 = input("To add please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            power = int(num1) ** int(num2)
            print("{} to the power of {} is: {}!".format(num1, num2, power))
    else:
         print("Okay! Another time then!")