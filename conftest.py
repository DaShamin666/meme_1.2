import pytest
from services.authorize import Authorize
from services.get_meme import GetMeme
from services.post_meme import PostMeme
from services.put_meme import PutMeme
from services.get_one_meme import GetOneMeme
from services.delete_meme import DeleteMeme
from services.valid_or_not import ValidOrNot


@pytest.fixture(scope='session')
def api_instance():
    return "Gachi Mem"


@pytest.fixture(scope='session')
def token():
    auth = Authorize()
    return auth.get_token("Gachi Mem")


@pytest.fixture(autouse=True)
def validate_token(token):
    status_code = ValidOrNot.validation_token(token)
    assert status_code == 200, "Токен недействителен."


@pytest.fixture()
def meme_data():
    return {
        "text": "очень смешные мемы))",
        "url": "https://www.meme-arsenal.com/memes/3f2a7b338fcd49f8d1d03b3f2a4bb7f2.jpg",
        "tags": ["сильный", "мощный"],
        "info": {"colors": ["черный", "все черное"]}
    }


@pytest.fixture()
def meme_id(api_instance, meme_data):
    post_meme = PostMeme(api_instance)
    return post_meme.execute(meme_data)


@pytest.fixture()
def get_meme_service(api_instance):
    return GetMeme(api_instance)


@pytest.fixture()
def post_meme_service(api_instance):
    return PostMeme(api_instance)


@pytest.fixture()
def put_meme_service(api_instance):
    return PutMeme(api_instance)


@pytest.fixture()
def get_one_meme_service(api_instance):
    return GetOneMeme(api_instance)


@pytest.fixture()
def delete_meme_service(api_instance, meme_id):
    delete_meme_instance = DeleteMeme(api_instance)
    yield delete_meme_instance


@pytest.fixture()
def created_meme(post_meme_service, meme_data):
    meme_id = post_meme_service.execute(meme_data)
    yield meme_id
