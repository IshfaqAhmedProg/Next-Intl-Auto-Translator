import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

# target main text:"lRu31"
# target extra texts[]:{target:"lrSgmd",source:"W5CUef"}


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await stealth_async(page)
            await page.goto(
                "https://translate.google.com/?sl=en&tl=ar&text=hello&op=translate"
            )
            # Wait for the elements to be available
            await page.wait_for_selector(".lRu31")

            # Get all elements with the class '.ryNqvb'
            elements = await page.query_selector_all(".lRu31")

            # Print the inner text of each element
            for element in elements:
                inner_text = await element.inner_text()
                print(inner_text)
            # await page.screenshot(path=f"images/test.png")
            await browser.close()


asyncio.run(main())


# tests
# page_ua = await browser.new_page()
# page_bot = await browser.new_page()
# await stealth_async(page_ua)
# await stealth_async(page_bot)
# await page_ua.goto("https://www.whatsmyua.info/")
# await page_ua.screenshot(path=f"images/ua-{browser_type.name}.png")
# await page_bot.goto("https://bot.sannysoft.com/")
# await page_bot.screenshot(path=f"images/bot-{browser_type.name}.png")
