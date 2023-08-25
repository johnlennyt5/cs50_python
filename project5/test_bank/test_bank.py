from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

def test_return_zero():
    assert value ('hello man ') == 0
    assert value ('Hello') == 0
    assert value ('HELlo Woman') == 0

def test_return_20():
    assert value ('Hey bud') == 20
    assert value ('hi  guy ') == 20


def test_return_100():
    assert value ('Welcome sports') == 100
    assert value ('what is up') == 100



if __name__ == '__main__':
    main()