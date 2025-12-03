from utils.selenium_func import click_elemento, obtener_elemento, obtener_texto, esperar_visibilidad
from selenium.common.exceptions import NoSuchElementException

#DECIDÍ MANTENER EL USO DE LAS FUNCIONES DE UTILS SIGUIENDO EL POM, PARA REUTILIZAR CÓDIGO


class InventoryPage:
    LOC_PRODUCTOS = ("class name", "inventory_item")
    LOC_MOCHILA = ("id", "add-to-cart-sauce-labs-backpack")
    LOC_CART_BTN = ("id", "shopping_cart_container")
    LOC_TITULO = ("class name", "title")
    LOC_ITEM_NOMBRE = ("class name", "inventory_item_name")
    LOC_ITEM_PRECIO = ("class name", "inventory_item_price")
    LOC_BTN_ADD = ("class name", "btn_inventory")


    def __init__(self, driver):
        self.driver = driver

    def agregar_mochila(self):
        click_elemento(self.driver, self.LOC_MOCHILA)
        return self

    def abrir_carrito(self):
        click_elemento(self.driver, self.LOC_CART_BTN)
        return self
    
    def obtener_titulo(self):
        return obtener_texto(self.driver, self.LOC_TITULO)

    def obtener_lista_productos(self):
        return obtener_elemento(self.driver, self.LOC_PRODUCTOS)
    
    def obtener_nombre_producto(self, index=0):
        nombres = obtener_elemento(self.driver, self.LOC_ITEM_NOMBRE)
        return nombres[index].text

    def obtener_precio_producto(self, index=0):
        precios = obtener_elemento(self.driver, self.LOC_ITEM_PRECIO)
        return precios[index].text
    
    def esperar_pagina(self):
        esperar_visibilidad(self.driver, self.LOC_TITULO)

    def esperar_catalogo(self, tiempo=10):
        esperar_visibilidad(self.driver, self.LOC_PRODUCTOS, tiempo)

    def conseguir_primer_producto(self):
        self.esperar_catalogo()
        productos = self.driver.find_elements(*self.LOC_PRODUCTOS)

        if not productos:
            raise Exception("No se encontraron productos en el inventario")

        primer_producto = productos[0]

        nombre = primer_producto.find_element(*self.LOC_ITEM_NOMBRE).text
        precio = primer_producto.find_element(*self.LOC_ITEM_PRECIO).text

        return {
            "nombre": nombre,
            "precio": precio
        }

    def agregar_primer_producto(self):
        self.esperar_catalogo()

        botones = self.driver.find_elements(*self.LOC_BTN_ADD)

        if not botones:
            raise Exception("No se encontró ningún botón 'Add to cart'")

        botones[0].click()

    def obtener_contador_carrito(self):
        try:
            return self.driver.find_element(*self.LOC_CART_BTN).text
        except NoSuchElementException:
            return "0"