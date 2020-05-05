import csv
import os


def get_coupons_from_csv_file(filename: str):
    if not os.path.exists(filename):
        raise Exception("error: csv file not found")

    with open(filename) as csv_file:
        rows = csv.reader(csv_file, delimiter=";")
        for row in rows:
            yield row[0]
