# calculator project

print(" ======== CALCULATOR.🥰 ========")

while True:
    operation = input("Enter the operation(+,-, *,/,%,power, square, cube,):")

    valid_operation = ["+","-", "*","/","%","power", "square", "cube"]

    if operation  not in valid_operation:
        print("Invalid operation:, Please choose the Right operation")
        continue

    try:
       
        if operation == "square":
            num1 = float(input("Enter first number:"))
            print ("Result:", num1 ** 2)

        elif operation == "cube":
            num1 = float(input("Enter first number:"))
            print("Result:", num1**3)

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
                    print("Cannot divide by zero.")

            elif  operation == "%":
                if num2 != 0:
                    print("Result:", num1%num2)
                else:
                    print("Cannot divide by zero.")
                
            elif  operation == "power":
                print("Result:", num1 ** num2)

            else:
                print("Invalid operation.")

    except ValueError:
        print("Invalid input! Please enter number only.")        

    while True:
        choice = input("continue?(yes/no):").lower()

        if choice == "yes":
            break

        elif choice == "no":
            print("calculator closed.")
            exit()

        else:
            print("Invalid choice! Please enter only yes or no.")
        
        

        