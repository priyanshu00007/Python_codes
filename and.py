my_list = []

while True:
    print("\nMenu:")
    print("1. Create List")
    print("2. Update Element")
    print("3. Append Element")
    print("4. Delete List")
    print("5. Delete Element")
    print("6. Sort List")
    print("7. Find Length")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        my_list = [input(f"Enter element {i+1}: ") for i in range(int(input("Enter number of elements: ")))]
        print("List created successfully!")

    elif choice == "2":
        if my_list:
            index = int(input("Enter index of element to update: "))
            if index < 0 or index >= len(my_list):
                print("Invalid index!")
            else:
                my_list[index] = input("Enter new element: ")
                print("Element updated successfully!")
        else:
            print("List is empty!")

    elif choice == "3":
        if my_list:
            my_list.append(input("Enter element to append: "))
            print("Element appended successfully!")
        else:
            print("List is empty!")

    elif choice == "4":
        my_list = []
        print("List deleted successfully!")

    elif choice == "5":
        if my_list:
            index = int(input("Enter index of element to delete: "))
            if index < 0 or index >= len(my_list):
                print("Invalid index!")
            else:
                del my_list[index]
                print("Element deleted successfully!")
        else:
            print("List is empty!")

    elif choice == "6":
        if my_list:
            my_list.sort()
            print("List sorted successfully!")
        else:
            print("List is empty!")

    elif choice == "7":
        if my_list:
            print("Length of list:", len(my_list))
        else:
            print("List is empty!")

    elif choice == "8":
        break

    else:
        print("Invalid choice! Please try again.")