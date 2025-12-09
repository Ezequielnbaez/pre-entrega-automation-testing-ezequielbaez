
from utils.config import BASE_URL, TIEMPO_DE_ESPERA
from utils.data_utils import leer_usaurios
from utils.logger import logger
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.common.exceptions import TimeoutException

#LOGIN A PARTIR DE DATOS EN CARPETA "datos" en JSON
def test_login_multiple(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    usuarios = leer_usaurios()

    logger.info("Iniciando test_login_multiple")
    driver.get(BASE_URL)
    logger.info(f"Abrí la URL: {BASE_URL}")

    for usuario in usuarios:
        user = usuario["usuario"]
        login.limpiar_campos()

        logger.info(f"Intentando login con usuario: {user}")
        login.login(usuario["usuario"], usuario["password"])

        try:
            inventory.esperar_catalogo(TIEMPO_DE_ESPERA)

            logger.info(f"Usuario '{user}' logro entrar correctamente")
            logger.info("Volviendo a la página principal para probar siguiente usuario")

            driver.get(BASE_URL)

        except TimeoutException:
            #fallo de login
            error = login.obtener_error()
            if error:
                print(f"Usuario '{usuario['usuario']}' falló login: {error}")
            else:
                print(f"Usuario '{usuario['usuario']}' falló login")
