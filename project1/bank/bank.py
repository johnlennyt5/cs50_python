def main(): 

    response = input("Greeting: ")


    if "hello" in response.lower().strip():
        print("$0")
    
    elif "h" in response[0].lower().strip():
        print("$20")
    else:
      print("$100")    



if __name__ == "__main__":
    main()  