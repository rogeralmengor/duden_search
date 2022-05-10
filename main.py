# -*- coding: latin-1 -*-
"""
Small command line programme for looking up words from the Duden dictionary
"""

from playwright.sync_api import Playwright, sync_playwright
import bs4 
import requests
import tempfile 
import json
import pandas as pd
import argparse
import html_to_json
import logging


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
    
    with open(temp_dir_path + "/" + "foo_bar.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_response.text)

    with open(temp_dir_path + "/" + "foo_bar.html", "r", encoding="utf-8") as html_file:
        html = html_file.read()
        json_ = html_to_json.convert(html)
    
    with open(json_path, "w", encoding="utf-8") as file:
	    json.dump(json_, file)

def export_definitions_as_csv(csv_path: str, definitions:list, word:str):
    df = pd.DataFrame(definitions, columns = [word])
    df.to_csv(csv_path)

def run(playwright: Playwright, csv_path:str, json_path:str, word:str) -> None:
    
    # Configuring logger 
    
    logging.basicConfig(filename='Prozess.log', encoding='utf-8', level=logging.DEBUG)
    
    # Getting input arguments

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    logging.debug("Go to https://www.duden.de/")
    page.goto("https://www.duden.de/")
    
    logging.debug("Accept first pop up message")
    page.frame_locator("#sp_message_iframe_622759").locator("text=AKZEPTIEREN").first.click()
    logging.debug("Place cursor on placeholder")
    page.locator("[placeholder=\"Stichwort\"]").click()
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    
    logging.debug(f"Fill placeholder with {word}")
    page.locator("[placeholder=\"Stichwort\"]").fill("B")
    page.locator("[placeholder=\"Stichwort\"]").press("CapsLock")
    page.locator("[placeholder=\"Stichwort\"]").fill(word)
    
    logging.debug("Click text=Nachschlagen oder Nachschlagen →")
    page.locator('button[class="form-asap__button"]').click()
    
    logging.debug(f'Word:\"{word}\" nachschlagen')
    page.locator('text=Zum vollst').nth(0).click()
    
    logging.debug("get html with bs4")
    html = page.inner_html("div:has(div.division)")
    soup = bs4.BeautifulSoup(html, "html.parser")
    bedeutung = soup.find_all("div", {"class":"enumeration__text"})

    logging.debug("Getting definitions as list")
    logging.debug("="*80)
    
    definitions = []
    
    for tag in bedeutung:
        definitions.append((tag.text.strip("\n")))
    
    for count, definition in enumerate(definitions, start=1):
        logging.debug(count, definition)
        logging.debug("-"*80)
    
    logging.debug("="*80)

    export_definitions_as_csv(csv_path=csv_path, 
                            definitions=definitions,
                            word=word)
    store_html_as_json(page.url, json_path=json_path)
    
    logging.debug("Closing browser and context")
    context.close()
    browser.close()


def main(): 
    args = parseArguments()
    csv_path = args.oc
    json_path = args.oj
    word = args.iw
    with sync_playwright() as playwright:
        run(playwright, csv_path, json_path, word)

if __name__ == "__main__":
    main()  
