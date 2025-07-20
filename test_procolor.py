# test_procolor.py
"""
Tests for ProColor module.
"""

import unittest
from procolor import ProColor

class TestProColor(unittest.TestCase):
    """Test cases for ProColor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProColor()
        self.assertIsInstance(instance, ProColor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProColor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
