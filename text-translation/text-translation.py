from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

# print all supported languages
#print("Total supported languages:", len(constants.LANGUAGES))
#print("Languages:")
#pprint(constants.LANGUAGES)

# translate a spanish text to english text (by default)
translation = translator.translate("Hola Mundo")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# translate a japanese text to english text (by default)
translation = translator.translate("こん に ち は 世 界")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
