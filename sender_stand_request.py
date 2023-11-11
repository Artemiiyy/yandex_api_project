import configuration
import requests
import data


#Для получения токена авторизации созданем нового пользователя
def get_new_user_token(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # Создание нового пользователя
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
    return response.json()['authToken'] #Возращаем токен нового пользователя (вот эта функция)


#Создание нового набора у авторизованного пользователя
def post_new_client_kit(kit_body, auth_token):
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.NEW_PRODUCT_KIT,   #тут исправил
                         json=kit_body,
                         headers=headers_with_token)