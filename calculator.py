import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.subtraction")
print("5.square root addition")
choice = int(input("Choose the operation: "))
print(choice)
if choice == 1:
    result = num1 + num2
    print("The sum is: ",result)
elif choice == 2:
    result = num1 - num2
    print("The subtraction is: ",result)
elif choice == 3:
    result = num1 * num2
    print("The multiplication is: ",result)
elif choice == 4:
    if num2 != 0:
        result = num1/num2
        print("The subtraction is: ",result)
    else:
        print("Subtractin by zero is not possible")
elif choice == 5:
    result = math.sqrt(num1) + math.sqrt(num2)
    print("result is: ",result)
else:
    print("choose the choice between 1 to 5")
        
    
    


    
