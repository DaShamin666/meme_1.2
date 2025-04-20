
from test_api.data import MEME_DATA, UPDATED_MEME_DATA, INVALID_MEME_DATA
from services.get_one_meme import GetOneMeme
from services.get_meme import GetMeme
from test_api.base_test import BaseMemeTest


class TestMemeAPI(BaseMemeTest):
    def test_get_memes(self, get_meme_service, token):
        get_meme_service.headers['Authorization'] = token
        response_code, response_data = get_meme_service.execute()
        assert response_code == 200, "Получение списка мемов должно вернуть статус 200"
        assert response_data is not None, "Ответ не должен быть пустым"
        assert isinstance(response_data, dict), "Ответ должен быть словарем"
        assert "data" in response_data, "В ответе должен быть ключ 'data'"
        assert isinstance(response_data["data"], list), "Значение 'data' должно быть списком"

        if response_data["data"]:  # Проверяем структуру только если есть мемы
            for meme in response_data["data"]:
                self.assert_meme_structure(meme)

    def test_post_new_meme(self, post_meme_service, token, api_instance):
        post_meme_service.headers['Authorization'] = token
        meme_id, response_code = post_meme_service.execute(MEME_DATA)
        assert response_code == 200, "Создание мема должно вернуть статус 200"
        assert meme_id is not None, "ID созданного мема не должен быть None"

        # Проверяем, что мем действительно создан
        get_one_meme_service = GetOneMeme(api_instance)
        get_one_meme_service.headers['Authorization'] = token
        response_data, get_response_code = get_one_meme_service.execute(meme_id)
        assert get_response_code == 200, "Созданный мем должен быть доступен"
        self.assert_meme_structure(response_data)
        assert response_data["text"] == MEME_DATA["text"], "Текст мема не соответствует переданным данным"
        assert response_data["url"] == MEME_DATA["url"], "URL мема не соответствует переданным данным"
        assert response_data["tags"] == MEME_DATA["tags"], "Теги мема не соответствуют переданным данным"
        assert response_data["info"] == MEME_DATA["info"], "Информация о меме не соответствует переданным данным"

    def test_put_meme(self, put_meme_service, new_meme_id, token, api_instance):
        put_meme_service.headers['Authorization'] = token
        update_data = UPDATED_MEME_DATA.copy()
        update_data["id"] = new_meme_id
        response_code = put_meme_service.execute(new_meme_id, update_data)
        assert response_code == 200, "Обновление мема должно вернуть статус 200"

        # Проверяем, что мем действительно обновлен
        get_one_meme_service = GetOneMeme(api_instance)
        get_one_meme_service.headers['Authorization'] = token
        response_data, get_response_code = get_one_meme_service.execute(new_meme_id)
        assert get_response_code == 200, "Обновленный мем должен быть доступен"
        self.assert_meme_structure(response_data)
        assert response_data["text"] == UPDATED_MEME_DATA["text"], "Текст мема не был обновлен"
        assert response_data["url"] == UPDATED_MEME_DATA["url"], "URL мема не был обновлен"
        assert response_data["tags"] == UPDATED_MEME_DATA["tags"], "Теги мема не были обновлены"
        assert response_data["info"] == UPDATED_MEME_DATA["info"], "Информация о меме не была обновлена"

    def test_delete_meme(self, delete_meme_service, new_meme_id, api_instance, token):
        delete_meme_service.headers['Authorization'] = token
        response_code = delete_meme_service.execute(new_meme_id)
        assert response_code == 200, "Удаление мема должно вернуть статус 200"

        # Проверяем, что мем действительно удален
        get_one_meme_service = GetOneMeme(api_instance)
        get_one_meme_service.headers['Authorization'] = token
        _, get_response_code = get_one_meme_service.execute(new_meme_id)
        assert get_response_code == 404, "Удаленный мем не должен быть доступен"

    def test_post_meme_invalid(self, post_meme_service, token):
        post_meme_service.headers['Authorization'] = token
        _, response_code = post_meme_service.execute(INVALID_MEME_DATA)
        assert response_code == 400, "Создание мема с некорректными данными должно вернуть статус 400"

    def test_get_meme_invalid_token(self, api_instance):
        invalid_token = "invalid_token"
        get_meme_service = GetMeme(api_instance)
        get_meme_service.headers['Authorization'] = invalid_token
        response_code, _ = get_meme_service.execute()
        assert response_code == 401, "Запрос с невалидным токеном должен вернуть статус 401"

    def test_put_meme_invalid_data(self, put_meme_service, new_meme_id, token):
        put_meme_service.headers['Authorization'] = token
        response_code = put_meme_service.execute(new_meme_id, INVALID_MEME_DATA)
        assert response_code == 400, "Обновление мема с некорректными данными должно вернуть статус 400"

    def test_delete_nonexistent_meme(self, delete_meme_service, token):
        delete_meme_service.headers['Authorization'] = token
        nonexistent_meme_id = "invalid_id"
        response_code = delete_meme_service.execute(nonexistent_meme_id)
        assert response_code == 404, "Удаление несуществующего мема должно вернуть статус 404"

    def test_get_one_meme(self, get_one_meme_service, new_meme_id, token):
        get_one_meme_service.headers['Authorization'] = token
        response_data, response_code = get_one_meme_service.execute(new_meme_id)
        assert response_code == 200, "Получение мема должно вернуть статус 200"
        self.assert_meme_structure(response_data)
        assert response_data["id"] == new_meme_id, "Получен мем с неправильным ID"

    def test_get_nonexistent_meme(self, get_one_meme_service, token):
        get_one_meme_service.headers['Authorization'] = token
        nonexistent_meme_id = "invalid_id"
        response_data, response_code = get_one_meme_service.execute(nonexistent_meme_id)
        assert response_code == 404, "Получение несуществующего мема должно вернуть статус 404"