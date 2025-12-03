from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_setup import setup_driver
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED

#AGREGA EL PRIMER PRODUCTO Y VALIDA

def test_nav_ver():
    driver = setup_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # login
    login.login(USUARIO_PRED, PASS_PRED)

    # valida titulo
    titulo = inventory.obtener_titulo()
    assert titulo == "Products", f"Título incorrecto: {titulo}"

    # lista
    productos = inventory.obtener_lista_productos()
    assert len(productos) > 0, "No se encontraron productos en el catálogo"

    # obtener nombre y precio
    primer_nombre = inventory.obtener_nombre_producto(0)
    primer_precio = inventory.obtener_precio_producto(0)

    print(f"Primer producto -> Nombre: {primer_nombre}  |  Precio: {primer_precio}")

    driver.quit()
