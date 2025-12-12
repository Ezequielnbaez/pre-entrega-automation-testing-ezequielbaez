from utils.selenium_func import escribir_text, click_elemento, esperar_visibilidad
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException, NoSuchElementException

#DECIDÍ MANTENER EL USO DE LAS FUNCIONES DE UTILS SIGUIENDO EL POM, PARA REUTILIZAR CÓDIGO


class CheckoutPage:
    LOC_FIRSTNAME = ("id", "first-name")
    LOC_LASTNAME = ("id", "last-name")
    LOC_ZIPCODE = ("id", "postal-code")
    LOC_CONTINUE_BTN = ("id", "continue")
    LOC_FINISH_BTN = ("id", "finish")
    LOC_MENSAJE_FINAL = ("class name", "complete-header")


    def __init__(self, driver):
        self.driver = driver

    def completar_formulario(self, nombre, apellido, codigo):
        #espero porque github tiene computadora lenta parece
        WebDriverWait(self.driver, 10).until(EC.url_contains("checkout-step-one.html"))
        escribir_text(self.driver, self.LOC_FIRSTNAME, nombre)
        escribir_text(self.driver, self.LOC_LASTNAME, apellido)
        escribir_text(self.driver, self.LOC_ZIPCODE, codigo)
        click_elemento(self.driver, self.LOC_CONTINUE_BTN)
        WebDriverWait(self.driver, 10).until(EC.url_contains("checkout-step-two.html"))

    def finalizar_compra(self):
        click_elemento(self.driver, self.LOC_FINISH_BTN)

    def obtener_mensaje_final(self):
        esperar_visibilidad(self.driver, self.LOC_MENSAJE_FINAL)
        elemento = self.driver.find_element(*self.LOC_MENSAJE_FINAL)
        return elemento.text    