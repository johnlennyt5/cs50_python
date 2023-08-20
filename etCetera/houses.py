students = [
  {"name": "Hermione", "house": "Gryffindor"},
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Ron", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Padma", "house": "Ravenclaw"},
]

# house = []
# for student in students:
#   if student["house"] not in house:
#     house.append(student["house"])

# for house in sorted(house):
#   print(house)    

house = set()
for student in students:
    house.add(student["house"])

for house in sorted(house):
    print(house)