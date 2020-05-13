# Dolce Gusto Coupons

Automatic coupon filling tool on the Dolce Gusto Brazil website.

This is a simple implementation just to "play" with the selenium and OCR pytesseract features.

## Install requirements

**Install Tesseract 4 on macOS**

```bash
brew install tesseract --HEAD
```

**Install Tesseract 4 on Ubuntu**

For Ubuntu 18.04 users, Tesseract 4 is part of the main apt-get repository, making it super easy to install Tesseract via the following command:

```bash
sudo apt install tesseract-ocr
```

**Python dependencies**

```bash
poetry install

# or with pip
pip install -r requirements.txt
```

## How to use

**Credentials**

Set your email and password in the **secrets.py** file

**Coupon Codes with CSV**

Fill out a list of coupons in a csv file and run the script with the parameters below:

```bash
python main.py --csv coupons/data.csv
```

**Coupon Codes with images**

Take pictures of all coupons, save to a folder and run the script with the parameters below:

```bash
python main.py --images coupons/images/
````
