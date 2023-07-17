from deep_translator import MyMemoryTranslator

''' Creating functions that translate text. '''

def english_to_french(english_text):
    '''Using MyMemory Translator to translate English to French and store it in 
       variable french_text'''
    french_text = MyMemoryTranslator(source='english us', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Using MyMemory Translator to translate French to English and store it in 
       variable english_text'''
    english_text = MyMemoryTranslator(source='french', target='english us').translate(french_text)
    return english_text
