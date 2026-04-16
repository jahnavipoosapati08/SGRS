import csv

with open("grievances.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Jahnavi"])

with open("grievances.csv", "r") as file:
    print(file.read())
