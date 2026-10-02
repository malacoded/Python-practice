# WEIGHT CONVERTER KG TO POUNDS

weight = float(input("Enter your weight: "))
unit = input("kg or pounds: ")
print("1.Convert to pounds")
print("2.Convert to kg")
choice = int(input("Enter the choice: "))
print(choice)
if choice == 1:
    result = weight*2.205
    print("Your weight is: pounds",result)
elif choice == 2:
    result = weight/2.205
    print("Your weight is: kg",result)
    print(result)
    
    
               
