import os
import tkinter as tk
from tkinter import filedialog, messagebox
import logging
from datetime import datetime

class GermanCharacterReplacer:
    def __init__(self, master):
        self.master = master
        master.title("German Character Replacer")
        master.geometry("400x300")

        self.folder_path = tk.StringVar()
        self.replacements = {
            'ß': 'SS',
            'Ü': 'Ue', 'ü': 'ue',
            'Ö': 'Oe', 'ö': 'oe',
            'Ä': 'Ae', 'ä': 'ae'
        }

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select folder:").pack(pady=10)
        tk.Entry(self.master, textvariable=self.folder_path, width=50).pack()
        tk.Button(self.master, text="Browse", command=self.browse_folder).pack(pady=5)

        for char, replacement in self.replacements.items():
            frame = tk.Frame(self.master)
            frame.pack(fill=tk.X, padx=20, pady=5)
            tk.Label(frame, text=f"Replace {char} with:").pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=10)
            entry.insert(0, replacement)
            entry.pack(side=tk.RIGHT)
            self.replacements[char] = entry

        tk.Button(self.master, text="Start Renaming", command=self.start_renaming).pack(pady=20)

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
                    if char.isupper():
                        new_name = new_name.replace(char, replacement.capitalize())
                    else:
                        new_name = new_name.replace(char, replacement.lower())
                
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