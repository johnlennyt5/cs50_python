# with open("students.csv") as file:
  # for line in file:
    # row = line.strip().split(",")
    # print(f"{row[0]} is in {row[1]}")

# with open("students.csv") as file:
    # for line in file:
      # name, house = line.strip().split(",")
      # print(f"{name} is in {house}")   


  
# students = []
# with open("students.csv") as file:
  # for line in file:
    # name, house = line.strip().split(",")
    # students.append(f"{name} is in {house}")

# for student in sorted(students):
  # print(student)          


#using dictionaries instead of list
# students = []
# with open("students.csv") as file:
#   for line in file:
#     name, house = line.strip().split(",")
#     student = {}
#     student["name"] = name
#     student["house"] = house
#     students.append(student)

# for student in students:
#   print(f"{student['name']} is in {student['house']}")    

# students = []
# with open("students.csv") as file:
#   for line in file:
#     name, house = line.strip().split(",")
#     student = {"name": name, "house": house}
#     students.append(student)

#  def get_name(student):
#    return student["name"]

# # def get_house(student):
#   # return student["house"]

# for student in sorted(students, key=get_name):
#   print(f"{student['name']} is in {student['house']}")    

  
#using lambda function instead of getname function
# students = []
# with open("students.csv") as file:
#   for line in file:
#     name, house = line.strip().split(",")
#     student = {"name": name, "house": house}
#     students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in {student['house']}")  


# #using csv module reader instead of li
# import csv

# students = []
# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for name, home in reader:
#     students.append({"name": name, "home": home})  

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is from {student['home']}")  


# #using csv module Dictionary reader instead of li
# import csv

# students = []
# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "home": row["home"]})  

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is from {student['home']}")  

# # write files using csv writer module
# import csv
# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students.csv", "a") as file:
#   writer = csv.writer(file)
#   writer.writerow([name, home])


# write files using csv DictWriter module
import csv
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"name": name, "home": home})
