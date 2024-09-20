import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("300x250")
        frame = tk.Frame(self.root, bg='lightblue')
        frame.place(relwidth=1, relheight=1)
        
        self.rand_number = random.randint(1, 100)
        self.attempts = 0

        # Create and place widgets
        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="",bg="lightblue")
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < 1 or guess > 100:
                self.result_label.config(text="Please enter a number between 1 and 100.",bg="yellow")
            elif guess < self.rand_number:
                self.result_label.config(text="Number is Too low! Try again.",bg="yellow")
            elif guess > self.rand_number:
                self.result_label.config(text="Number is Too high! Try again.",bg="yellow")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                messagebox.showinfo("Game Over", f"You guessed the number {self.rand_number} in {self.attempts} attempts!")
                self.entry.config(state="disabled")
                self.guess_button.config(state="disabled")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        self.rand_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.result_label.config(text="",bg="lightblue")
        self.entry.delete(0, tk.END)

# Create the main window and start the game
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
