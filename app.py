import json
import asyncio
from functions import (
    playwright_translator,
    replace_strings_in_object,
    remove_tag_elements,
)
import time
from pypeepa import signature, getFilePath, readJSON
import re


source_lang = "en"
target_lang = "ar"
translate_engine = "Deepl"


async def main():
    signature("\nNext-Intl Auto Translator")
    source_file = getFilePath(
        "Enter the path of the json file containing the source text: ", ".json"
    )
    translation_object = readJSON(source_file)

    # Clean the tag elements <hl><hl/> from the raw data
    cleanup_tick = time.time()
    print("Cleaning any tag elements that is present! please wait...")
    translation_object_cleaner = replace_strings_in_object(remove_tag_elements)
    await translation_object_cleaner(translation_object)
    print(f"Took {time.time()-cleanup_tick} to cleanup text.")
    del cleanup_tick

    # binding function to bind source_lang and target_lang
    async def translator_with_lang(source_text: str) -> str:
        return await playwright_translator(
            source_lang=source_lang,
            target_lang=target_lang,
            source_text=source_text,
            translate_engine=translate_engine,
        )

    # translating translation_object
    translation_tick = time.time()
    replace_strings = replace_strings_in_object(translator_with_lang)
    await replace_strings(translation_object)

    # converting dict to str
    translation_object_str = json.dumps(translation_object, ensure_ascii=False)

    # writing out the file
    with open(f"{target_lang}-{translate_engine}.json", "w", encoding="utf-8") as f:
        f.write(translation_object_str)
    print(f"Total time taken to translate {time.time()-translation_tick}s")


asyncio.run(main())
