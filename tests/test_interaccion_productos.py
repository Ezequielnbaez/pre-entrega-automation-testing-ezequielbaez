from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED
from utils.logger import logger

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

#VERIFICA CARRITO LUEGO DE AGREGAR
def test_carrito(driver):

    logger.info("Iniciando test_carrit")
    driver.get(BASE_URL)
    logger.info(f"Abrí la URL: {BASE_URL}")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    logger.info(f"Realizando login con usuario predeterminado: {USUARIO_PRED}")
    login.login(USUARIO_PRED, PASS_PRED)

    logger.info("Esperando que cargue la página de inventario")
    inventory.esperar_pagina()

    logger.info("Obteniendo información del primer producto")
    producto = inventory.conseguir_primer_producto()

    logger.info("Agregando el primer producto al carrito")
    inventory.agregar_primer_producto()

    contador = inventory.obtener_contador_carrito()
    logger.info(f"Contador del carrito: {contador}")
    assert inventory.obtener_contador_carrito() == "1", "Contador del carrito incorrecto"

    logger.info("Ir al carrito")
    inventory.abrir_carrito()
    cart.esperar()

    nombre_carrito = cart.get_first_item_name()
    logger.info(f"Producto encontrado en el carrito: {nombre_carrito}")
    nombre_carrito = cart.get_first_item_name()
    assert nombre_carrito == producto["nombre"], f"Producto incorrecto en carrito: {nombre_carrito}"

    logger.info("Test_carrito completado correctamente")
