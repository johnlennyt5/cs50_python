# first, _ = input("What's your name? ").split(" ")
# print(f"Hello, {first}")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")


# #unpacked  *coins
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts")


# #unpacked 
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# print(total(galleons=100, sickles=50, knuts=25), "Knuts")


# DICTIONARY
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}"}    

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")


# #unpacked DICTIONARY **
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}    

# print(total(**coins), "Knuts")


#ARGS & KWARGS
def f(*args, **kwargs):
    # print("Positional:", args)
    print("Named:", kwargs)

# f(100,50,25,5)
f(galleons=100, sickles=50, knuts=25)    
