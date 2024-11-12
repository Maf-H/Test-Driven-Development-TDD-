import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_session():
	print("\nSetUp session")

@pytest.fixture(scope="module", autouse=True)
def setup_module():
	print("\nSetUp module")

@pytest.fixture(scope="function", autouse=True)
def setup_function():
	print("\nSetUp function")

def test_1():
	print("Executing test_1...")
	assert True
def test_2():
	print("Executing test_2...")
	assert True
