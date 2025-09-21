import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Generate a random number between 1 and 100
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.title_label = tk.Label(
            root, text="Guess a Number (1 - 100)", font=("Arial", 16)
        )
        self.title_label.pack(pady=10)

        # Input field
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(
            root, text="Guess", font=("Arial", 12), command=self.check_guess
        )
        self.submit_button.pack(pady=5)

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(
            root, text="Restart", font=("Arial", 12), command=self.restart_game
        )
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(
                    text=f"{guess} is too low! Try again.", fg="blue"
                )
            elif guess > self.secret_number:
                self.feedback_label.config(
                    text=f"{guess} is too high! Try again.", fg="orange"
                )
            else:
                self.feedback_label.config(
                    text=f"🎉 Correct! The number was {self.secret_number}.\nAttempts: {self.attempts}",
                    fg="green",
                )
                self.submit_button.config(state="disabled")  # Disable after win
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="", fg="black")
        self.submit_button.config(state="normal")


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
