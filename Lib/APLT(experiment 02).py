import tkinter as tk
from tkinter import messagebox

class LearningTutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learning Tutor App")
        self.root.geometry("400x300")

        self.question_label = tk.Label(root, text="Question will appear here", wraplength=300, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 5 + 7?", "answer": "12"},
            {"question": "What is the color of the sky?", "answer": "Blue"}
        ]
        self.current_question_index = 0
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index]["question"])
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.question_label.config(text="Congratulations! You've completed all questions.")
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.feedback_label.config(text="Correct!", fg="green")
            self.current_question_index += 1
            self.root.after(1000, self.load_question)
        else:
            self.feedback_label.config(text="Try again!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LearningTutorApp(root)
    root.mainloop()
