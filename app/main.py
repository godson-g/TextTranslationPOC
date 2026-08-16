from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import router


app = FastAPI(
    title="Text Translation API",
    description="Translate text into multiple languages using Google Translator.",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


# Frontend Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Health Check
@app.get("/health")
def health():
    return {
        "status": "success",
        "message": "Text Translation API is running."
    }