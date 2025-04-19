from services.get_one_meme import GetOneMeme
from services.get_meme import GetMeme
from services.post_meme import PostMeme



def test_put_meme_invalid_data(put_meme_service, meme_id):
    invalid_data = {"text": "", "url": "not_a_url"}
    response_code = put_meme_service.execute(meme_id, invalid_data)
    assert response_code == 400, "Метод должен возвращать код 400 для некорректных данных при обновлении."

def test_get_one_meme(get_one_meme_service, meme_id):
    response_data, response_code = get_one_meme_service.execute(meme_id)
    assert response_code == 200, "Метод должен возвращать статус 200 при получении конкретного мема."

def test_post_meme_forbidden(post_meme_service):
    forbidden_data = {
        "text": "запрещенный контент",
        "url": "https://img-cdn.tnwcdn.com/image?fit=1200%2C1200&height=1200&url=https%3A%2F%2Fcdn0.tnwcdn.com%2Fwp-content%2Fblogs.dir%2F1%2Ffiles%2F2021%2F06%2FAI-Memer_-very-angry-troll_1_1.jpg&signature=f3914220842cdc9f191d3b7417510a1e"
    }
    _, response_code = post_meme_service.execute(forbidden_data)
    assert response_code == 403, "Метод должен возвращать код 403 для запрещенного контента."

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

def test_post_new_meme(post_meme_service, meme_data, meme_id):
    meme_id, response_code = post_meme_service.execute(meme_data)
    assert response_code == 200, "Метод должен возвращать статус 200 при создании нового мема."
    assert meme_id is not None, "Метод должен возвращать валидный ID мема после создания нового мема."

def test_post_meme_invalid_data(post_meme_service):
    invalid_data = {"text": "", "url": "not_a_url"}
    _, response_code = post_meme_service.execute(invalid_data)
    assert response_code == 400, "Метод должен возвращать код 400 для некорректных данных."


def test_put_meme(put_meme_service, meme_id, api_instance):

    if isinstance(meme_id, tuple):
        meme_id = meme_id[0]

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


def test_delete_meme(post_meme_service, meme_data, delete_meme_service, meme_id):
    meme_id, _ = post_meme_service.execute(meme_data)
    response_code = delete_meme_service.execute(meme_id)
    assert response_code == 200, "Мем должен быть успешно удален."

def test_delete_nonexistent_meme(delete_meme_service):
    nonexistent_meme_id = "invalid_id"
    response_code = delete_meme_service.execute(nonexistent_meme_id)
    assert response_code == 404, "Метод должен возвращать код 404 при попытке удаления несуществующего мема."

def test_get_nonexistent_meme(get_one_meme_service):
    nonexistent_meme_id = "invalid_id"
    response_data, response_code = get_one_meme_service.execute(nonexistent_meme_id)
    assert response_code == 404, "Метод должен возвращать код 404 при попытке получения несуществующего мема." 