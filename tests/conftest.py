import pytest
from test_data.users import single_user
from utils.rest_client import RestClient
from utils import URL_API_BASE, URL_CREATE_USER, URL_ALL_USERS


@pytest.fixture(scope="session", autouse=True)
def rest_client():
    return RestClient()

@pytest.fixture(scope="function")
def setup(rest_client):
    """ Creates the user before the test """

    response = rest_client.api_call(
        host_url = URL_CREATE_USER,
        http_method = "POST",
        request_data = single_user
    )
    user_id = response.json().get("id")
    print(f"\nCreated user with id: {user_id}")
    yield user_id

@pytest.fixture()
def teardown(rest_client):
    """ Deletes created user after the test is finished"""

    yield
    # TODO - find a better way to cleanup the created users
    print("\nDeleting user with id 1...")
    rest_client.api_call(
        host_url = f"{URL_API_BASE}/user/1",
        http_method = "DELETE"
    )
