# Text Translation Application Using Python

## Project Overview

This project is a Python-based Text Translation Application developed using **FastAPI** and the **deep-translator** library. The application allows users to translate single-line and multi-line text into a selected target language through a REST API.

The project follows modular coding practices, includes input validation, exception handling, logging, and automatic API documentation using Swagger UI.

---

## Features

- Translate text into multiple languages
- Supports both single-line and multi-line input
- Retrieve the list of supported languages
- Input validation for empty text
- Validation for unsupported language codes
- Graceful error handling for translation service failures
- Request logging for easier debugging
- Interactive API documentation using Swagger UI

---

## Technologies Used

- Python 3.13
- FastAPI
- deep-translator
- Uvicorn
- Pydantic

---

## Project Structure

```
TextTranslationPOC/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── translator.py
│   ├── schemas.py
│   ├── languages.py
│   ├── exceptions.py
│   └── logger.py
│
├── sample/
│   ├── sample_input.txt
│   └── sample_output.txt
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

or download the ZIP file.

### 2. Navigate to the project

```bash
cd TextTranslationPOC
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Execution

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET /**

Returns the application status.

---

### Supported Languages

**GET /languages**

Returns all languages supported by Google Translator.

---

### Translate Text

**POST /translate**

Request Body

```json
{
  "text": "Hello, how are you?",
  "target_language": "ta"
}
```

Response

```json
{
  "original_text": "Hello, how are you?",
  "translated_text": "வணக்கம், நலமா?",
  "target_language": "ta"
}
```

---

## Sample Input

```text
Hello, how are you?
Target Language: ta
```

---

## Sample Output

```text
Original Text:
Hello, how are you?

Translated Text:
வணக்கம், நலமா?

Target Language:
ta
```

---

## Error Handling

The application handles the following scenarios:

- Empty input text
- Unsupported language code
- Translation service failures
- Invalid API requests

Example Error Response

```json
{
  "detail": "Text cannot be empty."
}
```

---

## Assumptions

- An active internet connection is required for translation.
- Language codes should match the supported codes returned by the `/languages` endpoint.
- The translation output depends on the Google Translate service provided by the `deep-translator` library.

---

## Logging

Application logs are stored in:

```
logs/app.log
```

The log file records translation requests, successful operations, and errors for debugging purposes.

---

## Future Enhancements

- Language name support instead of language codes
- Translation history
- Authentication and authorization
- Docker deployment
- Unit testing

---

## Author

**Godson G**

Python POC – Text Translation Application

Developed as part of the Pixstech Internship Proof of Concept (POC).