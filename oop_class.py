class Grievance:
    def __init__(self, id, name, reg_no):
        self.id = id
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print(self.id, self.name, self.reg_no)

g1 = Grievance(1, "Jahnavi", "123")
g1.display()
