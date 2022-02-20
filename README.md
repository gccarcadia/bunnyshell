# Install dependencies
- Install Python (3.7 + required) and add pip and python executable to path
- Run `pip install -r requirements.txt` from the root project folder
- Run `playwright install`

# How to run tests
Run tests using headless browser (default) : `python -m pytest -v tests`
Run tests with headed browser: `python -m pytest -v --headed tests`
Run tests with specific browser: `python -m pytest -v --browser firefox --headed`
 (can be `chromium`, `firefox`, or `webkit`)

For additional information, please refer to those pages:
- `https://playwright.dev/python/docs/intro`
- `https://playwright.dev/python/docs/test-runners`.

# Bugs:
- Users are not unique - can add multiple users with the same data
- Every field of an user can be changed - including email

- Can add an user without any data
- There is no validation on any field (no number restrictions for phone number field, can enter anything in the email field, fields marked with * are not 
  mandatory)
- Pressing DELETE multiple times triggers additional DELETE requests and the app throws errors: Unhandled Rejection (Error): Request failed with status code 404

- and many others :)