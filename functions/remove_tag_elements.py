import re


async def remove_tag_elements(source_text: str):
    # Define a regular expression pattern to match HTML-like tags
    pattern = re.compile(
        r"<br\s*/?>|<[^>]*>"
    )  # Matches <br> or any other tags including nested tags

    # Use sub method to replace all matches with appropriate replacements
    def replace_tags(match):
        tag = match.group(0)
        if tag.startswith("<br"):
            return " "  # Replace <br> and <br/> with a space
        else:
            return ""  # Remove other tags completely

    # Use sub method with a function as the replacement
    clean_text = re.sub(pattern, replace_tags, source_text)
    return clean_text
