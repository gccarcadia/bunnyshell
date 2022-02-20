from playwright.sync_api import Page
from page_models.pm_users_edit import URL_EDIT_USER, NAME, USERNAME, EMAIL, \
    PHONE, BUTTON_UPDATE_USER
from test_data.users import edited_user as eu
from utils import URL_CREATE_USER


def test_ui_edit_user(page: Page, rest_client, setup, teardown):
    """ Edit a single user through the web user interface """

    page.goto(f"{URL_EDIT_USER}/{setup}")
    # Clear all the fields (by default Playwright concatenes existing string
    # with new strings in input fields)
    page.fill(NAME, "")
    page.fill(USERNAME, "")
    page.fill(EMAIL, "")
    page.fill(PHONE, "")
    # Fill in the new data for the user
    page.fill(NAME, eu.get("name"))
    page.fill(USERNAME, eu.get("username"))
    page.fill(EMAIL, eu.get("email"))
    page.fill(PHONE, eu.get("phone"))
    page.locator(BUTTON_UPDATE_USER).click()

    print("\nCheck if the user was edited")

    get_user_response = rest_client.api_call(
        host_url=f"{URL_CREATE_USER}/{setup}",
        http_method = "GET"
    )

    edited_user_response_dict = get_user_response.json()

    assert get_user_response.status_code == 200, \
        "Status code was not as expected!"

    assert edited_user_response_dict.get("name") == eu.get("name"), \
        f"The name of the edited user is not correct! Expected {eu.get('name')}"\
        f"but got {edited_user_response_dict.get('name')}"

    assert edited_user_response_dict.get("username") == eu.get("username"), \
        f"The username of the edited user is not correct! Expected "\
        f"{eu.get('username')} but got {edited_user_response_dict.get('username')}"

    assert edited_user_response_dict.get("email") == eu.get("email"), \
        f"The email of the edited user is not correct! Expected "\
        f"{eu.get('email')} but got {edited_user_response_dict.get('email')}"

    assert edited_user_response_dict.get("phone") == eu.get("phone"), \
        f"The phone number of the edited user is not correct! Expected "\
        f"{eu.get('phone')} but got {edited_user_response_dict.get('phone')}"
