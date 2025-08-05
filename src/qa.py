import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def ask_question(context: str, question: str, model: str = "mistralai/mistral-7b-instruct") -> str:
    if not context.strip():
        return "Context is empty. Cannot answer."

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant that answers questions based on provided financial document context."},
                {"role": "user", "content": f"Context:\n{context}"},
                {"role": "user", "content": f"Question:\n{question}"}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Error during LLM query: {e}"
if __name__ == "__main__":
    sample_context = """
    Invoice No: 9348
    Date: 2024-06-01
    Billed To: John Doe, Acme Inc.
    Items:
    - Widget A: $50
    - Widget B: $30
    Total: $80
    """
    q = "How much was charged for Widget B?"
    answer = ask_question(sample_context, q)
    print("Answer:", answer)
