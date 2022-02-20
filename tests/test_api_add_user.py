from test_data.users import single_user
from utils import URL_CREATE_USER


def test_add_user_via_api(rest_client, teardown):
    """ Add an user via API """

    create_user_response = rest_client.api_call(
        host_url = URL_CREATE_USER,
        http_method="POST",
        request_data = single_user
    )
    assert create_user_response.status_code == 201, \
        "Status code was not as expected!"
    create_user_response_dict = create_user_response.json()
    assert create_user_response_dict.get("id") == 1, \
        "The user id was not as expected"
    assert create_user_response_dict.get("user") == \
        single_user.get("user")
    assert create_user_response_dict.get("username") == \
        single_user.get("username")
    assert create_user_response_dict.get("email") == \
        single_user.get("email")
    assert create_user_response_dict.get("phone") == \
        single_user.get("phone")

    print("\nCheck if the user was created")

    get_user_response = rest_client.api_call(
        host_url=f"{URL_CREATE_USER}/{create_user_response_dict.get('id')}",
        http_method = "GET"
    )
    
    assert get_user_response.status_code == 200, \
        "Status code is not as expected!"
