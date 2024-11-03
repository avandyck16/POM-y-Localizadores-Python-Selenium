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

    def set_email(self,email):
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

## ======================== Clase para la página principal ======================== ##

class HomePageAround:
    profile_description = (By.CLASS_NAME, 'profile__description')

    def __init__(self,driver):
        self.driver = driver

    def wait_for_descr_visible(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.profile_description))

    def obtain_description_value(self):
        return self.driver.find_element(*self.profile_description).text
        ## Se espera que diga "Explorer"

#        actual_value = self.driver.find_element(*self.profile_description).text
#        expected_value = 'explorer'
#        assert actual_value == expected_value


## ======================== Clase para las pruebas ======================== ##

class TestPageAround:
    #driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')

    def test_login_at_login_page(self):
        self.login_page = LoginPageAround(self.driver)
        self.login_page.login('some@gmail.com','passwd')

    def test_check_profile_descr_value(self):
       self.home_page = HomePageAround(self.driver)
       self.home_page.wait_for_descr_visible()
       self.home_page.obtain_description_value()
       expected_text = 'Explorer'
       #print(f'Prueba 2: Texto Actual: "{self.home_page.obtain_description_value()}", Esperado:  "{expected_text}"')
       assert self.home_page.obtain_description_value() == expected_text


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()




