# process1.process


import sys
import os

import importlib.util 
cwd = os.getcwd()
print('cwd : ' +str(cwd))

parent_dir = os.path.dirname(cwd)
print('parent dir: '+ str(parent_dir))
print('chcek if we are table to find the parent dir of cwd')
abs_pipeline_path = str(parent_dir)+ '/scripts' + '/pipeline.py'
print(abs_pipeline_path)


spec = importlib.util.spec_from_file_location("pipeilne", abs_pipeline_path) 
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

my_module = module






# my_module
import unittest
# from scripts.pipeline import process_data

from .scripts.pipeline import process_data

class TestPipeline(unittest.TestCase):
    def test_process_data(self):
        # Add your test logic here
        result = my_module.process_data() 
        print("Testing data processing...")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
