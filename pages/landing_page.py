from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from pages.base_page import DriverManager
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(DriverManager):
    def __init__(self, driver):
        super().__init__(driver)

    def click_accept_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-amgdprcookie-js='accept']"))
            )
            # ActionChains(self.driver).click(button).perform()
            button.click()
            # button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for ACCEPT button to be clickable.")
            return False
        except NoSuchElementException:
            print("ACCEPT button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the ACCEPT button and intercepting the click.")
            return False
        
    def click_all_products_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-menu-item a[href*='/all-products']"))
            )
            ActionChains(self.driver).click(button).perform()
            # button.click
            return True
        except TimeoutException:
            print("Timed out waiting for SHOP-NOW button to be clickable.")
            return False
        except NoSuchElementException:
            print("SHOP-NOW button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the SHOP-NOW button and intercepting the click.")
            return False

    def click_on_dupree_product(self):
        try:
            self.driver.maximize_window()
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-item-info_96"))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for dupree product")
            return False
        except NoSuchElementException:
            print("dupree product not found")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the dupree product button and intercepting the click.")
            return False

    def click_add_to_basket(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-addtocart-button')))
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for ADD-TO-CART button to be clickable.")
            return False
        except NoSuchElementException:
            print("ADD-TO-CART button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the ADD-TO-CART button and intercepting the click.")
            return False

    def click_basket(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='page messages'] a[href*='checkout/cart']"))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CLICK-BASKET button 2 to be clickable.")
            return False
        except NoSuchElementException:
            print("CONTINUE button 2 not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CLICK-BASKET button and intercepting the click.")
            return False

    def click_proceed_to_checkout_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-role='proceed-to-checkout']"))
            )
            ActionChains(self.driver).click(button).perform()
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CHECKOUT button to be clickable.")
            return False
        except NoSuchElementException:
            print("CHECKOUT button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CHECKOUT button and intercepting the click.")
            return False

    def enter_email(self):
        try:
            emailTextBox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-role='email-with-possible-login'] input#customer-email"))
            )
            emailTextBox.send_keys("testuser@nuna.com")
            return True
        except TimeoutException:
            print("Timed out waiting for EMAIL-TEXTBOX to be clickable.")
            return False
        except NoSuchElementException:
            print("EMAIL-TEXTBOX not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the EMAIL-TEXTBOX and intercepting the click.")
            return False