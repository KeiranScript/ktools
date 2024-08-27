import subprocess

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

def run_paru_update(automate=False):
    """Run paru -Syyu command with optional automation of prompts."""
    command = "paru -Syyu --noconfirm" if automate else "paru -Syyu"
    try:
        result = subprocess.run(command, shell=True, text=True)
        if result.returncode == 0:
            print(bcolors.OKGREEN + "\nSystem update completed successfully!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "\nSystem update encountered errors." + bcolors.ENDC)
    except subprocess.CalledProcessError as e:
        print(bcolors.FAIL + f"Error: {str(e)}" + bcolors.ENDC)

def main():
    """Main function to handle system update."""
    print(bcolors.HEADER + "\nParu System Update" + bcolors.ENDC)
    print(bcolors.OKCYAN + "This will refresh all package databases and update all installed packages." + bcolors.ENDC)

    choice = input(bcolors.WARNING + "\nWould you like to automate this process? (Y/N): " + bcolors.ENDC)

    if choice.lower() == 'y':
        print(bcolors.OKBLUE + "\nStarting automated system update..." + bcolors.ENDC)
        run_paru_update(automate=True)
    else:
        print(bcolors.OKBLUE + "\nStarting interactive system update..." + bcolors.ENDC)
        run_paru_update()

if __name__ == "__main__":
    main()

