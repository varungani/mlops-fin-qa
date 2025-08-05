import requests
import os

def extract_text_from_file(file_path, api_key=None):
    """
    Extracts structured text from an image or PDF using OCR.Space API.
    """
    if not api_key:
        raise ValueError("Please provide a valid OCR.Space API key")

    url = 'https://api.ocr.space/parse/image'

    payload = {
        'isOverlayRequired': True,
        'OCREngine': 2,
        'isTable': True,
        'detectOrientation': True,
        'scale': True,
        'OCREngine': 2,
        'filetype': 'PDF' if file_path.lower().endswith('.pdf') else 'JPG'
    }

    with open(file_path, 'rb') as f:
        files = {
            'file': (os.path.basename(file_path), f)
        }
        headers = {
            'apikey': api_key
        }

        response = requests.post(url, data=payload, files=files, headers=headers)

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        print("Error:", result.get("ErrorMessage"))
        return None

    parsed_results = result.get("ParsedResults")
    if not parsed_results:
        print("No parsed results.")
        return None

    return parsed_results[0]["ParsedText"]

# Example usage
if __name__ == "__main__":
    api_key = "K87753573188957"
    file_path = "src\pnlsheet.pdf"

    text = extract_text_from_file(file_path, api_key=api_key)
    if text:
        print("------ Extracted Text ------")
        print(text)
