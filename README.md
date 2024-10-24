# utfi8er

utfi8er is a Python GUI application designed to rename files and folder names by replacing specific German characters (e.g. 'ß', 'Ü', 'Ö', 'Ä') with their standard equivalents ('SS', 'Ue', 'Oe', 'Ae'). It also allows for customizable character replacements through a user-friendly interface.

## 🎯 Purpose

- The app scans a specific user defined folder and its subfolders & files
- It then replaces the non-utf8 characters with their standard equivalents.
- The user can define the replacement rules in the GUI.
- The app will then rename all files and folders accordingly.
- The app respects the original _upper/lower case_ state.
- The user can also choose to save the original names in a log file.

## ⚙️ Features

- Replace specific German characters with user-defined alternatives.
- Supports both folder and file renaming.
- Provides a simple interface to add new character replacements.
- Generates detailed logs of all renaming actions.

## 🛠️ Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/utfi8er.git
cd utfi8er
```

### 2. Install Dependencies

This project requires `tkinter` for the GUI, which is included by default in most Python installations. You'll also need `logging`, `os`, and other standard Python libraries. You can install any missing dependencies by running:

```bash
pip install tk
```

### 3. Update PATH (Optional)

Make sure your Python and `pip` executables are added to your system’s PATH to ensure the dependencies are correctly installed and can be accessed.

On **Windows**:

- Open Control Panel and go to `System > Advanced system settings > Environment Variables`.
- Select `Path` under System Variables and click Edit.
- Add the paths to your Python and `pip` installations (e.g., `C:\Python39\Scripts` and `C:\Python39\`).

## 📝 How to Use

1. **Launch the Application**
   Run the script by navigating to the directory and executing:

   ```bash
   python utfi8er.py
   ```

   This will open the `German Character Replacer` GUI.

2. **Select a Folder**

   - Click the "Browse" button to select the folder containing the files and directories you wish to rename.

3. **Modify Replacement Rules**

   - The app displays default replacements for German characters: 'ß' -> 'SS', 'Ü' -> 'Ue', 'Ö' -> 'Oe', 'Ä' -> 'Ae'.
   - You can modify these by typing directly into the text fields.
   - To add new replacements, click the "Add New Replacement" button, enter the new character, and specify its replacement.

4. **Start Renaming**
   - After setting the folder and adjusting the replacement rules, click "Start Renaming".
   - The app will traverse through all files and folders in the selected directory, applying the replacements.
   - A success message will appear when the process is complete, and a log file (`renaming_log_YYYYMMDD_HHMMSS.txt`) will be generated with details of all renaming actions.

## 🛡️ Logging

A log file is created with every renaming process. The file is saved in the same directory as the script and contains information like:

- Original file/folder name
- New file/folder name
- Date and time of renaming

## ⚠️ Note

- Be cautious when using this tool, as renaming files might affect file references or dependencies in other programs.
- The app attempts to replace both uppercase and lowercase instances of the characters.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

---
