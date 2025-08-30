import sender_stand_request
import data

# Función de prueba positiva
def positive_assert(name):
    # Paso 1: Crear usuario y obtener token
    user_body = data.user_body  # Usar datos base del usuario
    user_response = sender_stand_request.post_new_user(user_body)

    # Verificar que el usuario se creó correctamente
    assert user_response.status_code == 201
    auth_token = user_response.json()["authToken"]

    # Paso 2: Crear kit usando el token
    kit_body = sender_stand_request.get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificar que el kit se creó correctamente
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_negative_assert_empty_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()
    
    # Paso 2: Crear kit con nombre vacío
    kit_body = {"name": ""}  # Aquí está la prueba: nombre vacío
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    # Verificaciones
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_negative_assert_512_char_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre 512 char
    kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}  # Aquí está el problema: nombre demasiado largo
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_negative_assert_missing_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre faltante
    kit_body = {} # Aquí está la prueba: nombre faltante
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_negative_assert_real_number_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre numero real
    kit_body = {"name" : 123} # Aquí está la prueba: nombre numero real,
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_positive_assert_1_char_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre valido 1 caracter
    kit_body = {"name": "a"}  # Aqui esta la prueba: 1 carácter
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]  # ¡Esta es la diferencia clave con las pruebas negativas!


def test_positive_assert_511_char_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre valido 511 caracteres
    kit_body = { "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}  # Aqui esta la prueba: 511 caracteres
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_positive_assert_special_char_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre caracteres especiales
    kit_body = {"name": '"№%@",'}  # Aqui esta la prueba: carácteres especiales
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_positive_assert_blank_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre con espacio en blanco
    kit_body = {"name": " A Aaa "}  # Aqui esta la prueba: 1 espacio vacio
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def test_positive_assert_numbers_string_name():
    # Paso 1: Crear usuario y obtener token
    auth_token = sender_stand_request.get_new_user_token()

    # Paso 2: Crear kit con nombre con numeros
    kit_body = {"name": "123"}  # Aqui esta la prueba: numeros string
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Verificaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]
