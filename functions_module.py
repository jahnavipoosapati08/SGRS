grievances = []

def add_grievance():
    name = input("Name: ")
    grievances.append(name)

def view_grievances():
    print(grievances)

def delete_grievance():
    name = input("Enter name to delete: ")
    if name in grievances:
        grievances.remove(name)

add_grievance()
view_grievances()
