my_list = []
while True:
    print("\n---List Operations Menu---")
    print("1.Insert an element")
    print("2.Remove an element")
    print("3.Append an element")
    print("4.Display length of the list")
    print("5.Pop an element")
    print("6.Clear the list")
    print("7.Display the list")
    print("8.Exit")
    choice = input("Enter your choice(1-8):")
    if choice=='1':
        element = input("Enter element to insert:")
        position = int(input("Enter position to insert at:"))
        my_list.insert(position,element)
        print("list value after insert:",my_list)
    elif choice=='2':
        element = input("Enter element to remove:")
        if element in my_list:
            my_list.remove(element)
            print("list value after remove:",my_list)
        else:
            print("Element not found in the list.")
    elif choice=='3':
        element = input("Enter element to Append:")
        my_list.append(element)
        print("list value after append:",my_list)
    elif choice=='4':
        print("lenth of the list:",len(my_list))
    elif choice=='5':
        if my_list:
            popped = my_list.pop()
            print("popped element:",popped)
            print("list value after pop:",my_list)
    elif choice=='6':
        my_list.clear()
        print("list cleared.")
    elif choice=='7':
        print("current list:",my_list)
    elif choice=='8':
        print("Exiting program. Good bye!")
        break 
    else:
        print("Invalid choice. please enter a number between 1 and 8")
