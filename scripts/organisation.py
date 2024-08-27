#!/usr/bin/python3

import shutil
from pathlib import Path

FILE_TYPES = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".odt",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
    ],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".sh", ".py", ".js", ".bat", ".pl"],
    "Others": [],  # Files that don't match any category
}


def organize_files(target_dir):
    target_dir = Path(target_dir)

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory {
              target_dir} does not exist or is not a directory.")
        return

    # Create folders if they don't exist
    for category in FILE_TYPES.keys():
        category_dir = target_dir / category
        if not category_dir.exists():
            category_dir.mkdir()

    # Move files to their corresponding folders
    for file in target_dir.iterdir():
        if file.is_file():
            # Skip hidden files (those that start with a dot)
            if file.name.startswith("."):
                print(f"Skipping hidden file: {file.name}")
                continue

            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    shutil.move(str(file), str(target_dir / category / file.name))
                    print(f"Moved: {file.name} -> {category}")
                    moved = True
                    break
            if not moved:  # Move to "Others" if no match found
                shutil.move(str(file), str(target_dir / "Others" / file.name))
                print(f"Moved: {file.name} -> Others")


def main(target_dir=str(Path.home() / "Downloads")):
    print("Organizing files in:", target_dir)
    organize_files(target_dir)
    print("File organization complete.")


if __name__ == "__main__":
    import sys

    main(*sys.argv[1:])
