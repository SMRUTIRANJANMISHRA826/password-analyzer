import re
import tkinter as tk
from tkinter import ttk

def check_password(event=None):
    password = entry.get()
    strength = 0
    remarks = []

    # Clear previous output
    progress['value'] = 0
    result_label.config(text="", fg="black")
    suggestion_box.delete("1.0", tk.END)

    # Conditions
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("• Minimum 8 characters")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks.append("• Add uppercase letter")

    if re.search("[a-z]", password):
        strength += 1
    else:
        remarks.append("• Add lowercase letter")

    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks.append("• Add number")

    if re.search("[@#$%^&*]", password):
        strength += 1
    else:
        remarks.append("• Add special character")

    # Update progress bar
    progress['value'] = strength * 20

    # Strength result
    if strength == 5:
        result_label.config(text="Strong Password", fg="green")
    elif strength >= 3:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Weak Password", fg="red")

    # Suggestions
    if remarks:
        suggestion_box.insert(tk.END, "Suggestions:\n")
        for r in remarks:
            suggestion_box.insert(tk.END, r + "\n")

# Show/Hide password
def toggle_password():
    if entry.cget('show') == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("450x420")
root.resizable(False, False)
title = tk.Label(root, text="Password Analyzer", font=("Arial", 18, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<KeyRelease>", check_password)  # live checking

toggle_btn = tk.Button(root, text="Show", command=toggle_password)
toggle_btn.pack()

progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

suggestion_box = tk.Text(root, height=6, width=40)
suggestion_box.pack(pady=10)

root.mainloop()