from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

## ======================== Clase para la página de inicio de sesión ======================== ##
class LoginPageAround:
    email_field = (By.ID, 'email')
    pass_field = (By.ID, 'password')
    login_button = (By.CLASS_NAME, 'auth-form__button')

    def __init__(self,driver):
        self.driver = driver

    def set_email(self, email):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'email')))
        self.driver.find_element(*self.email_field).send_keys(email)


    def set_password(self, password):
        self.driver.find_element(*self.pass_field).send_keys(password)


    def click_sign_in_button(self):
        self.driver.find_element(*self.login_button).click()


    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

## ======================== Clase para la página con el header ======================== ##

class HeaderPageAround:
    header = (By.CLASS_NAME, "header page__section")
    user_header = (By.CLASS_NAME, 'header__user')

    def __init__(self,driver):
        self.driver = driver

    def wait_for_header_visibility(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.user_header))

    def check_user_header_is_visible(self):
       self.driver.find_element(*self.user_header).is_displayed()

    def check_email_in_header(self):
        return self.driver.find_element(*self.user_header).text

        # Se espera que sea == email en llenar el email.
        # En la prueba, accede a esta funcion y la guardaré en una variable



## ======================== Clase para las pruebas ======================== ##

class TestPageAround:
    @classmethod

    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_login_and_header(self):
        self.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
        email = 'user@mail.com'
        password = 'passwd'
        LoginPageAround(self.driver).login(email,password)
        ## ESTAMOS ENTRANDO A LA CLASE QUE CONTIENE LAS FUNCIONES, NO CREANDO UN OBJETO ##

        ## ================================================== ##
        HeaderPageAround(self.driver).wait_for_header_visibility()
        HeaderPageAround(self.driver).check_user_header_is_visible()
        text_in_header = HeaderPageAround(self.driver).check_email_in_header()
        assert text_in_header == email




