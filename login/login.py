from playwright.sync_api import sync_playwright
import config

def try_login(page, username, password):
    page.goto(config.URL)
     # Input username
    page.fill("input[name='username']", username)
    # Input password
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    page.wait_for_timeout(5000)

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        #Positive Test: Valid Login
        print("Testing Positive Case: Valid Login")
        try_login(page, config.VALID_USER["username"], config.VALID_USER["password"])
        if page.locator(".oxd-text=Dashboard").is_visible():
            print("✅ Positive Test Passed: Logged in successfully!")
        else:
            print("❌ Positive Test Failed: No dashboard found.")
        # Go back to login page
        page.goto(config.URL)

        #Negative test
        print("\nTesting Negative Case: Invalid Login")
        try_login(page, config.INVALID_USER["username"], config.INVALID_USER["password"])
        # Check for error message
        if page.locator(".oxd-text=Invalid Credential")