from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED

#AGREGA EL PRIMER PRODUCTO Y VALIDA
def test_nav_ver(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Login
    login.login(USUARIO_PRED, PASS_PRED)

    # Validar título
    titulo = inventory.obtener_titulo()
    assert titulo == "Products", f"Título incorrecto: {titulo}"

    # Lista de productos
    productos = inventory.obtener_lista_productos()
    assert len(productos) > 0, "No se encontraron productos en el catálogo"

    # Obtener nombre y precio del primer producto
    primer_nombre = inventory.obtener_nombre_producto(0)
    primer_precio = inventory.obtener_precio_producto(0)

    print(f"Primer producto -> Nombre: {primer_nombre}  |  Precio: {primer_precio}")
