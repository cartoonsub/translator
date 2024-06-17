import deepl
import pprint as pp
import re
from time import sleep


class TextTranslator:
    def __init__(self) -> None:
        self.apiKey = self.getApiKey()
        if self.apiKey == "":
            raise ValueError("API key is empty")
        
        self.Translator = deepl.Translator(self.apiKey)

    def getApiKey(self) -> str:
        with open('files/apikey.txt', 'r') as file:
            return file.read().replace('\n', '')

    def translate_text(self, text: str, target_lang: str) -> str:
        result = self.Translator.translate_text(text, target_lang=target_lang)
        return result.text


def getFileLines() -> list:
    with open('files/snowDay.subtitlefile', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        return lines

def saveFileLines(lines: list) -> None:
    with open('files/snowDay.subtitlefile', 'w+', encoding='utf-8') as file:
        file.writelines(lines)

def main() -> None:
    translator = TextTranslator()
    lines = getFileLines()
    if lines == None:
        return
    
    pattern = r"(^Dialogue:.+?,,0,0,0,,)(.+)"
    for numLine, line in enumerate(lines):
        if not re.match(pattern, line):
            continue
        
        match = re.search(pattern, line)
        firstText = match.group(1)
        text = match.group(2)
        translatedText = translator.translate_text(text, "ru")
        newLine = firstText + text + "'bigBugHere'" + translatedText + "\n"
        lines[numLine] = newLine
        print('Translated:', text, '->', translatedText)
        
        if numLine % 10 == 0:
            print(f"Translated {numLine} lines")
            sleep(1)

    saveFileLines(lines)
    print("All lines translated")


if __name__ == "__main__":
    main()