# -*- coding: latin-1 -*-
import requests
import bs4
from playwright.sync_api import sync_playwright


URL = "https://www.duden.de"

def can_open_website(url): 
    """Returns True if the website can open. 
    url.getcode == 200"""
    response = requests.get(url)
    if response.status_code == 200:
        print('Web site exists')
        return True
    else:
        print('Web site does not exist') 
        return False

def create_url_search(duden_url, word): 
    """Creates the string when you search for a 
    word on www.duden.de
    e.g. https://www.duden.de/suchen/dudenonline/Pferd"""
    
    if type(duden_url) and type(word) not in [str]: 
        TypeError
    else: 
        return URL + "/" + "suchen" + "/" + "dudenonline" + "/" + word 

def test_duden_is_working():
    """Tests if duden website is up"""
    can_open = can_open_website(URL) 
    assert True == can_open 

def test_concatenation_suche(): 
    """Test if concatenation of ganz works"""
    assert "https://www.duden.de/suchen/dudenonline/Pferd" == create_url_search(URL, "Pferd")

def test_can_open_search_word():
    """Tests if website search pattern can be requested"""
    assert True == can_open_website(create_url_search(URL, "Pferd"))

def test_navigation_urls(): 
    """Tests if every website opened through the bot execution 
    is a valid url"""
    with sync_playwright() as p: 
        word = "Einheit"
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.duden.de/")
    
        page.frame_locator("#sp_message_iframe_622759").locator("text=AKZEPTIEREN").first.click()
        page.locator("[placeholder=\"Stichwort\"]").click()
        page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")

        print(f"Fill placeholder with {word}")
        page.locator("[placeholder=\"Stichwort\"]").fill("B")
        page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
        page.locator("[placeholder=\"Stichwort\"]").fill(word)
    
        page.locator('button[class="form-asap__button"]').click()
        assert page.url == create_url_search(URL, word)
    
        page.locator('text=Zum vollst').nth(0).click()
        assert page.url == "https://www.duden.de/rechtschreibung/Einheit"
        context.close()
        browser.close()