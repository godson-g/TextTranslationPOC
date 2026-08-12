from deep_translator import GoogleTranslator
from app.logger import logger


def translate_text(text: str, target_language: str) -> str:
    """
    Translate text into the selected language.
    """

    try:
        logger.info(f"Translation requested -> {target_language}")

        translated = GoogleTranslator(
            target=target_language
        ).translate(text)

        logger.info("Translation completed successfully.")

        return translated

    except Exception as exc:
        logger.error(f"Translation failed: {exc}")
        raise