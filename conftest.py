import pytest
from services.authorize import Authorize
from services.post_meme import PostMeme
from services.get_meme import GetMeme
from services.put_meme import PutMeme
from services.get_one_meme import GetOneMeme
from services.delete_meme import DeleteMeme
from services.valid_or_not import ValidOrNot
from test_api.data import API_INSTANCE, MEME_DATA

@pytest.fixture(scope='session')
def api_instance():
    return API_INSTANCE

@pytest.fixture(scope='session')
def token():
    auth = Authorize()
    return auth.get_token(API_INSTANCE)

@pytest.fixture(autouse=True)
def validate_token(token):
    status_code = ValidOrNot.validation_token(token)
    assert status_code == 200, "Токен недействителен."

@pytest.fixture()
def meme_data():
    return MEME_DATA

@pytest.fixture
def new_meme_id(post_meme_service):
    meme_id, response_code = post_meme_service.execute(MEME_DATA)
    assert response_code == 200
    assert meme_id is not None
    return meme_id

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
def delete_meme_service(api_instance):
    return DeleteMeme(api_instance)