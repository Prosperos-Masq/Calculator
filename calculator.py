calculator = True
while calculator:
    start = input("Hello! I'm your calculator would you like to use me (y/n)?: ").strip().lower()
    if start == "y" or "yes":
        calculate = input("Would you like to Multiply(m)/Divide(d)/Add(a)/Subtract(s)/Power(p)? :").strip().lower()
        if calculate == "add" or "a":
            num1 = input("To add please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            add = int(num1) + int(num2)
            print("{} + {} is {}!".format(num1, num2, add))
        elif calculate == "subtract" or "s":
            num1 = input("To subtract a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            subtract = int(num1) - int(num2)
            print("{} - {} is {}!".format(num1, num2, subtract))
        elif calculate == "multiply" or "m":
            num1 = input("To multiply a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            multiply = int(num1) * int(num2)
            print("{} x {} is {}!".format(num1, num2, multiply))
        elif calculate == "divide" or "m":
            num1 = input("To divide a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            divide = int(num1) / int(num2)
            print("{} / {} is {}!".format(num1, num2, divide))
        elif calculate == "power" or "p":
            num1 = input("Please enter a number: ").strip()
            num2 = input("Please enter another number for the power of: ").strip()
            power = int(num1) ** int(num2)
            print("{} to the power of {} is: {}!".format(num1, num2, power))
    else:
         print("Okay! Another time then!")