from utils.driver_setup import setup_driver
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

#VERIFICA CARRITO LUEGO DE AGREGAR

def test_carrito():
    driver = setup_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Login
    login.login(USUARIO_PRED, PASS_PRED)

    # Inventory
    inventory.esperar_pagina()
    producto = inventory.conseguir_primer_producto()

    # Agregar PRIMER producto
    inventory.agregar_primer_producto()

    # Validar contador
    assert inventory.obtener_contador_carrito() == "1", "Contador del carrito incorrecto"

    # Ir al carrito
    inventory.abrir_carrito()
    cart.esperar()

    # Validar nombre del producto agregado
    nombre_carrito = cart.get_first_item_name()
    assert nombre_carrito == producto["nombre"], f"Producto incorrecto en carrito: {nombre_carrito}"

    driver.quit()
