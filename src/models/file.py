import csv
import os

class File:
    @staticmethod
    def read_csv(path):
        try:
            with open(path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                return [row for row in csv_reader]
        except IOError:
            raise IOError(f'File not exist or not acessible. {path}')
