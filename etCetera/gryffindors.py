# students = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Ron", "house": "Gryffindor"}
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in gryffindors:
#     print(gryffindor)



# #FILTER
# students = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Ron", "house": "Gryffindor"}
# ]

# # def is_gryffindor(s):
# #     return s["house"] == "Gryffindor"
       
# # gryffindors = filter(is_gryffindor, students)

# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])



# #DICTIONARY COMPREHENSION
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#   gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)



# #DICTIONARY COMPREHENSION
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)


# # ENUMERATE
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

#ENUMERATE
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)


  
