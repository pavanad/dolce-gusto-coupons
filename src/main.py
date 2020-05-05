# -*- coding: utf-8 -*-

import argparse
import csv
import time
from secrets import DOLCE_PASSWORD, DOLCE_USERNAME

from coupons import get_coupons_from_csv_file
from selenium import webdriver


def open_browser():
    print("open browser and login in system")
    url = "https://www.nescafe-dolcegusto.com.br/"
    browser = webdriver.Firefox()
    browser.get(url)

    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    username.send_keys(DOLCE_USERNAME)
    password.send_keys(DOLCE_PASSWORD)
    browser.find_element_by_id("send2").click()
    browser.find_element_by_link_text("Meu Bônus").click()
    time.sleep(3)

    return browser


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv", help="path to csv file with coupons")
    ap.add_argument("-i", "--images", help="path to images files for detect coupons")
    args = vars(ap.parse_args())

    if args["csv"] is None and args["images"] is None:
        print("error: path do csv file or images files is required.")
        return

    try:
        if args["csv"] is not None:
            print("get coupons from csv file")
            coupons = get_coupons_from_csv_file(args["csv"])
        elif args["images"] is not None:
            # TODO: implement get coupons from images
            pass

        # open browser and login
        browser = open_browser()

        for coupon in coupons:
            print(f"enter coupon {coupon}")
            coupon_code = browser.find_elements_by_id("coupon_code")
            save_button = browser.find_elements_by_css_selector(
                '.button[value="Salvar"]'
            )
            coupon_code[0].send_keys(coupon)
            save_button[0].click()
            time.sleep(2)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
