# -*- coding: utf-8 -*-

import argparse
import time
from secrets import DOLCE_PASSWORD, DOLCE_USERNAME

from colorama import Fore

from coupons import get_coupons_from_csv_file, get_coupons_from_images
from services.api import DolceGustoClient


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv", help="path to csv file with coupons")
    ap.add_argument("-i", "--images", help="path to images files for detect coupons")

    args = vars(ap.parse_args())
    message_status = f"> {Fore.CYAN}[dolce-gusto-coupons]{Fore.RESET}"

    try:
        if args["csv"] is None and args["images"] is None:
            raise Exception("Path of the csv file or images files is required.")

        print(f"\n{message_status} Starting...")
        if args["csv"] is not None:
            print(f"{message_status} Get coupons from csv file")
            coupons = get_coupons_from_csv_file(args["csv"])
        elif args["images"] is not None:
            print(f"{message_status} Get coupons from images")
            coupons = get_coupons_from_images(args["images"])

        # connect to the API client
        print(f"{message_status} Connecting to the Dolce Gusto API")
        client = DolceGustoClient(username=DOLCE_USERNAME, password=DOLCE_PASSWORD)
        client.authenticate()

        for coupon in coupons:
            if not coupon:
                print(
                    f"{message_status} {Fore.RED}Coupon not found in file{Fore.RESET}"
                )
                continue

            client.send_coupon(coupon)
            print(f"{message_status} Applying the coupon {coupon}")
            time.sleep(0.5)

        print(f"{message_status} {Fore.GREEN}Done{Fore.RESET}\n")

    except Exception as error:
        print(f"\n{message_status} {Fore.RED}{str(error)}{Fore.RESET}\n")


if __name__ == "__main__":
    main()
