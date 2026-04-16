grievances = []

while True:
    print("\n1. Add Grievance")
    print("2. View Grievances")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        grievances.append(name)
    elif choice == '2':
        print("Grievances:", grievances)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
