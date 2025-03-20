from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    print("Typing in search bar...")
    page.fill("input[name='q']", "Playwright is awesome")
    page.press("input[name='q']", "Enter")
    page.wait_for_timeout(5000)  # Watch it search
    print("Search page title:", page.title())
    browser.close()