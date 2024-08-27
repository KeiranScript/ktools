from pathlib import Path
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    DIR = input("Enter directory path (or leave blank for default): ")
    FALLBACK_DIR = os.path.expanduser("~/Pictures/Screenshots")

    if DIR:
        DIR = Path(DIR)
        if not DIR.is_dir():
            print(bcolors.FAIL + "The provided directory does not exist or the program has insufficient permissions." + bcolors.ENDC)
            DIR = FALLBACK_DIR
    else:
        DIR = Path(FALLBACK_DIR)

    try:
        _, _, files = next(os.walk(DIR))
        file_count = len(files)
    except Exception as e:
        print(bcolors.FAIL + str(e) + bcolors.ENDC)
        return
    
    if file_count <= 0:
        print("There aren't any files here!")
        return

    count = 0
    print("Are you sure you wish to continue?")
    print("This action will " + bcolors.FAIL + "DELETE ALL FILES " + bcolors.ENDC + "in directory " + bcolors.OKBLUE + str(DIR) + ".")
    confirmation = input("Y/N >> ")

    if "y" in confirmation.lower():
        print(bcolors.HEADER + "Beginning execution." + bcolors.ENDC)
    else:
        return

    for file in DIR.iterdir():
        if file.suffix in {'.png', '.jpg'}:
            file.unlink()
            count += 1
            print(f"{bcolors.OKGREEN + file.name + bcolors.FAIL} deleted. {bcolors.ENDC}{count}/{file_count}")

if __name__ == "__main__":
    main()

