import tkinter as tk
from tkinter import scrolledtext

def popup_win(new_entries):

    root = tk.Tk()
    root.title("PSW Updates")

    # Set wider window
    root.geometry("900x450")

    if not new_entries:
        label = tk.Label(root, text="No new unique entries added.", font=("Arial", 12))
        label.pack(pady=20)
        return

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 11))
    # Courier New = monospaced (column alignment looks perfect)
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    text_area.insert(tk.END, f"{len(new_entries)} new entries added:\n\n")

    # Column headers (optional)
    header = f"{'Column1':<25}{'Column2':<25}{'Column3':<25}{'Column5':<25}\n"
    text_area.insert(tk.END, header)
    text_area.insert(tk.END, "-" * 100 + "\n")

    # Add each row with fixed-width formatting
    for row in new_entries:
        formatted = f"{row[0]:<25}{row[1]:<25}{row[2]:<25}{row[3]:<25}\n"
        text_area.insert(tk.END, formatted)

    text_area.config(state="disabled")

    root.mainloop()
