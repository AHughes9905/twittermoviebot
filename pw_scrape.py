from playwright.sync_api import sync_playwright

def get_top_250_html():

    p = sync_playwright().start()
    browser =p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.imdb.com/chart/top/', wait_until="domcontentloaded")
    page.is_visible(':text-matches("^250..*")')
    page.wait_for_timeout(10000)
    #last_movie = page.locator("#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(250) > div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-a69a4297-2.bqNXEn.cli-title.with-margin > a")
    #last_movie.wait_for()
    html = page.content()
    p.stop()
    return html

