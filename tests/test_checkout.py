from utils.driver_setup import setup_driver
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

#REALIZA UN CHECKOUT CON UN PRODUCTO

def test_checkout_completo():
    driver = setup_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.login(USUARIO_PRED, PASS_PRED)

    # Agregar producto
    inventory.agregar_mochila()

    # Carrito
    inventory.abrir_carrito()

    # Checkout
    cart.ir_checkout()

    # Formulario
    checkout.completar_formulario("Ezequiel", "Baez", "2800")

    # Finalizar
    checkout.finalizar_compra()

    # Validar mensaje final
    assert checkout.obtener_mensaje_final() == "Thank you for your order!", \
        "El mensaje final no coincide"

    driver.quit()
