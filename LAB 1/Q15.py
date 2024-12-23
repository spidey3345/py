#Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, Dob):
        self.name = name
        self.country = country
        self.Dob = Dob

    def calculateAge(self):
        current_year = 2024
        current_month = 11
        current_day = 24
        
        birth_year, birth_month, birth_day = map(int, self.Dob.split('-'))
        
        age = current_year - birth_year
        if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
            age -= 1
        return age

name = input("Enter name: ")
country = input("Enter country: ")
Dob = input("Enter date of birth (YYYY-MM-DD): ")

person = Person(name, country, Dob)
print(f"{person.name} is {person.calculateAge()} years old and lives in {person.country}.")

