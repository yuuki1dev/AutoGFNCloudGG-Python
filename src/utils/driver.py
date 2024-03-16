import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from time import sleep


logger: logging.Logger = logging.getLogger("utils.driver")

chromeOptions: uc.ChromeOptions = uc.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--window-size=800,600")
chromeOptions.add_argument("--disable-popup-blocking")

class DriverController():
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
        
    def navigate(self, url: str):
        self.driver.get(url)
        WebDriverWait(self.driver, 20).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            
    
    def find_element(self, css_selector: str) -> uc.webelement.WebElement:
        return self.driver.find_element(By.CSS_SELECTOR(css_selector))
    

    def wait_element(self, css_selector) -> uc.webelement.WebElement:
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


    def wait_sendkeys(self, css_selector: str, keys: str) -> None:
        self.wait_element(css_selector).send_keys(keys)

    
    def wait_click(self, css_selector: str, waitSeconds: int = 10) -> None:
        element = WebDriverWait(self.driver, waitSeconds).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        self.driver.execute_script("arguments[0].click();", element)


    def scroll_to(self, css_selector: str) -> None:
        element = self.wait_element(css_selector)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def wait_select(self, css_selector: str, option_value: str) -> None:
        Select(self.wait_element(css_selector)).select_by_value(option_value)