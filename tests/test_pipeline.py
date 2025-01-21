# process1.process


import sys
import os

import importlib.util 
cwd = os.getcwd()
print('cwd : ' +str(cwd))
parent_dir = cwd
# parent_dir = os.path.dirname(cwd)
# print('parent dir: '+ str(parent_dir))
print('chcek if we are table to find the parent dir of cwd')
abs_pipeline_path = str(parent_dir)+ '/scripts' + '/pipeline.py'
print(abs_pipeline_path)


spec = importlib.util.spec_from_file_location("pipeilne", abs_pipeline_path) 
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

my_module = module




import pytest
# from scripts.pipeline import process_data  # Import the function to be tested


@pytest.fixture
def sample_input():
    """Fixture to provide sample input data."""
    return {"key1": "value1", "key2": "value2"}


@pytest.fixture
def expected_output():
    """Fixture to provide the expected output data."""
    return {"key1": "VALUE1", "key2": "VALUE2"}


def test_process_data(sample_input, expected_output):
    """Test the process_data function."""
    result = my_module.process_data(sample_input)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
