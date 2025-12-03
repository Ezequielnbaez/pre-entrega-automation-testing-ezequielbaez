from utils.selenium_func import escribir_text, click_elemento, obtener_texto, esperar_visibilidad
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#DECIDÍ MANTENER EL USO DE LAS FUNCIONES DE UTILS SIGUIENDO EL POM, PARA REUTILIZAR CÓDIGO


class LoginPage:
    LOC_USER = ("id", "user-name")
    LOC_PASS = ("id", "password")
    LOC_BTN_LOGIN = ("id", "login-button")
    LOC_ERROR_MSG = ("css selector", "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, usuario, password):
        escribir_text(self.driver, self.LOC_USER, "")
        escribir_text(self.driver, self.LOC_PASS, "")

        escribir_text(self.driver, self.LOC_USER, usuario)
        escribir_text(self.driver, self.LOC_PASS, password)

        click_elemento(self.driver, self.LOC_BTN_LOGIN)

    def limpiar_campos(self):
        esperar_visibilidad(self.driver, self.LOC_USER)
        user = self.driver.find_element(*self.LOC_USER)
        password = self.driver.find_element(*self.LOC_PASS)

        user.clear()
        password.clear()

    def obtener_error(self):
        try:
            return obtener_texto(self.driver, self.LOC_ERROR_MSG)
        except (TimeoutException, NoSuchElementException):
            return None
        
