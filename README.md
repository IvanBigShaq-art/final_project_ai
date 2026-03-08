🎓 Student AI Assistant
A command-line tool that helps students manage tasks and study smarter using AI.
Features

✅ Task manager — add and view tasks with deadlines
📝 Lecture summarizer — paste any lecture text and get a short summary saved to your notes
❓ Study question generator — generate 5 questions from a lecture to test yourself
🤖 Ask AI about your notes — ask any question and get an answer based on your saved notes

Tech Stack

Python 3
SQLite — local database for tasks and notes
OpenAI API (GPT-4o-mini) — AI features
python-dotenv — secure API key management

Project Structure
final_project_ai/
├── main.py          # Menu and all app logic
├── database.py      # Database setup
├── ai_service.py    # OpenAI API functions
├── database.db      # Auto-generated SQLite database
├── .env             # Your API key (not uploaded to GitHub)
└── .env.example     # Template for .env
Installation

Clone the repository:

bashgit clone https://github.com/your-username/final_project_ai.git
cd final_project_ai

Install dependencies:

bashpip install openai python-dotenv

Create a .env file based on .env.example:

OPENAI_API_KEY=your_api_key_here

Run the app:

bashpython main.py
Usage
--- Menu ---
1. Add task
2. Show tasks
3. Summarize lecture
4. Generate study questions
5. Ask AI about notes
6. Exit
