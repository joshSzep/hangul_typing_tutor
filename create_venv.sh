#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

# Step 1: Ensure that poetry is installed
python3 install_poetry.py

# Step 2: Run poetry install to create the virtual environment and install dependencies
poetry install

# Step 3: Install pre-commit hooks for git in this repository
poetry run pre-commit install

# Step 4: Determine the OS and print the correct virtual environment activation instructions
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    echo "Windows is not supported. Please use WSL, Docker, or another virtualization solution."
    exit 1
else
    # Unix-like systems (like OSX, Linux, Windows with WSL, etc)
    shell_name=$(basename "$SHELL")

    echo "To activate the virtual environment, use the following command for your shell ($shell_name):"
    echo ""

    case "$shell_name" in
        (bash|zsh)
            echo "  ${bold}source \".venv/bin/activate\"${normal}"
            ;;
        (fish)
            echo "  ${bold}source \".venv/bin/activate.fish\"${normal}"
            ;;
        (csh|tcsh)
            echo "  ${bold}source \".venv/bin/activate.csh\"${normal}"
            ;;
        (*)
            echo "Unsupported shell: $shell_name"
            echo "Please refer to the documentation for your shell on how to activate a virtual environment."
            ;;
    esac
    echo ""
fi
