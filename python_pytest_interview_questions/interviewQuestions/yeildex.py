import pytest

@pytest.fixture
def sample_data():
    print("\n Setup: Creating test data")
    data = {"name": "Alice", "age": 30}
    yield data
    print("Cleaning up testdata")

#piece of code that comes after yield statement is the tear down code


def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed successfully with sample data:", sample_data)



    # fixtures will execute first before and executing the testcase

#How do you use yield for webdriver setup and teardown in pytest?
# before yield statement we write the setup code like browser invocation, db connection setup, etc and after 
# yield statement we write the teardown code like browser close, db connection close, teardown, etc