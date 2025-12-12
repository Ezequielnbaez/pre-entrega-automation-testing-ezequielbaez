import os
import datetime
import pytest
from utils.driver_setup import setup_driver


CARPETA_SCREENSHOTS = "screenshots"

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
   #si falla captura pantalla
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver", None)
        if driver is None:
            return

        #crea carpeta si no existe
        if not os.path.exists(CARPETA_SCREENSHOTS):
            os.makedirs(CARPETA_SCREENSHOTS)

        nombre_test = item.name
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo = f"{nombre_test}_{timestamp}.png"
        ruta = os.path.join(CARPETA_SCREENSHOTS, archivo)

        driver.save_screenshot(ruta)

        # screenshoot en html
        if item.config.pluginmanager.hasplugin("html"):
            extra = getattr(rep, "extra", [])
            extra.append(pytest_html.extras.png(ruta))
            rep.extra = extra


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")
