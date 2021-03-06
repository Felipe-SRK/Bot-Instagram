from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\USER\OneDrive\Área de Trabalho\geckodriver.exe"
        )

    def login(self):
        driver = self.driver
        driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher'")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(3)
        self.comente_nas_fotos_com_a_hashtag(
            ""
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        #driver.get("https://www.instagram.com/p/CN-_cOCoXJ6/")#Sorteio PC
        #driver.get("https://www.instagram.com/p/CNxXVgjHYtG/")#Sorteio Switch
        #driver.get("https://www.instagram.com/p/COS1yvhjoLG/")#Sorteio PS4
        
        time.sleep(2)

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "Eu quero",
                ]  # Remova esses comentários e insira os seus comentários aqui
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 5))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                time.sleep(random.randint(3, 5))
            except Exception as e:
                print(e)
                time.sleep(2)


# Entre com o usuário e senha aqui
felipebot = InstagramBot("usuarui", "senha")
felipebot.login()
