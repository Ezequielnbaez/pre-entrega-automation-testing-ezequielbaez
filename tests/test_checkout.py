from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED
from utils.logger import logger

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

#REALIZA UN CHECKOUT CON UN PRODUCTO
def test_checkout_completo(driver):

    logger.info("Iniciando test_checkout_completo")
    driver.get(BASE_URL)
    logger.info(f"Abrí la URL: {BASE_URL}")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    logger.info(f"Realizando login con usuario predeterminado: {USUARIO_PRED}")
    login.login(USUARIO_PRED, PASS_PRED)

    logger.info("Agregando mochila al carrito")
    inventory.agregar_mochila()

    logger.info("Ingresando al carrito")
    inventory.abrir_carrito()

    logger.info("Iniciando proceso de checkout")
    cart.ir_checkout()

    logger.info("Completando formulario del checkout")
    checkout.completar_formulario("Ezequiel", "Baez", "2800")

    logger.info("Finalizando compra")
    checkout.finalizar_compra()

    mensaje = checkout.obtener_mensaje_final()
    logger.info(f"Mensaje final obtenido: {mensaje}")
    assert checkout.obtener_mensaje_final() == "Thank you for your order!", \
        "El mensaje final no coincide"

    logger.info("✔ Test checkout completado exitosamente")
