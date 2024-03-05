import pytest
from pages.google import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    search_word = 'pytest'

    page.search.send_keys(search_word)
    page.search_run_button.click()

    for title in page.search_results_titles.get_text():
        assert search_word in title.lower()

