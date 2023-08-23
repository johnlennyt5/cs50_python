def main():
    camelCase = input("CamelCase: ")
    
    print("SnakeCase: ", end="")

    for letter in camelCase:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else: 
            print(letter, end="")

    print()

if __name__ == '__main__':
    main()
