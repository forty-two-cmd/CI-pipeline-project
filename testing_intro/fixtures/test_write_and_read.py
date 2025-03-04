import pytest
import os

@pytest.fixture
def output_file():
    filename = "example"
    yield filename
    os.remove(filename)

def test_create(output_file):
    from write_and_read import create_empty_file

    create_empty_file(output_file)
    assert os.path.exists(output_file)

@pytest.fixture
def input_file():
    filename = "example"
    file = open(filename, "w")
    file.write("This is an example file")
    file.close()
    yield filename
    os.remove(filename)

def test_read(input_file):
    from write_and_read import read_file

    file_content = read_file(input_file)
    assert file_content == "This is an example file"


## 1. create_empty_file creates a file called "example" in the folder fixtures
##    the fixture output_file removes the file after yielding the filename to the testing function
## 2. the fixture input_file initially only returns a filename. It doesn't create a file with the appropriate content
## 