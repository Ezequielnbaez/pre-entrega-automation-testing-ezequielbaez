from utils.config import BASE_URL, TIEMPO_DE_ESPERA
from utils.data_utils import leer_usaurios

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.common.exceptions import TimeoutException

#LOGIN A PARTIR DE DATOS EN CARPETA "datos" en JSON
def test_login_multiple(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    usuarios = leer_usaurios()

    driver.get(BASE_URL)

    for usuario in usuarios:

        login.limpiar_campos()

        # intentar login
        login.login(usuario["usuario"], usuario["password"])

        try:
            inventory.esperar_catalogo(TIEMPO_DE_ESPERA)
            print(f"✔ Usuario '{usuario['usuario']}' logró entrar")

            # volver al inicio para siguiente usuario
            driver.get(BASE_URL)

        except TimeoutException:
            # fallo de login
            error = login.obtener_error()
            if error:
                print(f"❌ Usuario '{usuario['usuario']}' falló login: {error}")
            else:
                print(f"❌ Usuario '{usuario['usuario']}' falló login (sin mensaje detectable)")
