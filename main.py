from re import I
from playwright.sync_api import sync_playwright
import bs4
URL = "https://duden.de"


def main(): 
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page() 
        page.goto(URL)
        page.fill("input#edit-search-api-fulltext--2", "Pferd")
        page.click('text=Naschlagen')
        page.is_visible()
        html = page.inner_html()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        print(soup.find_all('strong'))


if __name__ == "__main__":
    main()