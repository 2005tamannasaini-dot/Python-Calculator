# calculator project

print(" ======== CALCULATOR.🥰 ========")

while True:
    operation = input("Enter the operation(+,-, *,/,%,power, square,):")

    if operation == "square":
        num1 = float(input("Enter first number:"))
        print ("Result:", num1 ** 2)

    else:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        
        if operation== "+":
            print("Result:",num1+num2)

        elif operation == "-":
            print ("Result:", num1-num2)

        elif operation == "*":
            print ("Result:",num1*num2)

        elif operation == "/":
            if num2 != 0:
                print("Result:", num1/num2)
            else:
                print("cannot divide by zero.")

        elif operation == "%":
            if num2 != 0:
                print("Result:", num1%num2)
            else:
                print("cannot divide by zero.")
            
        
        elif operation == "power":
            print("Result:", num1 ** num2)

        else:
            print("Invalid operation.")

    choice = input("continue?(yes/no):").lower()

    if choice == "no":
        print("calculator closed.")
        break        


        