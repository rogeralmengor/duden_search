# -*- coding: latin-1 -*-
from playwright.sync_api import Playwright, sync_playwright
import bs4 
import requests
import tempfile 
import xmltojson
import json
import pandas as pd
import argparse


def parseArguments(): 
    # Create argument parser
    parser = argparse.ArgumentParser(description= __doc__)

    # Positional mandatory arguments
    parser.add_argument('-iw', help='input word', \
        type=str, required=True, metavar='')
    
    parser.add_argument('-oj', help='complete path to JSON',\
         type=str, required = True, \
                        metavar='')

    parser.add_argument('-oc', help='complete path to output csv',\
         type=str, required = True, \
                        metavar='')

    # Parse arguments
    args = parser.parse_args()
    
    return args

def store_html_as_json(url:str, json_path:str): 
    html_response = requests.get(url=url)
    # Save the page content as sample.html
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = temp_dir.name 
    
    with open(temp_dir_path + "/" + "foo_bar.html", "w") as html_file:
        html_file.write(html_response.text)

    with open(temp_dir_path + "/" + "foo_bar.html", "r") as html_file:
        html = html_file.read()
        json_ = xmltojson.parse(html)
        print(json_)
    
    with open(json_path, "w") as file:
	    json.dump(json_, file)

def export_definitions_as_csv(csv_path: str, definitions:list, word:str):
    df = pd.DataFrame(definitions, columns = word)
    df.to_file(csv_path)

def run(playwright: Playwright) -> None:
    
    # Getting input arguments
    args = parseArguments()
    csv_path = args.oc
    json_path = args.oj
    word = args.iw

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
    
    for count, definition in enumerate(definitions, start=1):
        print(count, definition)
        print("-"*80)
    
    print("="*80)

    store_html_as_json(page, json_path=json_path)
    export_definitions_as_csv(csv_path=csv_path, 
                            definitions=definitions,
                            word=word)
    
    print("Closing browser and context")
    context.close()
    browser.close()

if __name__ == "__main__": 
    with sync_playwright() as playwright:
        run(playwright)