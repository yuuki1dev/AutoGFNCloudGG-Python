import requests
import bs4
import logging
from random import choice

RANDOM_NAME_RANGE = "abcdefghijklmnopqrstuvwxyz0123456789"
MAIL_DOMAIN = "@mailforspam.com"

logger: logging.Logger = logging.getLogger("utils.mail")

mail_prefix: str = ""


class Mail():
    currentMailUsername: str = None
    currentActivateLink: str = None
    

    def get_current_email(self) -> str:
        return self.currentMailUsername + MAIL_DOMAIN

    
    def generate(self) -> str:
        _new: str = mail_prefix
        for i in range(6): _new += choice(RANDOM_NAME_RANGE)
        self.currentMailUsername = _new
        logger.debug(f"New email generated: {self.get_current_email()}")
        return _new
    

    def get_activate_link(self) -> str:
        pass
