# import sys
# print("hello, my name is", sys.argv[1])

# import sys
# try:
  # print("hello, my name is", sys.argv[1])
# except IndexError:
  # print("Too few argumetents")

# import sys
# if len(sys.argv) < 2:
  # print("Too few arguments")
# elif len(sys.argv) > 2:
  # print("Too many arguments")
# else:  
  # print("hello, my name is", sys.argv[1])


# import sys

#check for errors
# if len(sys.argv) < 2:
    # sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
    # sys.exit("Too many arguments")

#Print name tags
# print("hello, my name is", sys.argv[1])


import sys

if len(sys.argv) < 2:
  sys.exit("Too few arguments")

for arg in sys.argv[1:]:
  print("hello, my name is", arg)
