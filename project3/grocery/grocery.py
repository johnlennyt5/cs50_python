list = {}
    
      
while True:
    try:
        item = input().lower()

        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    
    except EOFError:
        for key in sorted(list):
            print(list[key], key.upper())
        break