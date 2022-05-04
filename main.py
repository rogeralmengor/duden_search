# -*- coding: latin-1 -*-
from attr import attr
from playwright.sync_api import Playwright, sync_playwright, expect
import bs4 
import pprint

word = "Hund"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    #browser = playwright.chromium.launch()
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    print("Go to https://www.duden.de/")
    page.goto("https://www.duden.de/")
    print("Click text=AKZEPTIEREN >> nth=0")
    page.frame_locator("#sp_message_iframe_622759").locator("text=AKZEPTIEREN").first.click()
    print("Click [placeholder=\"Stichwort\"]")
    page.locator("[placeholder=\"Stichwort\"]").click()
    print("Press CapsLock")
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    print("Fill [placeholder=\"Stichwort\"]")
    page.locator("[placeholder=\"Stichwort\"]").fill("B")
    print("Press CapsLock")
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    print("Fill [placeholder=\"Stichwort\"]")
    page.locator("[placeholder=\"Stichwort\"]").fill(word)
    print("Click text=Nachschlagen oder Nachschlagen →")
    #page.click('button[text=Nachschlagen]')
    #page.locator('button', has_text='Nachschlagen]').click()
    page.locator('button[class="form-asap__button"]').click()
    # expect(page).to_have_url("https://www.duden.de/suchen/dudenonline/word")
    print(f'Word:\"{word}\" nachschlagen')
    #print("Click text=word Substantiv, Neutrum – aus Malz, Hopfen, Hefe und Wasser … Zum vollständigen >> strong")
    #page.locator('a:has-text("Zum vollst\p{L}ndigen Artikel")')
    #page.locator('text=').click()
    page.locator('text=Zum vollst').nth(0).click()
    #page.locator("text=Gitarre Substantiv, feminin – Zupfinstrument mit flachem [einer Acht \p{L}hnlichem >> strong").click()
    #page.locator("text=Gi­tar­re Substantiv, feminin – Zupfinstrument mit flachem [einer Acht ähnlichem >> a").nth(1).click()
    #page.frame_locator("[id=\"google_ads_iframe_\\/53015287\\,224194632\\/duden\\.de_interstitial_0\"]").frame_locator("iframe[name=\"ad_iframe\"]").locator("[aria-label=\"Anzeige schließen\"]").click()
    #page.locator(f"a", has_text=word).click()
    #row = page.locator('a')
    #row.locator(":scope", has_text=word).click()
    #page.locator('a', has_text = word).click()
    #page.locator(f'a[text="Zum vollst"])').click()
    #page.query_selector('strong[text=\"{word}\"]').click()
    #page.locator(f'a:has-text(\"{word}\")').click()
    #page.locator(f'strong:has-text(\"{word}\")').click()
    #page.locator(f'article:has(strong)').click()
    #page.locator(f'h2:has(strong:has-text(\"{word}\"))').click()
    print("get html")
    #print(page.content())
    html = page.inner_html("div:has(div.division)")
    #print(html)
    import re
    soup = bs4.BeautifulSoup(html, "html.parser")
    #bedeutung= soup.findAll("li", id=re.compile('^Bedeutung-'))
    bedeutung = soup.find_all("div", {"class":"enumeration__text"})
    #bedeutung = soup.findAll("div", {"class": "enumeration__text"})
    #print(bedeutung.text)
    print(type(bedeutung))
    definitions = []
    for tag in bedeutung:
        definitions.append((tag.text.strip("\n")))
    for definition in definitions:
        print(definition)
    #print(soup)


    #print(bedeutung)
    #print(bedeutung)
    #for div in bedeutung.findAll("div"):
    #    print(div)
    #    print("-"*80)
    #print(soup.get_text())
    #for li in soup.find_all("li"):
    #    print(li)
    
    #page.locator('a >> nth=0').click()
    #page.locator('strong').click()
    # expect(page).to_have_url("https://www.duden.de/suchen/dudenonline/word#google_vignette")
    # Click [aria-label="Anzeige schließen"]
    #page.frame_locator("[id=\"google_ads_iframe_\\/53015287\\,224194632\\/duden\\.de_interstitial_0\"]").frame_locator("iframe[name=\"ad_iframe\"]").locator("[aria-label=\"Anzeige schließen\"]").click()
    # expect(page).to_have_url("https://www.duden.de/rechtschreibung/word")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)