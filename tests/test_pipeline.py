import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

import unittest
# from scripts.pipeline import process_data

from .scripts.pipeline import process_data

class TestPipeline(unittest.TestCase):
    def test_process_data(self):
        # Add your test logic here
        print("Testing data processing...")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
