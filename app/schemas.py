from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    """Request model for text translation."""

    text: str = Field(
        ...,
        min_length=1,
        description="Text to translate",
    )

    target_language: str = Field(
        ...,
        min_length=2,
        description="Target language name or language code, e.g. tamil or ta",
        examples=["string"],
    )


class TranslationResponse(BaseModel):
    """Response model for translated text."""

    original_text: str
    translated_text: str
    target_language: str