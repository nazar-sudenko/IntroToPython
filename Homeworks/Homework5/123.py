import csv

file1 = open("Homeworks/Homework5/people.csv", 'r')
file2 = open("Homeworks/Homework5/employees.csv", 'r')

lines1 = csv.reader(file1)
lines2 = csv.reader(file2)


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = None
        self.phone = None

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_phone(self, phone):
        self.phone = phone

class Employee(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.company = None
        self.salary = None

    def set_company(self, company):
        self.company = company

    def set_salary(self, salary):
        self.salary = salary


for line in lines1:
    p = Person(line[0], line[1])
    p.set_birthdate(line[2])
    p.set_phone(line[3])
    print(p.firstname)
    print(p.lastname)
    print(p.birthdate)
    print(p.phone)

for line2 in lines2:
    e = Employee(line2[0], line2[1])
    e.set_birthdate(line2[2])
    e.set_phone(line2[3])
    e.set_company(line2[4])
    e.set_salary(line2[5])
    print(e.firstname)
    print(e.lastname)
    print(e.birthdate)
    print(e.phone)
    print(e.company)
    print(e.salary)


file1.close()
file2.close()