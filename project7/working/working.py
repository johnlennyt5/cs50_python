import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    isFormatCorrect = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM)  to  (\d{1,2}):?(\d{2})? (AM|PM)$", s)
    if isFormatCorrect:
        pieces = isFormatCorrect.groups()
        if int(pieces[0]) > 12 or int(pieces[3]) > 12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + "to" + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            hour = 0
        else:
            hour = int(hour)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}:" + minute

    return new_time

if __name__ == '__main__':
    main()
