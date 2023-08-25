from plates import is_valid


def main():

    test_min_n_max_characters()
    test_start_with_2_letters()
    test_middle_numbers()
    test_zero()
    test_punctuation()

    
def test_min_n_max_characters():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False


def test_start_with_2_letters():
    assert is_valid('AB') == True
    assert is_valid('B2') == False
    assert is_valid('2A') == False
    assert is_valid('55') == False

def test_middle_numbers():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
    assert is_valid('BB55TT') == False
    assert is_valid('BBMN60') == True


def test_zero():
    assert is_valid('AAAC50') == True
    assert is_valid('AAAC05') == False
    

def test_punctuation():
    assert is_valid('PIB.14') == False
    assert is_valid('PIB!14') == False
    assert is_valid('PIB?14') == False
    assert is_valid('PIB,14') == False
    assert is_valid('PIB 14') == False
    
if __name__ == "__main__":
    main()  