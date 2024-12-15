import tkinter as tk
from tkinter import messagebox, simpledialog

# 1. utworzenie głównego okna aplikacji
window = tk.Tk()

# 2. Tytuł okna
window.title("Lista zakupów")

# 3. Rozmiar okna (szer x wys)
window.geometry("600x600")

tk.Label(window, text="Lista zakupów", font=("Arial, 20")).pack(pady=10)

# Uruchomienie aplikacji w pętli głównej
window.mainloop()