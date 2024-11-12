# import pytest

def fizzbuzz(value):
	if check_modulo(int(value), 3):
		if check_modulo(int(value), 5):
			return "FizzBuzz"
		return "Fizz"
	if check_modulo(int(value), 5):
		return "Buzz"
	return value
def check_modulo(dividend, divisor):
	return dividend % divisor == 0
def check_fizzbuzz(value, expected_value):
	result = fizzbuzz(value)
	assert result == expected_value

def test_returns_1_when_1_is_passed():
	check_fizzbuzz("1", "1")
def test_returns_2_when_2_is_passed():
	check_fizzbuzz("2", "2")
def test_returns_fizz_when_3_is_passed():
	check_fizzbuzz("3", "Fizz")
def test_returns_buzz_when_5_is_passed():
	check_fizzbuzz('5', 'Buzz')
def test_returns_fizz_when_6_is_passed():
	check_fizzbuzz('6', 'Fizz')
def test_returns_buzz_when_10_is_passed():
	check_fizzbuzz('10', 'Buzz')
def test_returns_buzz_when_15_is_passed():
	check_fizzbuzz('15', 'FizzBuzz')