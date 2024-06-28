# Next-Intl-Auto-Translator

- [Next-Intl-Auto-Translator](#next-intl-auto-translator)
  - [Introduction](#introduction)
    - [Warning ⚠](#warning-)
  - [Requirements](#requirements)
  - [How To Run](#how-to-run)

## Introduction

This is a python script that allows you to automate translation of Next-Intl messages using one of two translation engines (Google Translate or Deepl). You can translate any json file from any source language to a target language. Any tag elements in your message file will be removed. It works by using playwright to scrape the results of your translation from Google Translate or Deepl. There is a possibility that the desired translation might be one of the suggested translations instead of the first translation. This will only take the first translation and not the suggested translation. The purpose of this script is to see if it is possible to automate translation without requiring any API keys.

### Warning ⚠
**Using tools that scrape Google Translate or DeepL violates their terms of service and can lead to legal action, account suspension, IP blocking, and data inaccuracies. Always use these services through their official APIs ([Google API](https://cloud.google.com/translate?hl=en), [DeepL API](https://www.deepl.com/en/pro-api)) to avoid these risks. I will not be held responsible for any consequences arising from such actions**.

## Requirements

To run the script you will need:-
- CMD or terminal access as Admin
- Git
- Python 3.11+
- At least one Next-Intl message file(eg:- "en.json")
- Exact ISO-639(set-1) language code (eg:- "en","es","de"...) of the source and target language.

## How To Run

1. Clone or download this repo.
2. Open terminal or CMD as admin and run `run.bat` for Windows, and `run.sh` for UNIX like systems.
3. After the dependencies have installed you will be asked for 
   - The path to your Next-Intl message file.
   - The path to the folder you want to save the output. File names will be the ISO-639 code of the target language.
   - The ISO-639(set-1) code for your source language.
   - The ISO-639(set-1) code for your target language.
   - The translation engine you want to use. (Results will vary depending on the engine you choose). 

