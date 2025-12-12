from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USUARIO_PRED, PASS_PRED, BASE_URL
from utils.logger import logger


def test_remover_seguir_comprando(driver):

    logger.info("Iniciando test_remover_seguir_comprando")
    driver.get(BASE_URL)
    logger.info(f"Abrí la URL: {BASE_URL}")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    logger.info(f"Realizando login con usuario predeterminado: {USUARIO_PRED}")
    login.login(USUARIO_PRED, PASS_PRED)

    logger.info("Agregando la mochila al carrito")
    inventory.agregar_mochila()

    logger.info("Abriendo carrito")
    inventory.abrir_carrito()

    cantidad = cart.cantidad_items()
    logger.info(f"Items en carrito: {cantidad}")
    assert cart.cantidad_items() == 1, "El carrito debería tener 1 item"

    logger.info("Removiendo mochila del carrito")
    cart.remover_mochila()

    cantidad = cart.cantidad_items()
    logger.info(f"Items tras remover: {cantidad}")
    assert cart.cantidad_items() == 0, "El carrito debería quedar vacío después de remover el item"

    logger.info("Haciendo clic en 'Continue Shopping'")
    cart.continuar_comprando()

    titulo = inventory.obtener_titulo()
    logger.info(f"Título actual de la página: {titulo}")
    assert inventory.obtener_titulo() == "Products", "No volvió a la página de productos"

    logger.info("Test test_remover_seguir_comprando finalizado con éxito")
