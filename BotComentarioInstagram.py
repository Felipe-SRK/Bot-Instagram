from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="./Users/felipesilva/Downloads/geckodrive/"
                                        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

felipebot = InstagramBot("fe_srk", "fs210698")
felipebot.login()
