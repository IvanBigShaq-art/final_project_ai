import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

client = OpenAI(api_key=api_key)


def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user",
                 "content": f"Summarize this lecture for a student: {text}"}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"AI error: {e}")
        return None


def generate_questions(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user",
                 "content": f"Generate 5 study questions based on this lecture text. "
                            f"Number each question. Text: {text}"}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"AI error: {e}")
        return None


def answer_question(question, context):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user",
                 "content": f"You are a helpful study assistant. "
                            f"Answer the student's question based on the lecture notes provided.\n\n"
                            f"Lecture notes:\n{context}\n\n"
                            f"Student question: {question}"}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"AI error: {e}")
        return None