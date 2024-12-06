# Grammar and Spell Checker

A simple web application to correct spelling and grammar mistakes in text. Built using Flask, TextBlob, and LanguageTool, this tool helps identify and rectify errors in user-provided text or uploaded files.

## Features

- **Spell Correction**: Automatically corrects spelling mistakes in text.
- **Grammar Correction**: Identifies and corrects grammatical errors.
- **File Support**: Upload a text file for bulk corrections.
- **Interactive UI**: User-friendly web interface built with HTML and Bootstrap.

## Technologies Used

- **Backend**: Flask (Python)
- **Libraries**:
  - [TextBlob](https://textblob.readthedocs.io/en/dev/): For spelling corrections.
  - [LanguageTool](https://github.com/danielnaber/languagetool): For grammar corrections.
- **Frontend**: HTML, Bootstrap

## Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd grammar-and-spell-checker
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

### Spell Checker
1. Enter text into the input box.
2. Click the **Correct** button.
3. View the corrected text and grammar mistakes below the form.

### File Upload
1. Upload a `.txt` file using the file upload form.
2. Click the **Correct** button.
3. View the corrected text and grammar mistakes below the form.
