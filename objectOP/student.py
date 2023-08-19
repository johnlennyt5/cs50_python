# def main():
#     name = input("Name: ")
#     house = input("House: ")
#     print(f"{name} from {house}")

# def get_name():
#     retrun input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()

# #tuple get error immutable ()
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()


# #list no tuple mutable []
# def main():
#     student= get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()


# #Dictionary mutable {}
# def main():
#     student= get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

# #Dictionary mutable {}
# def main():
#     student= get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()


# #classes
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()


# # classes
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"):
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()



# #classes added patronus
# class Student:
#     def __init__(self, name, house,patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"):
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
    
#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "Stag charm"
#             case "Otter":
#                 return "Otter charm"
#             case "Jack Russel terrier":
#                 return "Jack Russel terrier charm"
#             case _:
#                 return "No charm"

# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)
      

# if __name__ == "__main__":
#     main()


#classes
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #getter
    @property
    def name(self):
        return self._name
    #setter
    @name.setter   
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self, house):
        if house not in ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"):
            raise ValueError("Invalid house")       
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
      

if __name__ == "__main__":
    main()
