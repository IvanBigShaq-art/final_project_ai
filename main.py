import sqlite3
from database import init_db, DB_NAME
from ai_service import summarize_text, generate_questions, answer_question


def connect_db():
    return sqlite3.connect(DB_NAME)


def add_task():
    title = input("Task title: ").strip()
    if not title:
        print("Error: title cannot be empty.")
        return

    deadline = input("Deadline (e.g. 2025-12-31): ").strip()

    try:
        with connect_db() as conn:
            conn.execute(
                "INSERT INTO tasks (title, deadline) VALUES (?, ?)",
                (title, deadline)
            )
            conn.commit()
        print("Task added successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")


def show_tasks():
    try:
        with connect_db() as conn:
            tasks = conn.execute("SELECT * FROM tasks").fetchall()

        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- Your Tasks ---")
            for task in tasks:
                print(f"[{task[0]}] {task[1]} | Deadline: {task[2]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")


def summarize():
    text = input("Paste lecture text:\n").strip()
    if not text:
        print("Error: text cannot be empty.")
        return

    print("Summarizing, please wait...")
    summary = summarize_text(text)

    if summary is None:
        print("Failed to get summary. Try again later.")
        return

    try:
        with connect_db() as conn:
            conn.execute(
                "INSERT INTO notes (text, summary) VALUES (?, ?)",
                (text, summary)
            )
            conn.commit()

        print("\n--- Summary ---")
        print(summary)

    except sqlite3.Error as e:
        print(f"Database error: {e}")


def questions_from_lecture():
    text = input("Paste lecture text:\n").strip()
    if not text:
        print("Error: text cannot be empty.")
        return

    print("Generating questions, please wait...")
    questions = generate_questions(text)

    if questions is None:
        print("Failed to generate questions. Try again later.")
        return

    print("\n--- Study Questions ---")
    print(questions)


def ask_ai():
    try:
        with connect_db() as conn:
            notes = conn.execute("SELECT id, summary FROM notes").fetchall()

        if not notes:
            print("No saved notes found. Please summarize a lecture first.")
            return

        print("\n--- Your Notes ---")
        for note in notes:
            preview = note[1][:60] + "..." if len(note[1]) > 60 else note[1]
            print(f"[{note[0]}] {preview}")

        note_id = input("\nEnter note ID to ask about (or press Enter to use all): ").strip()

        if note_id:
            with connect_db() as conn:
                result = conn.execute(
                    "SELECT text FROM notes WHERE id = ?", (note_id,)
                ).fetchone()

            if not result:
                print("Note not found.")
                return

            context = result[0]
        else:
            with connect_db() as conn:
                all_notes = conn.execute("SELECT text FROM notes").fetchall()
            context = "\n\n".join([n[0] for n in all_notes])

        question = input("\nYour question: ").strip()
        if not question:
            print("Error: question cannot be empty.")
            return

        print("Thinking, please wait...")
        answer = answer_question(question, context)

        if answer is None:
            print("Failed to get answer. Try again later.")
            return

        print("\n--- Answer ---")
        print(answer)

    except sqlite3.Error as e:
        print(f"Database error: {e}")


def menu():
    print("Student AI Assistant started.")

    while True:
        print("\n--- Menu ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Summarize lecture")
        print("4. Generate study questions")
        print("5. Ask AI about notes")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            summarize()

        elif choice == "4":
            questions_from_lecture()

        elif choice == "5":
            ask_ai()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    init_db()
    menu()