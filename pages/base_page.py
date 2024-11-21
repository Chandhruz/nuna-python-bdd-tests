from selenium import webdriver
from time import sleep
from resources import config


class DriverManager:
    def __init__(self, driver):
        self.driver = driver

    def launch_browser_and_navigate(url, wait_time=10):
        if config.Config.BROWSER== "Chrome":
            driver = webdriver.Chrome()  # Initialize WebDriver (you may adjust this as needed)
            driver.get(url)  # Navigate to the provided URL
            # driver.maximize_window()  # Maximize the browser window
            # sleep(wait_time)  # Wait for the specified time (in seconds) for the page to load
            return driver