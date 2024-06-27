# replace_strings_in_object.py
from typing import Callable, Any
import inspect
import asyncio


def replace_strings_in_object(func: Callable[..., str]):
    # Ensure the function has 'source_text' as a parameter
    sig = inspect.signature(func)
    if "source_text" not in sig.parameters:
        raise ValueError("The function must have a parameter called 'source_text'")

    async def wrapper(nested_object: Any) -> None:
        stack = [(nested_object, None, None)]

        while stack:
            current, parent, key = stack.pop()

            if isinstance(current, dict):
                for k, value in current.items():
                    stack.append((value, current, k))
            elif isinstance(current, list):
                for index, item in enumerate(current):
                    stack.append((item, current, index))
            elif isinstance(current, str):
                translated_text = await func(source_text=current)
                if isinstance(parent, dict):
                    parent[key] = translated_text
                elif isinstance(parent, list):
                    parent[key] = translated_text

    return wrapper
