import requests
from utils.logger import logger

#get
def test_api_get_posts(base_url):
    logger.info("Iniciando test_api_get_posts")

    response = requests.get(f"{base_url}/posts")

    assert response.status_code == 200, \
        f"Status esperado 200, recibido {response.status_code}"

    assert "application/json" in response.headers.get("Content-Type", ""), \
        "La respuesta no es JSON"

    data = response.json()
    assert isinstance(data, list), "La respuesta debería ser una lista"
    assert len(data) > 0, "No se recibieron posts"

    logger.info(f"Primer post recibido: {data[0]}")


#póst
def test_api_post_crear_post(base_url):
    logger.info("Iniciando test_api_post_crear_post")

    payload = {
        "title": "Prueba Automática",
        "body": "Contenido generado con pytest",
        "userId": 1
    }

    response = requests.post(f"{base_url}/posts", json=payload)

    data = validate_api_response(
        response,
        expected_status=201,
        expected_fields={"title", "body", "userId", "id"}
    )

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    logger.info(f"Post creado correctamente: {data}")


#delete
def test_api_delete_post(base_url):
    logger.info("Iniciando test_api_delete_post")

    response = requests.delete(f"{base_url}/posts/1")

    #JSONPlaceholder devuelve 200 en DELETE
    validate_api_response(response, expected_status=200)

    logger.info("Delete ejecutado correctamente")


#punto opcional: encadenamiento
def test_api_flujo_completo(base_url):
    logger.info("Iniciando flujo encadenado")

    #crea recurso
    payload = {"title": "Flow test", "body": "pytest chaining test", "userId": 99}
    r1 = requests.post(f"{base_url}/posts", json=payload)

    nuevo = validate_api_response(
        r1,
        expected_status=201,
        expected_fields={"title", "body", "userId", "id"}
    )
    logger.info(f"Recurso creado: {nuevo}")

    #obtiene id
    r2 = requests.get(f"{base_url}/posts/{nuevo['id']}")

    #GET puede devolver 404
    assert r2.status_code in (200, 404), \
        f"Se esperaba 200 o 404, recibido {r2.status_code}"

    if r2.status_code == 200:
        validate_api_response(
            r2,
            expected_status=200,
            expected_fields={"userId", "id", "title", "body"}
        )
        logger.info(f"Recurso obtenido: {r2.json()}")
    else:
        logger.info("El recurso no existe realmente (comportamiento esperado en JSONPlaceholder)")

    #borra recurso
    r3 = requests.delete(f"{base_url}/posts/{nuevo['id']}")

    validate_api_response(r3, expected_status=200)

    logger.info("Flujo completo ejecutado exitosamente")


#validaciones
def validate_api_response(response, expected_status, expected_fields=None, max_time=1.0):
    """Validación de API con 5 niveles"""

    #status code
    assert response.status_code == expected_status, \
        f"Status esperado {expected_status}, recibido {response.status_code}"

    #headers
    if expected_status != 204:
        assert "application/json" in response.headers.get("Content-Type", ""), \
            "La respuesta no es JSON"

    #estructura + contenido
    if expected_fields and response.text:
        body = response.json()
        if isinstance(body, dict):
            assert expected_fields <= set(body.keys()), \
                f"Faltan campos: {expected_fields - set(body.keys())}"

    #performance
    assert response.elapsed.total_seconds() < max_time, \
        f"La respuesta tardó demasiado: {response.elapsed.total_seconds()}s"

    return response.json() if response.text else None
