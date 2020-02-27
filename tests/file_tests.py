import unittest
import os

from src.models.file import File

CSV_FOLDER = os.path.join(os.path.dirname(__file__), 'csv')

class TestFile(unittest.TestCase):

    def test_with_valid_path(self):
        rows = File.read_csv(f'{CSV_FOLDER}/accounts.csv')
        self.assertTrue(rows)

    def test_with_invalid_path(self):
        with self.assertRaises(IOError):
            File.read_csv(f'{CSV_FOLDER}/accounts_t.csv')
