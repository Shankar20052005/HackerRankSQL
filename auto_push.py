import os
import time
import subprocess

FOLDER_TO_WATCH = "."
ALLOWED_EXTENSIONS = [".sql", ".py"]

def push_file_to_github(filename):
    print(f"📤 Uploading {filename} to GitHub...")
    try:
        subprocess.run(["git", "add", filename], check=True)
        subprocess.run(["git", "commit", "-m", f"Add: {filename}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"✅ {filename} pushed successfully!\n")
    except subprocess.CalledProcessError as e:
        print("❌ Git error:", e)

def main():
    seen = set(os.listdir(FOLDER_TO_WATCH))

    print("🚀 Watching folder for new files...")
    while True:
        time.sleep(3)
        current = set(os.listdir(FOLDER_TO_WATCH))
        new_files = current - seen
        for file in new_files:
            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                push_file_to_github(file)
        seen = current

if __name__ == "__main__":
    main()
