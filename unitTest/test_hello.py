# from hello import hello

# def test_hello():
    # assert hello("David") == "hello, David"
    # assert hello() == "hello, world"

from hello import hello

def test_default():
    assert hello() == "hello, world"

# def test_argument():
    # assert hello("David") == "hello, David"

def test_argument():
  for name in ["Hermione", "Ron", "Harry"]:
    assert hello(name) == f"hello, {name}"