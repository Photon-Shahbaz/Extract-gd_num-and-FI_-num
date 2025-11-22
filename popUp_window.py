import tkinter as tk
from tkinter import messagebox


def popup_win(new_entries):
    if new_entries:
        msg = f"{len(new_entries)} new entries added:\n\n"
        for row in new_entries:
            msg += ", ".join(row) + "\n"

        root = tk.Tk()
        root.withdraw()  # Hide main window
        messagebox.showinfo("PSW Updates", msg)
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("PSW Updates", "No new unique entries added.")
