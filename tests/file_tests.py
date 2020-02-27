import unittest

from src.models.file import File


class TestFile(unittest.TestCase):

    def test_with_valid_path(self):
        rows = File.read_csv(
            'C:\\Users\\DataInfo\\Documents\\projetos\\Rispar\\rispar\\tests\\csv\\accounts.csv')
        self.assertTrue(rows)

    def test_with_invalid_path(self):
        with self.assertRaises(IOError):
            File.read_csv(
                'C:\\Users\\DataInfo\\Documents\\projetos\\Rispar\\rispar\\tests\\csv\\accounts_t.csv')
