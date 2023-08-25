def main():

    replace = input("Input: ")
    print("Output: ", end="")
   
    for letter in replace:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            print(letter, end="")
    
    print()

if __name__ == '__main__':
    main()


