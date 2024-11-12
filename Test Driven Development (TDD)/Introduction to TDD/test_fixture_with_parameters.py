import pytest

@pytest.fixture(params=[1, 2, 3])
def setup(request):
	return_value = request.param
	print(f"\nSetup returned value {return_value}")
	return return_value

def test_1(setup):
	print(f"Setup {setup}")