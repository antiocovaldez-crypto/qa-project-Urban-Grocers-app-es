import requests
import configuration
import data

def post_new_user(body):
    # Envía solicitud POST para crear usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    # Envía solicitud POST para crear kit
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=kit_body,
                         headers={"Authorization": ("Bearer " + auth_token)})

def get_new_user_token():
    # Usa el user_body de data.py para crear un usuario
    user_response = post_new_user(data.user_body)  # ← Aquí usas data.user_body
    return user_response.json()["authToken"]

def get_kit_body(name):
    # Función para crear cuerpo de kit con nombre personalizado
    current_kit_body = data.kit_body.copy()  # Usar copy() para no modificar el original
    current_kit_body["name"] = name
    return current_kit_body