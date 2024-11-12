import pytest
@pytest.fixture()
def setup_1():
	print("\nSetup")
	yield
	print("\nTeardown")
@pytest.fixture()
def setup_2(request):
	print("\nSetup")

	def teardown_1():
		print("\nTeardown")

	def teardown_2():
		print("\nTeardown")
	request.addfinalizer(teardown_1)
	request.addfinalizer(teardown_2)

def test_1(setup_1):
	print("Test 1 Executing...")
	assert True
def test_2(setup_2):
	print("Test 2 Executing...")
	assert True