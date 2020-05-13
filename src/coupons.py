# -*- coding: utf-8 -*-

import csv
import os

import pytesseract
from PIL import Image


def get_coupons_from_csv_file(filename: str):
    if not os.path.exists(filename):
        raise Exception("error: csv file not found")
    with open(filename) as csv_file:
        rows = csv.reader(csv_file, delimiter=";")
        for row in rows:
            yield row[0]


def get_coupons_from_images(images_path: str):
    if not os.path.exists(images_path):
        raise Exception("error: images path not found")

    image_types = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

    for (root_dir, dir_names, filenames) in os.walk(images_path):
        for filename in filenames:
            extension = filename[filename.rfind(".") :].lower()
            if extension.endswith(image_types):
                image_path = os.path.join(root_dir, filename)
                cupom_code = pytesseract.image_to_string(Image.open(image_path))
                yield cupom_code.replace(" ", "")
