from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPageAround:
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    reg_button = (By.CLASS_NAME, "auth-form__button")

    def __init__(self,driver):
        self.driver = driver

    def set_email(self,mail):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'email')))
        self.driver.find_element(*self.email).send_keys(mail)

    def set_password(self,passwd):
        self.driver.find_element(*self.password).send_keys(passwd)

    def register(self,mail,passwd):
        self.set_email(mail)
        self.set_password(passwd)
        self.driver.find_element(*self.reg_button).click()


class TestRegistrationPageAround:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://around-v1.nm.tripleten-services.com/signup')
        cls.page = RegistrationPageAround(cls.driver)

    def test_register(self):
        self.page.register('mail@example.com','passwords')


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

