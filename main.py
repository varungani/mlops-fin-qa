from src.extraction import extract_text_from_file
from src.qa import ask_question

def main():
    print("=== FinDocIQ Terminal QA ===")

    # Ask user for the PDF or image file
    file_path = input("Enter path to PDF or image file: ").strip()
    
    # Your OCR.Space API key
    api_key = "K87753573188957"

    print("\n[INFO] Extracting text from document...")
    try:
        extracted_text = extract_text_from_file(file_path, api_key=api_key)

        if not extracted_text:
            print("[ERROR] Could not extract any text from the file.")
            return
        
        print("\n[INFO] Text extracted successfully.\n")
        print("You can now ask questions about the document.")
        print("Type 'exit' to quit.\n")

        while True:
            user_question = input("Ask a question: ").strip()
            if user_question.lower() in ['exit', 'quit']:
                print("Exiting QA.")
                break

            answer = ask_question(context=extracted_text, question=user_question)
            print(f"\n[Answer]: {answer}\n")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
