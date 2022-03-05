"""A module to understand unit tests"""
import unittest
import os
from unit_test_02 import analyze_text


class TextAnalyzerTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war,\n' 
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n' 
                    'can long endure.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except OSError:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """test that line count is OK"""
        file_length, _ = analyze_text(self.filename)
        self.assertEqual(file_length, 4)

    def test_character_count(self):
        """Test that the character count is ok"""
        _, character_count = analyze_text(self.filename)
        self.assertEqual(character_count, 131)

    def test_file_not_exists(self):
        """Tests that the function raises an exception when the file does not exist"""
        with self.assertRaises(IOError):  # Context manager!
            analyze_text("not_a_file")


# setUp does the pre-processing, tearDown does the post-processing


if __name__ == '__main__':
    unittest.main()
