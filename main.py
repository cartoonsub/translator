import deepl
import pprint as pp

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
    
def main() -> None:
    translator = TextTranslator()
    lines = getFileLines()
    for numLine, line in enumerate(lines):
        pp.pprint(f"Line {numLine}: {line}")


    return
    text = translator.translate_text("Hello, world!", "ru")
    print(text)


if __name__ == "__main__":
    main()