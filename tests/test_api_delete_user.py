from utils import URL_CREATE_USER


def test_delete_user_by_id_via_api(rest_client, setup):
    """ Delete an user via API """

    delete_user_response = rest_client.api_call(
        host_url= f"{URL_CREATE_USER}/{setup}",
        http_method = "DELETE",
    )
    assert delete_user_response.status_code == 200, \
        "Status code was not as expected!"

    print("\nCheck if the user was deleted")

    get_user_response = rest_client.api_call(
        host_url=f"{URL_CREATE_USER}/user/{setup}",
        http_method = "GET"
    )

    assert get_user_response.status_code == 404, \
        "Status code is not as expected!"
