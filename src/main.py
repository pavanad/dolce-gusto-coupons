# -*- coding: utf-8 -*-

import argparse
import time
from secrets import DOLCE_PASSWORD, DOLCE_USERNAME

from colorama import Fore

from coupons import get_coupons_from_csv_file, get_coupons_from_images
from services import open_browser


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv", help="path to csv file with coupons")
    ap.add_argument("-i", "--images", help="path to images files for detect coupons")

    args = vars(ap.parse_args())
    message_status = f"> {Fore.CYAN}[dolce-gusto-coupons]{Fore.RESET}"

    try:
        if args["csv"] is None and args["images"] is None:
            raise Exception("Path do csv file or images files is required.")

        print(f"\n{message_status} Starting...")
        if args["csv"] is not None:
            print(f"{message_status} Get coupons from csv file")
            coupons = get_coupons_from_csv_file(args["csv"])
        elif args["images"] is not None:
            print(f"{message_status} Get coupons from images")
            coupons = get_coupons_from_images(args["images"])

        # open browser and login
        print(f"{message_status} Opening the browser and accessing the system")
        browser = open_browser()

        for coupon in coupons:
            print(f"{message_status} Applying the coupon {coupon}")
            coupon_code = browser.find_elements_by_id("coupon_code")
            save_button = browser.find_elements_by_css_selector(
                '.button[value="Salvar"]'
            )
            coupon_code[0].send_keys(coupon)
            save_button[0].click()
            time.sleep(2)

        print(f"{message_status} {Fore.GREEN}Done{Fore.RESET}\n")

    except Exception as error:
        print(f"\n{message_status} {Fore.RED}{str(error)}{Fore.RESET}\n")


if __name__ == "__main__":
    main()
