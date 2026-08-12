from fastapi import APIRouter

from app.languages import get_supported_languages
from app.schemas import TranslationRequest, TranslationResponse
from app.translator import translate_text
from app.exceptions import (
    empty_text_exception,
    invalid_language_exception,
    translation_service_exception,
)

router = APIRouter()


@router.get("/languages")
def get_languages():
    """
    Returns all supported languages.
    """
    return get_supported_languages()


@router.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    """
    Translate the given text into the selected language.
    """

    if not request.text.strip():
        empty_text_exception()

    supported_languages = get_supported_languages()

    target_language = request.target_language.strip().lower()

    # Accept both language names and language codes
    if target_language in supported_languages:
        language_code = supported_languages[target_language]

    elif target_language in supported_languages.values():
        language_code = target_language

    else:
        invalid_language_exception()

    try:
        translated_text = translate_text(
            request.text,
            language_code,
        )

        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            target_language=target_language,
        )

    except Exception:
        translation_service_exception()
