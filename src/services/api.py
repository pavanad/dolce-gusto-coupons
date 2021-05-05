import requests
from bs4 import BeautifulSoup


class DolceGustoClient:

    BASE_URL = "https://www.nescafe-dolcegusto.com.br"

    def __init__(self, username: str = None, password: str = None) -> None:
        self.__username = username
        self.__password = password
        self.__session = requests.Session()
        self.__cookies = self.__get_cookies()

    def __get_cookies(self):
        url = f"{self.BASE_URL}/customer/account/login/referer/aHR0cHM6Ly93d3cubmVzY2FmZS1kb2xjZWd1c3RvLmNvbS5ici8%2C/"
        response = self.__session.get(url, headers=self.__get_header())
        soup = BeautifulSoup(response.content, features="html.parser")

        form = soup.find("form", {"id": "login-form"})
        fields = form.findAll("input")
        form_data = dict((field.get("name"), field.get("value")) for field in fields)

        return {
            "PHPSESSID": requests.utils.dict_from_cookiejar(self.__session.cookies)[
                "PHPSESSID"
            ],
            "form_key": form_data["form_key"],
        }

    def __get_header(self) -> dict:
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
            "Referer": "https://www.nescafe-dolcegusto.com.br//",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.nescafe-dolcegusto.com.br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers",
        }

    def authenticate(self) -> bool:
        """Authenticates to the api."""
        url = f"{self.BASE_URL}/customer/account/loginPost/referer/aHR0cHM6Ly93d3cubmVzY2FmZS1kb2xjZWd1c3RvLmNvbS5ici8%2C/"
        credentials = {
            "form_key": self.__cookies["form_key"],
            "login[username]": "adilson.pavan@gmail.com",
            "login[password]": "eqcmm78",
            "send": "",
        }
        authenticated = False
        response = self.__session.post(
            url, headers=self.__get_header(), cookies=self.__cookies, data=credentials
        )

        # update cookies after authentication
        if response.status_code == 200:
            authenticated = True
            cookie_json = self.__session.cookies.get_dict()
            self.__cookies = {
                "form_key": cookie_json["form_key"],
                "PHPSESSID": cookie_json["PHPSESSID"],
            }
        return authenticated

    def send_coupon(self, code: str) -> int:
        url = f"{self.BASE_URL}/reward/customer/pcm/"
        data = {"form_key": self.__cookies["form_key"], "code": code}
        response = self.__session.post(
            url, headers=self.__get_header(), cookies=self.__cookies, data=data
        )
        return response.status_code
