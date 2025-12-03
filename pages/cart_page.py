from utils.selenium_func import click_elemento,esperar_visibilidad

#DECIDÍ MANTENER EL USO DE LAS FUNCIONES DE UTILS SIGUIENDO EL POM, PARA REUTILIZAR CÓDIGO

class CartPage:
    LOC_REMOVE_BTN = ("id", "remove-sauce-labs-backpack")
    LOC_CONTINUE_SHOPPING = ("id", "continue-shopping")
    LOC_CHECKOUT_BTN = ("id", "checkout")
    LOC_CART_ITEMS = ("class name", "cart_item")
    LOC_TITULO = ("class name", "title")
    LOC_ITEM_NAME = ("class name", "inventory_item_name")


    def __init__(self, driver):
        self.driver = driver

    def remover_mochila(self):
        click_elemento(self.driver, self.LOC_REMOVE_BTN)

    def continuar_comprando(self):
        click_elemento(self.driver, self.LOC_CONTINUE_SHOPPING)

    def ir_checkout(self):
        click_elemento(self.driver, self.LOC_CHECKOUT_BTN)

    def cantidad_items(self):
        items = self.driver.find_elements(*self.LOC_CART_ITEMS)
        return len(items)
    
    def esperar(self):
        esperar_visibilidad(self.driver, self.LOC_TITULO)
    
    def get_first_item_name(self):
        esperar_visibilidad(self.driver, self.LOC_CART_ITEMS)
        items = self.driver.find_elements(*self.LOC_CART_ITEMS)
        if not items:
            raise AssertionError("El carrito está vacío, no hay productos")

        return items[0].find_element(*self.LOC_ITEM_NAME).text