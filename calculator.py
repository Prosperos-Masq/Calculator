while True:
    start = input("Hello! I'm your calculator would you like to use me (y/n)?: ").strip().lower()
    if start == "y" or "yes":
        calculate = input("Would you like to Multiply/Divide/Add/Subtract? :").strip().lower()
        if calculate == "add":
            num1 = input("To add please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            answer = int(num1) + int(num2)
            print("The answer is {}!".format(answer))
        elif calculate == "subtract":
            num1 = input("To subtract a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            answer = int(num1) - int(num2)
            print("The answer is {}!".format(answer))
        elif calculate == "multiply":
            num1 = input("To multiply a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            multiply = int(num1) * int(num2)
            print("The answer is {}!".format(multiply))
        elif calculate == "divide":
            num1 = input("To divide a number please enter a number: ").strip()
            num2 = input("Please enter another number: ").strip()
            answer = int(num1) / int(num2)
            print("The answer is {}!".format(answer))
    else:
         print("Okay! Another time then!")