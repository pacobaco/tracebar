import tkinter as tk
import pyperclip

def show_summary(summary_text="", filename=""):
    window = tk.Tk()
    window.title("NER Summary")
    window.geometry("500x400")
    tk.Label(window, text=f"{filename}", font=("Helvetica", 12, "bold")).pack(pady=5)
    text_box = tk.Text(window, wrap="word", font=("Courier", 10))
    text_box.insert("1.0", summary_text)
    text_box.pack(expand=True, fill="both", padx=10, pady=5)
    tk.Button(window, text="Copy to Clipboard", command=lambda: pyperclip.copy(summary_text)).pack(pady=10)
    window.mainloop()
