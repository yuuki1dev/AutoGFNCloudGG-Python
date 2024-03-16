import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import logging
from time import sleep


logger: logging.Logger = logging.getLogger("utils.driver")

chromeOptions: uc.ChromeOptions = uc.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--window-size=800,600")
chromeOptions.add_argument("--disable-popup-blocking")

class Driver():
    driver: uc.Chrome = uc.Chrome(chromeOptions)

    def wait_redirect(self, destination: str) -> None:
        logger.debug(f"Driver is waiting for redirect to {destination}")
        countdown: int = 120
        while self.driver.current_url != destination:
            if countdown < 0:
                logger.warn(f"Waiting for redirect to {destination} timed out.")
                break
            countdown -= 1
            sleep(1)
        
        if destination not in self.driver.current_url:
            raise RuntimeError(f"Cannot reach {destination} after 120 seconds!")
            
    
    def element(self, cssSelector: str) -> uc.webelement.WebElement:
        return self.driver.find_element(By.CSS_SELECTOR(cssSelector))
    

    def wait_sendkeys(self, cssSelector: str, keys: str) -> None:
        pass