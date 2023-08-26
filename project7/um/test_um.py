from um import count

def main():
    test_casing()
    test_word_with_um()
    test_surrounded_by_space()


def test_casing():
    assert count("Um, thanks for the note") == 1
    assert count(Um, thanks, um) ==2

    
def test_word_with_um():
    assert count(yummy) == 0
   
def test_surrounded_by_space():
    assert count("Hello um world") == 1
    assert count("um?") == 1

