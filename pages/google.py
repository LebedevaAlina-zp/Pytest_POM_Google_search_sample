import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://google.com/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='APjFqb')

    # Search button
    search_run_button = WebElement(xpath='//div[@class="FPdoLc lJ9FBc"]/center/input[@name="btnK"]')

    # Titles of the search results
    search_results_titles = ManyWebElements(xpath='//h3[@class="LC20lb MBeuO DKV0Md"]')
