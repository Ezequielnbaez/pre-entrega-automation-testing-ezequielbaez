from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USUARIO_PRED, PASS_PRED, BASE_URL


def test_remover_seguir_comprando(driver):

    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Login
    login.login(USUARIO_PRED, PASS_PRED)

    # Agrega mochila y va al carrito
    inventory.agregar_mochila()
    inventory.abrir_carrito()

    # Valida item en carrito
    assert cart.cantidad_items() == 1, "El carrito debería tener 1 item"

    # Remover producto
    cart.remover_mochila()

    # Validar carrito vacío
    assert cart.cantidad_items() == 0, "El carrito debería quedar vacío después de remover el item"

    # Continuar comprando
    cart.continuar_comprando()

    # Validar que vuelve a Products
    assert inventory.obtener_titulo() == "Products", "No volvió a la página de productos"
