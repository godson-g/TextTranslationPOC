from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Text Translation API",
    description="Translate text into multiple languages using Google Translator.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def health():
    return {
        "status": "success",
        "message": "Text Translation API is running."
    }