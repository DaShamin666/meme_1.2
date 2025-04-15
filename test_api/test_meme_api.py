from services.get_meme import GetMeme
from services.get_one_meme import GetOneMeme



def test_get_meme(get_meme_service):
    response_code = get_meme_service.execute()
    assert response_code == 200, "Метод должен возвращать статус 200 при получении мемов."


def test_get_meme_invalid_token():
    invalid_token = "invalid_token"
    get_meme_service = GetMeme("Gachi Mem")
    get_meme_service.headers['Authorization'] = f"{invalid_token}"
    response_code = get_meme_service.execute()
    assert response_code == 401, "Метод должен возвращать статус 401 при использовании невалидного токена."


def test_post_new_meme(post_meme_service, meme_data, delete_meme_service,meme_id):
    meme_id = post_meme_service.execute(meme_data)
    assert meme_id is not None, "Метод должен возвращать валидный ID мема после создания нового мема."

    invalid_meme_data = {"text": "", "url": "not_a_url"}
    response_code_invalid = post_meme_service.execute(invalid_meme_data)
    assert response_code_invalid is None, "Метод должен возвращать None для некорректных данных."

    delete_response_code = delete_meme_service.execute(meme_id)
    assert delete_response_code == 200, "Мем должен быть успешно удален."


def test_put_meme(put_meme_service, created_meme, delete_meme_service, api_instance,meme_id):
    meme_id = created_meme
    get_one_meme_service = GetOneMeme(api_instance)
    response_code = get_one_meme_service.execute(meme_id)
    assert response_code == 200, f"Мем с ID {meme_id} не найден."

    updated_data = {
        "id": meme_id,
        "text": "обновленный текст мема",
        "url": "https://www.meme-arsenal.com/memes/3f2a7b338fcd49f8d1d03b3f2a4bb7f2.jpg",
        "tags": ["новый", "тег"],
        "info": {"colors": ["новый цвет", "другой цвет"]},
    }

    response_code = put_meme_service.execute(meme_id, updated_data)
    assert response_code == 200, "Метод должен возвращать статус 200 после обновления мема."

    response_code_invalid = put_meme_service.execute(meme_id=-1, data=updated_data)
    assert response_code_invalid == 404, "Метод должен возвращать статус 404 для несуществующего мема."

    delete_response_code = delete_meme_service.execute(meme_id)
    assert delete_response_code == 200, "Мем должен быть успешно удален."



def test_delete_meme(post_meme_service, meme_data, delete_meme_service):
    meme_id = post_meme_service.execute(meme_data)
    response_code = delete_meme_service.execute(meme_id)
    assert response_code == 200, "Мем должен быть успешно удален."

    delete_response_code_invalid = delete_meme_service.execute(meme_id=-1)
    assert delete_response_code_invalid == 404, "Метод должен возвращать статус 404 для несуществующего мема."


def test_get_one_meme(post_meme_service, meme_data, get_one_meme_service, delete_meme_service,meme_id):
    meme_id = post_meme_service.execute(meme_data)
    response_code = get_one_meme_service.execute(meme_id)
    assert response_code == 200, "Метод должен возвращать статус 200 при получении конкретного мема."

    response_code_invalid = get_one_meme_service.execute(meme_id=-1)
    assert response_code_invalid == 404, "Метод должен возвращать статус 404 для несуществующего мема."

    delete_response_code = delete_meme_service.execute(meme_id)
    assert delete_response_code == 200, "Мем должен быть успешно удален."


def test_post_meme_invalid_data(post_meme_service):
    invalid_data = {"text": "текст мема"}  # Отсутствует URL
    response_code = post_meme_service.execute(invalid_data)
    assert response_code is None, "Метод должен возвращать None для некорректных данных."


def test_get_meme_with_invalid_token():
    invalid_token = "invalid_token"
    get_meme_service = GetMeme("Gachi Mem")
    get_meme_service.headers['Authorization'] = f"{invalid_token}"
    response_code = get_meme_service.execute()
    assert response_code == 401, "Метод должен возвращать статус 401 при использовании невалидного токена."
