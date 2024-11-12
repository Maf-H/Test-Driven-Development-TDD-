from pytest import approx, raises

def test_string_equality():
	assert "TDD" == "TDD"
def test_integer_equality():
	assert 42 == 42
def test_float_equality():
	assert 1.5 == 1.5
def test_list_equality():
	assert [1, 2, 3] == [1, 2, 3]
def test_dict_equality():
	assert {"a": 1, "b": 2, "c": 3} == {"a": 1, "b": 2, "c": 3}
def test_float_sum_approx_equality():
	assert (1/3 + 1/3 + 1/3) == approx(1.0)
def test_float_sum_equality():
	assert (1/3 + 1/3 + 1/3) == 1.0

def raises_value_exception():
	raise ValueError
def test_raises_exception():
	with raises(ValueError):
		raises_value_exception()