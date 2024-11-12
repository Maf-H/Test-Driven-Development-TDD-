import pytest

@pytest.fixture(scope = "module", autouse = True)
def setup_module_2():
	print("\nSetUp module")

@pytest.fixture(scope = "function", autouse = True)
def setup_function_2():
	print("\nSetUp function")
@pytest.fixture(scope = "class", autouse = True)
def setup_class():
	print("\nSetUp class")

class TestClass:
	def test_3(self):
		print("Executing test_3...")
		assert True

	def test_4(self):
		print("Executing test_4...")
		assert True
