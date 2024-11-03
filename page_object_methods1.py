import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# Agregar una nueva publicacion
# Login

class PageAround:
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    login_button = (By.CLASS_NAME, 'auth-form__button')
    add_new_button = (By.CLASS_NAME, 'profile__add-button')
    place_name = (By.NAME, 'name')
    place_link = (By.NAME, 'link')
    save_button = (By.XPATH, ".//form[@name='new-card']/button[text()='Save']")
    pic_descr = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]/h2')

    def __init__(self,driver):
        self.driver = driver

    def login_to_page(self,mail,passwd):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'email')))
        self.driver.find_element(*self.email).send_keys(mail)
        self.driver.find_element(*self.password).send_keys(passwd)
        self.driver.find_element(*self.login_button).click()

    def add_new_place(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/ul')))
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[1]')))
        self.driver.find_element(*self.add_new_button).click()
        self.driver.find_element(*self.place_name).send_keys("Новое место")
        self.driver.find_element(*self.place_link).send_keys('https://concepto.de/wp-content/uploads/2015/03/paisaje-e1549600034372.jpg')
        self.driver.find_element(*self.save_button).click()


    def check_cards(self):
       #wait 1
       WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/ul')))
       #wait 2
       WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
           (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]/h2')))

       #wait 3
       expected = "Новое место"
       WebDriverWait(self.driver,5).until(
           expected_conditions.text_to_be_present_in_element((By.XPATH,'//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]/h2'),expected))

       pic_text = self.driver.find_element(*self.pic_descr).text
       assert expected == pic_text, f'El texto no coincide'


class TestPageAround:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=en')
        cls.page = PageAround(cls.driver)

    def test_login(self):
        self.page.login_to_page('some@gmail.com','passwd')

    def test_add_new(self):
        self.page.add_new_place()

    def test_check_card_added(self):
        self.page.check_cards()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



