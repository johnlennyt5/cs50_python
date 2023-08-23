def main():
    due = 50
    while due > 0:
        print("Amount Due:", due)  

        coin = int(input("Insert Coin: "))

        if coin in [25,10,5]:
            due -= coin

    change = abs(due)

    print("Change Due:", change)


if __name__ == '__main__':
    main()
