from playwright.sync_api import sync_playwright

def pw_init(headless=True):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US"
    )
    return p, browser, context

def get_top_250_html(context, url="https://www.imdb.com/chart/top/"):
    page = context.new_page()
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    """)
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_selector(':text-matches("^250..*")')
    html = page.content()
    page.close()
    return html

def expand_spoiler_and_get_html(context, url):
    page = context.new_page()
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    """)
    page.goto(url, wait_until="domcontentloaded")
    try:
        spoiler_button = page.query_selector('button[aria-label="Expand Spoiler"]')
        if spoiler_button:
            spoiler_button.click()
            page.wait_for_timeout(500)  # Wait for content to expand
        html = page.content()
    except Exception as e:
        print(f"Error expanding spoiler: {e}")
        html = page.content()
    page.close()
    return html

def press_spoiler_button(context, url):
    page = context.new_page()
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
    """)
    page.goto(url, wait_until="domcontentloaded")
    try:
        spoiler_button = page.query_selector('button:has-text("Spoilers")')
        if spoiler_button:
            spoiler_button.click()
            result = True
        else:
            result = False
    except Exception as e:
        print(f"Error pressing spoiler button: {e}")
        result = False
    page.close()
    return result