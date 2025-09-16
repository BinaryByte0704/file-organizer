import os
import shutil

extention_map = {
    "documents" : [".pdf",".docx",".txt",".doc", ".odt", ".rtf", ".csv", ".xls", ".xlsx", ".ppt", ".pptx", ".pub", ".pages", ".md"],
    "archives"  : [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "pictures"  : [".jpg",".jpeg",".webp",".avif",".png",".gif", ".bmp", ".tiff", ".tif", ".svg", ".ico", ".raw"],
    "media" : [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".mpeg", ".mpg", ".webm", ".3gp"],
    "audio" : [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".wma"],
    "apps" : [".exe",".app", ".apk", ".com", ".cmd", ".bat"],
    "code" : [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".json", ".xml",".ipynb",".sql"],
    "system"    : [".sys", ".ini", ".dll", ".tmp", ".cfg"],
    "installers" : [".msi"],
    "saves" : [".save", ".dat", ".sav", ".bak"],
}

directory = input("Enter the directory to organize: ")

if not os.path.isdir(directory):
    print("❌ The directory doesn't exist")
    exit()
else:
    print("✅ Directory accessed")

try:
    files = os.listdir(directory)
except Exception as e:
    print(f"❌ Error listing directory: {e}")
    exit()

for file in files:
    filepath = os.path.join(directory, file)

    # skip folders
    if os.path.isdir(filepath):
        continue

    filename, extension = os.path.splitext(file)
    moved = False

    try:
        for key, value in extention_map.items():
            if extension.lower() in value:
                target_folder = os.path.join(directory, key)

                if not os.path.isdir(target_folder):
                    try:
                        os.mkdir(target_folder)
                    except Exception as e:
                        print(f"⚠️ Could not create folder {target_folder}: {e}")
                        continue

                try:
                    shutil.move(filepath, os.path.join(target_folder, file))
                    print(f"✅ Moved: {file} → {key}/")
                except Exception as e:
                    print(f"❌ Could not move {file}: {e}")
                moved = True
                break

        # if no matching extension found
        if not moved:
            other_folder = os.path.join(directory, "others")
            if not os.path.isdir(other_folder):
                try:
                    os.mkdir(other_folder)
                except Exception as e:
                    print(f"⚠️ Could not create 'others' folder: {e}")
                    continue

            try:
                shutil.move(filepath, os.path.join(other_folder, file))
                print(f"✅ Moved: {file} → others/")
            except Exception as e:
                print(f"❌ Could not move {file} to 'others': {e}")

    except Exception as e:
        print(f"⚠️ Unexpected error with {file}: {e}")
