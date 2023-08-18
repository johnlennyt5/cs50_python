# email = input("What's your email address? ").strip()
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#   print("Valid")
# else:
#   print("Invalid")



# import re
# email = input("What's your email address? ").strip()

# if re.search("^.+@.+\.edu$", email):
#   print("Valid") 
# else:
#   print("Invalid")



# import re
# email = input("What's your email address? ").strip()
# if re.search("^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")



# import re
# email = input("What's your email address? ").strip()
# if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")



import re
email = input("What's your email address? ").strip()  
  
if re.search("^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")    