#!/usr/bin/python3

import os
import importlib
import sys
from pathlib import Path

SCRIPT_DIR = Path("./scripts")  # Directory where individual scripts are stored
SCRIPT_EXT = ".py"  # Extension for script files


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def list_scripts():
    """List all available scripts in the scripts directory."""
    scripts = [f.stem for f in SCRIPT_DIR.glob(f"*{SCRIPT_EXT}")]
    return scripts


def load_and_run_script(script_name, *args):
    """Dynamically load and execute a script by name with additional arguments."""
    script_path = SCRIPT_DIR / f"{script_name}{SCRIPT_EXT}"
    if script_path.exists():
        module_name = f"scripts.{script_name}"
        try:
            module = importlib.import_module(module_name)
            print(bcolors.OKCYAN +
                  f"\nRunning script: {script_name}" + bcolors.ENDC)
            module.main(*args)  # Pass arguments to the script's main function
        except Exception as e:
            print(bcolors.FAIL +
                  f"Failed to run {script_name}: {e}" + bcolors.ENDC)
    else:
        print(bcolors.FAIL +
              f"Script {script_name} does not exist." + bcolors.ENDC)


def main():
    """Main hub interface."""
    while True:
        print(bcolors.HEADER + "\nAvailable Scripts:" + bcolors.ENDC)
        scripts = list_scripts()
        for idx, script in enumerate(scripts, 1):
            print(bcolors.OKBLUE + f"{idx}. {script}" + bcolors.ENDC)

        print(bcolors.WARNING + "0. Exit" + bcolors.ENDC)
        choice = input(bcolors.OKCYAN +
                       "Select a script to run: " + bcolors.ENDC)

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print(bcolors.OKGREEN + "Exiting ktools. Goodbye!" + bcolors.ENDC)
                sys.exit()
            elif 1 <= choice <= len(scripts):
                script_name = scripts[choice - 1]
                args = input(
                    bcolors.OKCYAN
                    + "Enter any arguments (space-separated): "
                    + bcolors.ENDC
                ).split()
                load_and_run_script(script_name, *args)
            else:
                print(
                    bcolors.FAIL + "Invalid selection. Please try again." + bcolors.ENDC
                )
        else:
            print(bcolors.FAIL + "Please enter a number." + bcolors.ENDC)


if __name__ == "__main__":
    main()
