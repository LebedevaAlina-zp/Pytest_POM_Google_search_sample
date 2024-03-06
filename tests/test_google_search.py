import pytest
from pages.google import MainPage
import datetime


@pytest.mark.parametrize("input_browser", ['chrome', 'firefox'])
def test_check_main_search(selenium_chromedriver, selenium_firefoxdriver, input_browser):
    """ Make sure main search works fine. """
    if input_browser == "chrome":
        page = MainPage(selenium_chromedriver)
    if input_browser == "firefox":
        page = MainPage(selenium_firefoxdriver)

    search_word = 'pytest'

    page.search.send_keys(search_word)
    page.search_run_button.click()

    page.screenshot(file_name='screenshots/' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + '.png')

    for title in page.search_results_titles.get_text():
        assert search_word in title.lower()

