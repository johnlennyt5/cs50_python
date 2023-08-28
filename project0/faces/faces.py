def main():
    
    msg = input("How do you feel? ")
    result = convert(msg)
    print(result)

def convert(msg):
    
    msg1 = msg.replace(":)", '🙂')
    msg2 = msg1.replace(":(", '🙁')
    return msg2

if __name__ == "__main__":
    main()  

