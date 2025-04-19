import pytest
from test_api.data import MEME_DATA, UPDATED_MEME_DATA, INVALID_MEME_DATA
from services.get_one_meme import GetOneMeme
from services.get_meme import GetMeme


def test_get_memes(get_meme_service):
    response_code, response_data = get_meme_service.execute()
    assert response_code == 200
    assert response_data is not None
    assert isinstance(response_data, dict)
    assert "data" in response_data
    assert isinstance(response_data["data"], list)
    assert len(response_data["data"]) > 0
    assert all(isinstance(meme, dict) for meme in response_data["data"])
    assert all("id" in meme and "text" in meme and "url" in meme for meme in response_data["data"])


def test_post_new_meme(post_meme_service):
    meme_id, response_code = post_meme_service.execute(MEME_DATA)
    assert response_code == 200
    assert meme_id is not None



def test_put_meme(put_meme_service, new_meme_id, token):
    put_meme_service.headers['Authorization'] = token
    update_data = UPDATED_MEME_DATA.copy()
    update_data["id"] = new_meme_id
    response_code = put_meme_service.execute(new_meme_id, update_data)
    assert response_code == 200



def test_put_meme_nonexistent(put_meme_service):
    response_code = put_meme_service.execute("999999", UPDATED_MEME_DATA)
    assert response_code == 404


def test_delete_meme(delete_meme_service, new_meme_id, api_instance):
    response_code = delete_meme_service.execute(new_meme_id)
    assert response_code == 200
    # Проверяем, что мем действительно удален
    get_one_meme_service = GetOneMeme(api_instance)
    _, get_response_code = get_one_meme_service.execute(new_meme_id)
    assert get_response_code == 404


def test_post_meme_invalid(post_meme_service):
    _, response_code = post_meme_service.execute(INVALID_MEME_DATA)
    assert response_code == 400



def test_get_meme(get_meme_service):
    response_code, response_data = get_meme_service.execute()
    assert response_code == 200, "Метод должен возвращать статус 200 при получении мемов."
    assert response_data is not None, "Ответ не должен быть пустым."


def test_get_meme_invalid_token(api_instance):
    invalid_token = "invalid_token"
    get_meme_service = GetMeme(api_instance)
    get_meme_service.headers['Authorization'] = f"{invalid_token}"
    response_code, _ = get_meme_service.execute()
    assert response_code == 401, "Метод должен возвращать статус 401 при использовании невалидного токена."


def test_post_meme_invalid_data(post_meme_service):
    _, response_code = post_meme_service.execute(INVALID_MEME_DATA)
    assert response_code == 400, "Метод должен возвращать код 400 для некорректных данных."


def test_put_meme_invalid_data(put_meme_service, new_meme_id):
    response_code = put_meme_service.execute(new_meme_id, INVALID_MEME_DATA)
    assert response_code == 400, "Метод должен возвращать код 400 для некорректных данных при обновлении."


def test_delete_nonexistent_meme(delete_meme_service):
    nonexistent_meme_id = "invalid_id"
    response_code = delete_meme_service.execute(nonexistent_meme_id)
    assert response_code == 404, "Метод должен возвращать код 404 при попытке удаления несуществующего мема."


def test_get_one_meme(get_one_meme_service, new_meme_id):
    response_data, response_code = get_one_meme_service.execute(new_meme_id)
    assert response_code == 200, "Метод должен возвращать статус 200 при получении конкретного мема."
    assert response_data["id"] == new_meme_id, "Получен мем с неправильным ID"


def test_get_nonexistent_meme(get_one_meme_service):
    nonexistent_meme_id = "invalid_id"
    response_data, response_code = get_one_meme_service.execute(nonexistent_meme_id)
    assert response_code == 404, "Метод должен возвращать код 404 при попытке получения несуществующего мема."