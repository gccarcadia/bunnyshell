from playwright.sync_api import Page
from page_models.pm_users_add import URL_ADD_USER, NAME, USERNAME, EMAIL, \
    PHONE, BUTTON_ADD_USER
from test_data.users import single_user as su
from utils import URL_CREATE_USER


def test_ui_add_user(page: Page, rest_client, teardown):
    """  Add a single user through the web user interface """

    page.goto(URL_ADD_USER)
    page.fill(NAME, su.get("name"))
    page.fill(USERNAME, su.get("username"))
    page.fill(EMAIL, su.get("email"))
    page.fill(PHONE, su.get("phone"))
    page.locator(BUTTON_ADD_USER).click()

    print("\nCheck if the user was created")

    get_user_response = rest_client.api_call(
        host_url=f"{URL_CREATE_USER}/1",
        http_method = "GET"
    )

    created_user_response_dict = get_user_response.json()

    assert get_user_response.status_code == 200, \
        "Status code was not as expected!"

    assert created_user_response_dict.get("name") == su.get("name"), \
        f"The name of the edited user is not correct! Expected {su.get('name')}"\
        f"but got {created_user_response_dict.get('name')}"

    assert created_user_response_dict.get("username") == su.get("username"), \
        f"The username of the edited user is not correct! Expected "\
        f"{su.get('username')} but got {created_user_response_dict.get('username')}"

    assert created_user_response_dict.get("email") == su.get("email"), \
        f"The email of the edited user is not correct! Expected "\
        f"{su.get('email')} but got {created_user_response_dict.get('email')}"

    assert created_user_response_dict.get("phone") == su.get("phone"), \
        f"The phone number of the edited user is not correct! Expected "\
        f"{su.get('phone')} but got {created_user_response_dict.get('phone')}"