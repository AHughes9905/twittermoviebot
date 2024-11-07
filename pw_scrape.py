from playwright.sync_api import sync_playwright

def get_top_250_html():

    p = sync_playwright().start()
    browser =p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.imdb.com/chart/top/', wait_until="domcontentloaded")
    page.is_visible(':text-matches("^250..*")')
    html = page.content()
    p.stop()
    return html

