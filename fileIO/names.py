# name = input("What's your name: ")
# print(f"Hello, {name}")

# names = []
# for i in range(3):
    # name = input("What's your name? ")
    # names.append(name)
    # names.append(input("What's your name? "))

# for name in sorted(names):
    # print(f"Hello, {name}")


# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name)
# file.close()

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
    # file.write(f"{name}\n")

#read file
# with open("names.txt", "r") as file:
    # lines = file.readlines()
# for line in lines:
    # print("hello,", line, end="")    
    # print("hello,",line.strip())

#removed extra line 
# with open("names.txt", "r") as file:
    # for line in file:
      # print("hello,", line.strip())


names = []
with open("names.txt") as file:
  for line in file:
    names.append(line.strip())

for name in sorted(names, reverse=True):
  print(f"Hello, {name}")    