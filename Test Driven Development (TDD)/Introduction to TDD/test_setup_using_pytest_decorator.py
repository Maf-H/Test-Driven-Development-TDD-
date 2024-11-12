import pytest

@pytest.fixture(autouse=True)
def setup():
	print("\nSetup")


def test_1():
	print("Test 1 Executing...")
	assert True
def test_2():
	print("Test 2 Executing...")
	assert True