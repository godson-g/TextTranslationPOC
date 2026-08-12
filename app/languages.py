from deep_translator import GoogleTranslator

# Load supported languages once when the application starts
SUPPORTED_LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)


def get_supported_languages():
    """
    Returns all languages supported by Google Translator.
    """
    return SUPPORTED_LANGUAGES