# -*- coding: latin-1 -*-
from playwright.sync_api import Playwright, sync_playwright
import bs4 

word = "Hund"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    print("Go to https://www.duden.de/")
    page.goto("https://www.duden.de/")
    
    print("Accept first pop up message")
    page.frame_locator("#sp_message_iframe_622759").locator("text=AKZEPTIEREN").first.click()
    print("Place cursor on placeholder")
    page.locator("[placeholder=\"Stichwort\"]").click()
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    
    print(f"Fill placeholder with {word}")
    page.locator("[placeholder=\"Stichwort\"]").fill("B")
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    page.locator("[placeholder=\"Stichwort\"]").fill(word)
    
    print("Click text=Nachschlagen oder Nachschlagen →")
    page.locator('button[class="form-asap__button"]').click()
    
    print(f'Word:\"{word}\" nachschlagen')
    page.locator('text=Zum vollst').nth(0).click()
    
    print("get html with bs4")
    html = page.inner_html("div:has(div.division)")
    import re
    soup = bs4.BeautifulSoup(html, "html.parser")
    bedeutung = soup.find_all("div", {"class":"enumeration__text"})

    print("Getting definitions as list")
    print("="*80)
    definitions = []
    for tag in bedeutung:
        definitions.append((tag.text.strip("\n")))
    #for definition in definitions:
    #    print(definition)
    for count, definition in enumerate(definitions):
        print(count, definition)
        print("-"*80)
    
    print("="*80)
    
    print("Closing everything")
    context.close()
    browser.close()

if __name__ == "__main__": 
    with sync_playwright() as playwright:
        run(playwright)