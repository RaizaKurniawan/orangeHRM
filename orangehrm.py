import re
from playwright.sync_api import Page, expect, sync_playwright
from dotenv import load_dotenv
import os, config

load_dotenv()
url = os.getenv('URL')
username = config.validUsername
password = config.validPassword

def main():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        # Input username
        page.fill("input[name='username']", username)
        # Input password
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        page.wait_for_timeout(5000)




        #browser.close()





if __name__ == '__main__':
    main()