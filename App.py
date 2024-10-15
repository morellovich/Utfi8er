import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging
from datetime import datetime

class GermanCharacterReplacer:
    def __init__(self, master):
        self.master = master
        master.title("German Character Replacer")
        master.geometry("500x400")  # Increased window size

        self.folder_path = tk.StringVar()
        self.replacements = {
            'ß': 'SS',
            'Ü': 'Ue',
            'Ö': 'Oe',
            'Ä': 'Ae'
        }

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select folder:").pack(pady=10)
        tk.Entry(self.master, textvariable=self.folder_path, width=50).pack()
        tk.Button(self.master, text="Browse", command=self.browse_folder).pack(pady=5)

        self.replacements_frame = ttk.Frame(self.master)
        self.replacements_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.create_replacement_widgets()

        tk.Button(self.master, text="Add New Replacement", command=self.add_replacement).pack(pady=5)
        tk.Button(self.master, text="Start Renaming", command=self.start_renaming).pack(pady=10)

    def create_replacement_widgets(self):
        for widget in self.replacements_frame.winfo_children():
            widget.destroy()

        for i, (char, replacement) in enumerate(self.replacements.items()):
            frame = ttk.Frame(self.replacements_frame)
            frame.pack(fill=tk.X, pady=2)

            tk.Label(frame, text=f"Replace {char} with:").pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=10)
            entry.insert(0, replacement)
            entry.pack(side=tk.LEFT, padx=(0, 10))

            tk.Button(frame, text="Remove", command=lambda c=char: self.remove_replacement(c)).pack(side=tk.RIGHT)

            self.replacements[char] = entry

    def add_replacement(self):
        new_char = tk.simpledialog.askstring("New Replacement", "Enter the character to replace:")
        if new_char:
            self.replacements[new_char] = 'New'
            self.create_replacement_widgets()

    def remove_replacement(self, char):
        del self.replacements[char]
        self.create_replacement_widgets()

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def start_renaming(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return

        log_file = f"renaming_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        logging.basicConfig(filename=log_file, level=logging.INFO, 
                            format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        replacements = {k: v.get() for k, v in self.replacements.items()}
        
        for root, dirs, files in os.walk(folder):
            for name in dirs + files:
                new_name = name
                for char, replacement in replacements.items():
                    new_name = new_name.replace(char, replacement)
                    new_name = new_name.replace(char.lower(), replacement.lower())
                
                if new_name != name:
                    old_path = os.path.join(root, name)
                    new_path = os.path.join(root, new_name)
                    os.rename(old_path, new_path)
                    logging.info(f"Renamed: {old_path} -> {new_path}")

        messagebox.showinfo("Success", f"Renaming complete. Log file created: {log_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GermanCharacterReplacer(root)
    root.mainloop()