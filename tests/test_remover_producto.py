from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USUARIO_PRED, PASS_PRED, BASE_URL
from utils.driver_setup import setup_driver

#REMUEVE PRODUCTO AGREGADO

def test_remover_seguir_comprando():
    driver = setup_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # login
    login.login(USUARIO_PRED, PASS_PRED)

    # agrega mochila y va al carrito
    inventory.agregar_mochila().abrir_carrito()

    # valida item
    assert cart.cantidad_items() == 1, "El carrito debería tener 1 item"

    # saca producto del carrito
    cart.remover_mochila()

    # valida
    assert cart.cantidad_items() == 0, "El carrito debería quedar vacío después de remover el item"
    cart.continuar_comprando()

    # valida página
    assert inventory.obtener_titulo() == "Products", "No volvió a la página de productos"

    driver.quit()
