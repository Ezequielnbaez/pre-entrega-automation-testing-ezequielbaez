from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED
from utils.logger import logger

#AGREGA EL PRIMER PRODUCTO Y VALIDA
def test_nav_ver(driver):

    logger.info("Iniciando test_nav_ver")
    driver.get(BASE_URL)
    logger.info(f"Abrí la URL: {BASE_URL}")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    logger.info(f"Realizando login con usuario predeterminado: {USUARIO_PRED}")
    login.login(USUARIO_PRED, PASS_PRED)

    logger.info("Validando el título de la página de inventario")
    titulo = inventory.obtener_titulo()
    assert titulo == "Products", f"Título incorrecto: {titulo}"

    logger.info("Obteniendo lista de productos del inventario")
    productos = inventory.obtener_lista_productos()
    assert len(productos) > 0, "No se encontraron productos en el catálogo"

    logger.info("Obteniendo nombre y precio del primer producto")
    primer_nombre = inventory.obtener_nombre_producto(0)
    primer_precio = inventory.obtener_precio_producto(0)

    logger.info(f"Primer producto -> Nombre: {primer_nombre}  |  Precio: {primer_precio}")

    logger.info("Test test_nav_ver finalizado con éxito")
