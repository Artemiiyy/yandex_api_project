import sender_stand_request
import data

#эта функция меняет значения в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body

# Функция для позитивной проверки (если сервер возвращает 201 и response.name верное)
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    #В переменную  auth_token сохраняется полученный токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    
    # В переменную kit_response сохраняется результат запроса на создание пользователя
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверить, что код ответа 201
    assert kit_response.status_code == 201

    # Проверить, что поле name  в запросе совпадает с name в ответе
    assert kit_response.json()["name"] == name

    # Функция для негативной проверки (если сервер возвращает 400)
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную  auth_token сохраняется полученный токен
    
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверить, что код ответа равен 400
    assert kit_response.status_code == 400


# Тест 1. Набор создается успешно
# Name - допустимое количество символов - 1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")

# Тест 2. Набор создается успешно
# Name - допустимое количество символов - 511
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Набор не создается
# Name - количество символов меньше доопустимого - 0
def test_create_kit_0_letter_in_name_get_400_response():
    negative_assert_code_400("")

# Тест 4. Набор не создается
# Name - количество символов больше допустимого - 512
def test_create_kit_512_letters_in_name_get_400_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Набор создается успешно
# Name - разрешены английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Набор создается успешно
# Name - разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Набор создается успешно
# Name - разрешены спецсимволы
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Набор создается успешно
# Name - разрешены пробелы
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Набор создается успешно
# Name - разрешены цифры
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Набор не создается
# Name параметр не передан в запрос
def test_create_kit_no_name_get_400_response():
    # Копируется словарь с телом запроса из файла data в переменную kits_body
    kits_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kits_body.pop("name")
    # В переменную  auth_token сохраняется полученный токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)

    # ну если я все правильно понял, то у меня не была написана эта функция, я ее написал в sender ))))
    
    # В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kits_body, auth_token)

    # Проверить, что код ответа - 400
    assert kit_response.status_code == 400


# Тест 11. Набор не создается
# В параметр name передан другой тип параметра
def test_create_number_as_name_get_400_response():
    negative_assert_code_400(123)