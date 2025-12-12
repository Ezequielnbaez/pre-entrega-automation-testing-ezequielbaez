#  Proyecto de Automatización de Pruebas - SauceDemo

## 1. Propósito del Proyecto

El objetivo es demostrar un framework de automatización profesional que integre:

- Pruebas UI con Selenium WebDriver
- Pruebas API con Requests
- Buenas prácticas de estructura y reutilización
- Reportes detallados
- Screenshots automáticos en fallos
- Fixtures centralizados en `conftest.py`

Los casos de prueba fueron desarrollados con **Python**, **Selenium** y **Pytest**.
Las funciones utilizadas para un código más modular están en utils, el chromedriver está en la carpeta drivers.
Los datos usados de usuarios par alogin se acceden leyendo un json en la carpeta datos.
Los archivos principales para las prubeas de automatización están en tests.
Por último los reportes se guardan en carpeta reports.

---

## 2. Tecnologías Utilizadas
- **Python 3.x**
- **Selenium WebDriver**
- **WebDriver Manager**
- **Pytest**
- **Pytest-HTML**
- **Requests**
- **Logging**
- **POM (Page Object Model)**
---

## 3. Estructura
TP_AUTOMATIZACION/
│
├── datos/                          # Archivos de datos usados por los tests
│   └── usuarios.json
│
├── drivers/                        # Drivers de navegador
│   ├── chromedriver.exe
│   ├── LICENSE.chromedriver
│   └── THIRD_PARTY_NOTICES.chromedriver
│
├── logs/                           # Logs generados por pytest (pytest.ini + logger.py)
│   └── (se generan automáticamente)
│
├── pages/                          # Page Objects (POM)
│   ├── __pycache__/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/                        # Reportes HTML generados por pytest-html
│   └── (pytests-report.html, etc.)
│
├── screenshots/                    # Capturas automáticas al fallar un test
│   └── (se generan automáticamente con timestamp)
│
├── tests/                          # Casos de prueba
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_automatizacion_login.py
│   ├── test_checkout.py
│   ├── test_interaccion_productos.py
│   ├── test_navegacion_verificacion.py
│   ├── test_remover_producto.py
│   └── test_selenium.py
│
├── utils/                          # Funciones auxiliares reutilizables
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py                   # Configuraciones del proyecto
│   ├── data_utils.py               # Lectura y parsing de datos
│   ├── driver_setup.py             # Setup del WebDriver
│   ├── logger.py                   # Configuración centralizada de logs
│   └── selenium_func.py            # Funciones comunes de Selenium
│
├── venv/                           # Entorno virtual (no se sube a git)
│
├── conftest.py                     # Fixtures globales (driver, reportes, screenshots)
├── README.md                       # Documentación del proyecto
└── requirements.txt                # Dependencias del proyecto


## 4. Instalación de Dependencias

1. **Clonar el repositorio**
   git clone https://github.com/Ezequielnbaez/pre-entrega-automation-testing-ezequielbaez

   cd pre-entrega-automation-testing-ezequielbaez

3. **Crear y activar un entorno virtual**
   python -m venv venv
   venv\Scripts\activate

4. **Instalar dependencias**
   pip install -r requirements.txt


## 5. Generar Reporte HTML de Pruebas


**Test de todos los archivos**:
pytest tests/ -v --html=reporte_general.html

Test automatización de login:
pytest tests/test_automatizacion_login.py -v --html=reporte.html

**Test navegación y verificación**:
pytest tests/test_navegacion_verificacion.py -v --html=reporte.html

**Test interacción de productos(test completo de todos los puntos, login, navegacion y carrito)**:
pytest tests/test_interaccion_productos.py -v --html=reporte.html

Test checkout:
pytest tests/test_checkout.py -v --html=reporte.html


Test remover producto:
pytest tests/test_remover_producto.py -v --html=reporte.html

Test de API completo
pytest tests/test_api.py --html=reports/api_report.html --self-contained-html

Test completo con fallos, logs y screenshots
pytest --html=report.html --self-contained-html

## 6. El archivo report.html contiene:

**Resumen general del run**
**Detalle por test**
**Logs adjuntos**
**Capturas de pantalla en fallos**
**Información de tiempos y metadata**


Ezequiel Báez
Proyecto realizado como parte del curso de Automatización
Año: 2025
