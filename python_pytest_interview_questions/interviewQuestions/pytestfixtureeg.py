import pytest

@pytest.fixture
def sample_data():
    print("\n Setup: Creating test data")
    data = {"name": "Alice", "age": 30}
    return data

#browser instantiation is added in fixture and it will be executed first before executing the testcase


@pytest.mark.sanity
def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed successfully with sample data:", sample_data)

    # fixtures will execute first before and executing the testcase
#How do you use yield for webdriver setup and teardown in pytest?