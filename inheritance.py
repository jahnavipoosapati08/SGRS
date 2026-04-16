class Record:
    def __init__(self, id):
        self.id = id

class Grievance(Record):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

g = Grievance(1, "Jahnavi")
print(g.id, g.name)
