import asyncio
from pyppeteer import launch

async def main(url, xpath):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    #    html = await page.evaluate('document.getElementById("covid19dashdph").childNodes[0].getAttribute("src")', force_expr=True)
    js_selector = f'''
    document.evaluate('{xpath}', document, null, XPathResult.ANY_TYPE,null).iterateNext().nodeValue
    '''
    html = await page.evaluate(js_selector, force_expr=True)
    await browser.close()
    return html

def js_render_xpath_text(url, xpath):
    value = asyncio.get_event_loop().run_until_complete(main(url, xpath))
    return value


if __name__ == "__main__":
    print(js_render_xpath_text('https://dph.georgia.gov/covid-19-daily-status-report',
                               '//*[@id="covid19dashdph"]/iframe/@src'))
