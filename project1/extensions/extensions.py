def main():
    file = input("File name: ").lower()

    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".jpeg"):  
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("application/txt")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
