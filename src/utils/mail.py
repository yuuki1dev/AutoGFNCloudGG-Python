import requests
import bs4
import logging
from random import choice

RANDOM_NAME_RANGE = "abcdefghijklmnopqrstuvwxyz0123456789"
MAIL_DOMAIN = "@mailforspam.com"

logger: logging.Logger = logging.getLogger("utils.mail")

mail_prefix: str = ""


class Mail():
    current_username: str = None
    current_activate_link: str = None
    

    def get_current_email(self) -> str:
        return self.current_username + MAIL_DOMAIN

    
    def generate(self) -> str:
        _new: str = mail_prefix
        for i in range(6): _new += choice(RANDOM_NAME_RANGE)
        self.currentMailUsername = _new
        logger.debug(f"New email generated: {self.get_current_email()}")
        return _new
    

    def request(self, index: int = None) -> str:
        url = f"https://mailforspam.com/mail/{self.current_username}/{index if index is not None else ''}"
        logger.debug("Sending request to " + url)
        resp: requests.Response = requests.get()
        logger.debug(f"Request completed. Code: {resp.status_code}")
        if resp.status_code != 200: raise requests.exceptions.HTTPError("Failed to get request response data.")
        return resp.text
    

    def get_activate_link(self) -> str:
        pass


def parse_mail_list(mail_obj: Mail):
    data = mail_obj.request()
    parser = bs4.BeautifulSoup(data)
    for element in parser.select("a"):
        pass