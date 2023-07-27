from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ACCEPTED_LANGUAGES = [
    'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'en', 'el', 'es', 'fi', 'fr', 'it',
    'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans'
]


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Please, choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language in ACCEPTED_LANGUAGES:
        service = Service()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=service, options=options)
        print(f"{language} was selected")
    else:
        raise pytest.UsageError(
            f"--language should be one from accepted language. Here is the list :{ACCEPTED_LANGUAGES}")
    yield browser
    print("\nquit browser..")
    browser.quit()
