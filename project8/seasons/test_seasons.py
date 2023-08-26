from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("1978-09-08") == ("1978", "09", "08")
    assert check_birthday("1978-9-8") == None
    assert check_birthday("June 3, 1995") == None


if __name__ == "__main__":
    main()  