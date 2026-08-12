from fastapi import HTTPException


def empty_text_exception():
    """
    Raised when the input text is empty.
    """
    raise HTTPException(
        status_code=400,
        detail="Text cannot be empty."
    )


def invalid_language_exception():
    """
    Raised when an unsupported language code is provided.
    """
    raise HTTPException(
        status_code=400,
        detail="Unsupported language."
    )


def translation_service_exception():
    """
    Raised when the translation service is unavailable.
    """
    raise HTTPException(
        status_code=503,
        detail="Translation service is currently unavailable. Please try again later."
    )