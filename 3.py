# password generator
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        include_digits = digits_var.get()
        include_special = special_var.get()

        characters = string.ascii_letters
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "⚠ Please select at least one character type.")
            return

      
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")


def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "✅ Password copied to clipboard!")

root = tk.Tk()
root.title("🔐 Elegant Password Generator")

win_w, win_h = 450, 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int((screen_w - win_w) / 2)
y = int((screen_h - win_h) / 2)
root.geometry(f"{win_w}x{win_h}+{x}+{y}")

root.configure(bg="#1f1f2e")
root.resizable(False, False)

# MAIN GUI
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_ENTRY = ("Consolas", 14)
COLOR_PRIMARY = "#6c5ce7"
COLOR_HOVER = "#a29bfe"
COLOR_SUCCESS = "#00b894"

tk.Label(root, text="Secure Password Generator", font=FONT_TITLE, bg="#1f1f2e", fg="white").pack(pady=20)

length_frame = tk.Frame(root, bg="#1f1f2e")
length_frame.pack(pady=10)

tk.Label(length_frame, text="Length:", font=FONT_LABEL, bg="#1f1f2e", fg="white").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5, font=FONT_ENTRY, justify="center",
                        bg="#2d2d44", fg="white", relief="flat")
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT, padx=10)

checkbox_frame = tk.Frame(root, bg="#1f1f2e")
checkbox_frame.pack(pady=10)

digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(checkbox_frame, text="Include Numbers", variable=digits_var, font=FONT_LABEL,
               bg="#1f1f2e", fg="white", selectcolor="#2d2d44", activebackground="#1f1f2e").pack(anchor='w')

tk.Checkbutton(checkbox_frame, text="Include Special Characters", variable=special_var, font=FONT_LABEL,
               bg="#1f1f2e", fg="white", selectcolor="#2d2d44", activebackground="#1f1f2e").pack(anchor='w')

result_entry = tk.Entry(root, font=FONT_ENTRY, justify='center',
                        bg="#2d2d44", fg="#00ffcc", relief="flat", bd=4)
result_entry.pack(pady=15, padx=20, fill=tk.X)

def on_enter(e): e.widget.config(bg=COLOR_HOVER)
def on_leave(e): e.widget.config(bg=COLOR_PRIMARY)


btn_generate = tk.Button(root, text="Generate Password", font=FONT_LABEL,
                         bg=COLOR_PRIMARY, fg="white", command=generate_password,
                         relief="flat", padx=10, pady=6)
btn_generate.pack(pady=10)
btn_generate.bind("<Enter>", on_enter)
btn_generate.bind("<Leave>", on_leave)

btn_copy = tk.Button(root, text="Copy to Clipboard", font=FONT_LABEL,
                     bg=COLOR_SUCCESS, fg="white", command=copy_to_clipboard,
                     relief="flat", padx=10, pady=6)
btn_copy.pack(pady=5)
btn_copy.bind("<Enter>", lambda e: btn_copy.config(bg="#55efc4"))
btn_copy.bind("<Leave>", lambda e: btn_copy.config(bg=COLOR_SUCCESS))

root.mainloop()
