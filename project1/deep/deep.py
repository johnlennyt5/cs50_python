def main():
    response = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    if response.strip().lower() == "forty-two" or response.strip().lower() == "forty two" or response.strip().lower()  == "42":
        print("Yes")
    # elif response.lower().strip()  == "forty-two":
    #     print("Yes") 
    # elif response.lower().strip()   == "forty two":
    #     print("Yes")

    else:
        print("No")
    

if __name__ == "__main__":
    main()
