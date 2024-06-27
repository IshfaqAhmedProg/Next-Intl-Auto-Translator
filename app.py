import json
import asyncio
from functions import playwright_translator, replace_strings_in_object


# target main text:"lRu31"
# target extra texts[]:{target:"lrSgmd",source:"W5CUef"}


source_text = "hello"
source_lang = "en"
target_lang = "ar"

translation_object = {
    "a": "hello",
    "b": {"c": "world", "d": ["how", {"e": "are"}]},
    "f": ["today", "you"],
}


async def main():
    async def translator_with_lang(source_text: str) -> str:
        return await playwright_translator(
            source_lang=source_lang, target_lang=target_lang, source_text=source_text
        )

    wrapped_replace_strings = replace_strings_in_object(translator_with_lang)
    await wrapped_replace_strings(translation_object)

    translation_object_str = json.dumps(translation_object, ensure_ascii=False)
    with open(f"{target_lang}.json", "w", encoding="utf-8") as f:
        f.write(translation_object_str)


asyncio.run(main())
