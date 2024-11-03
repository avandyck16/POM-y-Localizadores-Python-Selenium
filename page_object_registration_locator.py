from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class LoginPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Iniciar sesión
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # Agrega aquí un localizador para el botón Registrarse
    register_button = (By.CLASS_NAME, 'header__auth-link')



    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'email')))

    # El metodo comprueba si se puede hacer clic en el botón Iniciar sesión
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.sign_in_button).is_enabled()

    # El metodo hace clic en el botón Iniciar sesión
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # El metodo valida el texto en el botón Registrarse
    def check_text_registration_button(self):
        registration_button_text = self.driver.find_element(*self.register_button).text
        expected = "Registrarse"
        assert registration_button_text == expected, f'El texto del botón no coincide con {expected}'

    # El metodo hace clic en el botón Registrarse
    def click_registration_button(self):
        self.driver.find_element(*self.register_button).click()
        assert self.driver.current_url == 'https://around-v1.nm.tripleten-services.com/signup'


class TestLoginPageAround:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
        cls.page = LoginPageAround(cls.driver)

    def test_check_button_enabled(self):
        self.page.check_sign_in_is_enabled()

    def test_click_on_signin(self):
        self.page.click_sign_in_button()

    def test_check_text_on_button(self):
        self.page.check_text_registration_button()

    def test_click_registration(self):
        self.page.click_registration_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


