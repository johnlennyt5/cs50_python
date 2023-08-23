while True:
    fuel= input("Fractions: ")
    try:
        x,y = fuel.split('/')

        new_x = int(x)
        new_y = int(y)

        fraction = (new_x/new_y)
        if fraction <= 1:
          break        
    except (ValueError, ZeroDivisionError):
        pass

percentage = int(fraction * 100)       
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
           
