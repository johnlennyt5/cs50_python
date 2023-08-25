import inflect

def main():
    names = []
    
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    p = inflect.engine()
    output = p.join(names)
    print("Adieu , adieu, to " + output)

if __name__ == '__main__':
    main()
