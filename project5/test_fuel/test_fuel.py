from fuel import convert, gauge
import pytest

def main():
    
    test_correct_input()
    test_value_error()
    test_zero_division()

def test_correct_input():
    assert convert('1/2') == 50 and gauge(50) == '50%'
    assert convert('99/100') == 99 and gauge(99) == 'F'
    assert convert('1/100') == 1 and gauge(1) == 'E'

def test_value():
    with pytest.raises(ValueError):
        assert convert('a/b') == valueError
        assert convert('a/5') == valueError
        assert convert('5/a') == valueError

def test_zero_division():    
     with pytest.raises(ZeroDivisionError):
         assert convert('1/0') == ValueError

if __name__ == "__main__":
    main()