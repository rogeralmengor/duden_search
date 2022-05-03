import requests
import urllib.request
URL = "https://duden.de"

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
        return duden_url + "/" + "suchen" + "/" + "dudenonline" + "/" + word 

def test_duden_is_working():
    """Tests if duden website is up"""
    can_open = can_open_website(URL) 
    assert True == can_open 

def test_concatenation_suche(): 
    """Test if concatenation of ganz works"""
    assert "https://duden.de/suchen/dudenonline/Pferd" == create_url_search(URL, "Pferd")

def test_can_open_search_word():
    """Tests if website search pattern can be requested"""
    assert True == can_open_website(create_url_search(URL, "Pferd"))

    #page = requests.get(URL)
    #print(page.text)
    #page.goto("ttps://www.duden.de")
    #print(page)
    #with sync_playwright() as p:
#        browser = p.chromium.launch()
#        page = browser.new_page()
#        page.goto("https://www.duden.de/")
#        print(page.title())
#        browser.close()
    #assert page.inner_text('h1') == 'Example Domain'
    #page.click("text=More information")


#https://www.duden.de/