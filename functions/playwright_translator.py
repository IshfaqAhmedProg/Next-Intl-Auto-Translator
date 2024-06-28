from playwright.async_api import async_playwright, expect, Page
from playwright_stealth import stealth_async
import time
from urllib import parse
from typing import Optional
from asyncio import sleep
import re


# Wait for the target element to not have the undesired class
async def wait_for_element_not_to_have_class(
    page, target_element_selector, undesired_class, timeout=1
):
    """
    Waits for the target element to not have the specified undesired class using Playwright.

    Args:
        page: The Playwright page object.
        target_element_selector: The CSS selector to identify the target element.
        undesired_class: The class name the element should not have.
        timeout (optional): The maximum wait time in seconds (default: 10).
    """

    try:
        await page.wait_for_selector(
            target_element_selector, state="visible"
        )  # Ensure element is visible first
        await page.wait_for_function(
            f"""
      return !document.querySelector('{target_element_selector}').classList.contains('{undesired_class}')
      """,
            timeout=timeout * 1000,  # Convert seconds to milliseconds
        )
    except any:
        print(any)


def format_long_text(text: str, safe_length: int = 50):
    if len(text) > safe_length:
        return f"{text[:safe_length]}..."
    else:
        return f"{text[:safe_length]}"


async def playwright_translator(
    source_lang: str,
    target_lang: str,
    source_text: str,
    translate_engine: Optional[str] = "Google",
) -> str:

    if translate_engine not in ("Google", "Deepl"):
        raise ValueError("translate_engine must be either 'Google' or 'Deepl'")

    print(f"Translating [{format_long_text(source_text)}], please wait...!")
    text_tick = time.time()
    safe_source_text = parse.quote(source_text)

    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await stealth_async(page)

            target_elements = []
            if translate_engine == "Deepl":
                target_element_selector = '[name="target"] span:first-of-type'
                # This is used because the target_element by default will have .dl_disabled but we want it not to have .dl_disabled
                undesired_class = "dl_disabled"
                await page.goto(
                    f"https://www.deepl.com/en/translator#{source_lang}/{target_lang}/{safe_source_text}"
                )
                # wait for the target_element to not have the undesired_class
                await expect(page.locator(target_element_selector)).not_to_have_class(
                    undesired_class
                )
                # then query for the target_element
                target_elements = await page.query_selector_all(target_element_selector)

            else:
                target_element_selector = ".lRu31"
                await page.goto(
                    f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={safe_source_text}&op=translate"
                )
                # wait for the target text to load
                await page.wait_for_selector(target_element_selector)
                # then query for the target_element
                target_elements = await page.query_selector_all(target_element_selector)

            # select the target text using .lRu31 and store the first instance of it
            await page.screenshot(path=f"images/{format_long_text(source_text,10)}.png")
            target_text = await target_elements[0].inner_text()
            await browser.close()

            print(
                f"Translated to [{format_long_text(target_text)}]. Took {time.time()-text_tick}s"
            )
            del text_tick

            return target_text
