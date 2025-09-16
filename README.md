# 📂 File Organizer Script (Python)

This Python script helps you **organize files in a directory** into categorized folders based on their extensions.  
It automatically moves files into subfolders like `documents/`, `pictures/`, `media/`, etc.

---

## 🚀 Features

- Sorts files by type:

  - 📄 **Documents** → `.pdf`, `.docx`, `.txt`, `.csv`, `.xls`, `.pptx`, etc.
  - 📦 **Archives** → `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, etc.
  - 🖼 **Pictures** → `.jpg`, `.png`, `.gif`, `.svg`, etc.
  - 🎬 **Media (Videos)** → `.mp4`, `.avi`, `.mkv`, `.mov`, etc.
  - 🎵 **Audio** → `.mp3`, `.wav`, `.flac`, `.aac`, etc.
  - ⚙️ **Apps** → `.exe`, `.apk`, `.bat`, `.cmd`, etc.
  - 💻 **Code** → `.py`, `.cpp`, `.java`, `.js`, `.html`, etc.
  - 🛠 **System Files** → `.sys`, `.dll`, `.ini`, `.tmp`, etc.
  - 📥 **Installers** → `.msi`
  - 💾 **Saves** → `.save`, `.dat`, `.bak`
  - 📂 **Others** → Any file not matching above categories

- Creates new folders automatically if they don’t exist.
- Ignores directories (only works on files).
- Handles errors safely with warnings.

---

## 🖥️ Usage

1. Clone or download this script.
2. Run the script in Python:

   ```bash
   python file_organizer.py
   ```

3. Enter the directory path when prompted:
   Enter the directory to organize: C:\Users\YourName\Downloads
4. Files will be automatically sorted into appropriate folders.

📌 Example

Before running:
Downloads/
├── resume.pdf
├── movie.mp4
├── setup.exe
├── song.mp3
├── notes.txt
├── randomfile.xyz

After running:
Downloads/
├── documents/
│ ├── resume.pdf
│ ├── notes.txt
├── media/
│ ├── movie.mp4
├── apps/
│ ├── setup.exe
├── audio/
│ ├── song.mp3
├── others/
│ ├── randomfile.xyz
