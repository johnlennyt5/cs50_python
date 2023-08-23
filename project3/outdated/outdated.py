month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
date = input("Date: ")
    try:
         year, month, day = date.split("/")
        if  int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break
    except:       
        try:
           year, old_month, old_day = date.split(" ")
           for i in range(len(month)):
               if month[i] == old_month:
                   month = i + 1
            day = old_day.replace(",", "")
             if  int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break
        except:
            print()  


print(f"{year}-{int(month):02}-{int(day):0d}")