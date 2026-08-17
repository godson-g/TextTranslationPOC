# Text Translation Application Using Python

## Project Overview

This project is a Python-based Text Translation Application developed using **FastAPI** and the **deep-translator** library. The application allows users to translate single-line and multi-line text into a selected target language through a REST API and a web-based user interface.

The project follows modular coding practices, includes input validation, exception handling, logging, and automatic API documentation using Swagger UI.

---

## Features

- Translate text into multiple languages
- Supports both single-line and multi-line input
- Web-based user interface for easy translation
- Target language selection using a dropdown
- Retrieve the list of supported languages
- Supports target language names and language codes (e.g., tamil or ta)
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
- HTML
- CSS
- JavaScript
- Jinja2

---

## Project Structure

```text
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
│   ├── Error Handling.png
│   ├── Error Handling 1.png
│   ├── Multiline Text.png
│   └── Sample Output.png
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/godson-g/TextTranslationPOC.git
```

Or download the project ZIP file.

---

### 2. Navigate to the Project

```bash
cd TextTranslationPOC
```

---

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

---

### 5. Install Dependencies

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

```text
http://127.0.0.1:8000
```

---

## Web Application

Open the following URL in a browser:

```text
http://127.0.0.1:8000/
```

The web interface allows users to:

- Enter text for translation
- Enter single-line or multi-line text
- Select a target language from the dropdown
- Translate the entered text
- View the translated output

---

## Swagger Documentation

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the available API endpoints directly from the browser.

---

## Web Application Usage

### Step 1: Enter Text

Enter the text that needs to be translated in the text box.

Example:

```text
Hello, how are you?
```

The application also supports multi-line input.

Example:

```text
Hello
How are you?
Good Morning
```

---

### Step 2: Select Target Language

Select the required target language from the dropdown.

Example:

```text
Tamil
```

The application also supports language codes such as:

```text
ta
```

---

### Step 3: Click Translate

Click the **Translate** button.

The translated text will be displayed in the **Translated Text** section.

---

## API Endpoints

### Health Check

**GET /**

Returns the application status and loads the web interface.

---

### Supported Languages

**GET /languages**

Returns the list of languages supported by the translation service.

---

### Translate Text

**POST /translate**

Translates the provided text into the selected target language.

#### Request Body

```json
{
  "text": "Hello, how are you?",
  "target_language": "tamil"
}
```

#### Example Response

```json
{
  "original_text": "Hello, how are you?",
  "translated_text": "வணக்கம், நலமா?",
  "target_language": "tamil"
}
```

---

## Sample Input and Output

### Sample 1

#### Input

```text
Input Text:
Hello, how are you?

Target Language:
ta
```

#### Output

```text
Original Text:
Hello, how are you?

Translated Text:
வணக்கம், நலமா?

Target Language:
ta
```

---

### Sample 2

#### Input

```text
Input Text:
Good Morning

Target Language:
te
```

#### Output

```text
Original Text:
Good Morning

Translated Text:
శుభోదయం

Target Language:
te
```

---

### Sample 3 - Multi-line Input

#### Input

```text
Input Text:
Hello
How are you?
Good Morning

Target Language:
ta
```

#### Output

```text
Original Text:
Hello
How are you?
Good Morning

Translated Text:
வணக்கம்
எப்படி இருக்கிறீர்கள்?
காலை வணக்கம்

Target Language:
ta
```

The application supports multi-line input and preserves the line structure in the translated output.

---

## Error Handling

The application handles the following scenarios:

- Empty input text
- Unsupported language code or language name
- Translation service failures
- Invalid API requests
- Network-related translation service failures

### 1. Empty Text

If the user submits empty text, the application returns an appropriate validation error.

Example:

```json
{
  "detail": "Text cannot be empty."
}
```

---

### 2. Unsupported Language

If an unsupported language code or language name is provided, the application returns an appropriate validation error.

---

### 3. Translation Service Failure

If the external translation service is unavailable or a network failure occurs, the application handles the exception gracefully instead of crashing.

---

### 4. Invalid API Request

FastAPI and Pydantic validation handle invalid request formats and return appropriate HTTP error responses.

---

## Logging

The application generates runtime logs for debugging and monitoring.

Runtime log files are excluded from Git tracking because generated log files should not be committed to the repository.

The `.gitignore` file contains:

```text
logs/
*.zip
```

Therefore:

- Runtime logs are kept locally.
- ZIP files are not committed to Git.
- The source repository remains clean.

---

## Screenshots

The project contains screenshots demonstrating the application's functionality.

Available screenshots include:

- Web application interface
- Multi-line text translation
- Sample translation output
- Error handling

Screenshots are available in:

```text
screenshots/
```

---

## Assumptions

- An active internet connection is required for translation.
- Target language can be provided using a supported language name or language code, such as `tamil` or `ta`.
- The translation output depends on the Google Translate service provided by the `deep-translator` library.
- Translation service availability may affect translation requests.

---

## Future Enhancements

Possible future improvements include:

- Translation history
- Authentication and authorization
- Database integration
- Unit and integration testing
- Docker deployment
- Additional translation providers
- Improved UI/UX
- Rate limiting
- Cloud deployment

---

## Author

**Godson G**

Python POC – Text Translation Application

Developed as part of the **Pixstech Internship Proof of Concept (POC)**.