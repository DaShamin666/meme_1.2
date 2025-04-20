class BaseMemeTest:
    def assert_successful_response(self, response_code, response_data):
        assert response_code == 200, "Статус код должен быть 200"
        assert response_data is not None, "Ответ не должен быть пустым"
        assert isinstance(response_data, dict), "Ответ должен быть словарем"
        assert "data" in response_data, "В ответе должен быть ключ 'data'"
        assert isinstance(response_data["data"], list), "Значение 'data' должно быть списком"

    def assert_meme_structure(self, meme):
        assert isinstance(meme, dict), "Мем должен быть словарем"
        assert "id" in meme, "Мем должен иметь поле 'id'"
        assert "text" in meme, "Мем должен иметь поле 'text'"
        assert "url" in meme, "Мем должен иметь поле 'url'"
        assert "tags" in meme, "Мем должен иметь поле 'tags'"
        assert "info" in meme, "Мем должен иметь поле 'info'"
        assert isinstance(meme["tags"], list), "Теги должны быть списком"
        assert isinstance(meme["info"], dict), "Информация должна быть словарем"