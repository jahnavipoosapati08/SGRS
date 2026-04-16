grievances = []

def add_grievance():
    g = {
        "name": input("Name: "),
        "reg_no": input("Reg No: "),
        "category": input("Category: "),
        "desc": input("Description: ")
    }
    grievances.append(g)

def view():
    for g in grievances:
        print(g)

add_grievance()
view()
