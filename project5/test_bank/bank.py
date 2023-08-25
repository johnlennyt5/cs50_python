def main(): 

    response = input("Greeting: ")

    value_to_print = value(response)
    print(f"${value_to_print}")
        
def value(response):
    if "hello" in response.lower().strip():
        return 0
    elif "h" in response[0].lower().strip():
        return 20
    else:
        return 100    



if __name__ == "__main__":
    main()  