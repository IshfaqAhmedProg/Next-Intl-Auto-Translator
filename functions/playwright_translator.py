from playwright.async_api import async_playwright
from playwright_stealth import stealth_async


def format_log(text):
    if len(text) > 30:
        return f"[{text[:30]}...]"
    else:
        return f"[{text[:30]}]"


async def playwright_translator(source_lang: str, target_lang: str, source_text: str):
    print(f"Translating {format_log(source_text)}, please wait...!")
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await stealth_async(page)
            await page.goto(
                f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={source_text}&op=translate"
            )
            # wait for the target text to load
            await page.wait_for_selector(".lRu31")

            # select the target text using .lRu31 and store the first instance of it
            elements = await page.query_selector_all(".lRu31")
            await page.screenshot(path=f"images/test.png")
            target_text = await elements[0].inner_text()
            await browser.close()
            # print("target_text:", target_text)
            print(f"Translated to {format_log(target_text)}")
            return target_text


# await page.screenshot(path=f"images/test.png")
# tests
# page_ua = await browser.new_page()
# page_bot = await browser.new_page()
# await stealth_async(page_ua)
# await stealth_async(page_bot)
# await page_ua.goto("https://www.whatsmyua.info/")
# await page_ua.screenshot(path=f"images/ua-{browser_type.name}.png")
# await page_bot.goto("https://bot.sannysoft.com/")
# await page_bot.screenshot(path=f"images/bot-{browser_type.name}.png")
