#!/bin/bash

# Step 1: Run install_poetry.py with python3
python3 install_poetry.py

# Step 2: Run poetry install
poetry install

# Step 3: Install pre-commit hooks
poetry run pre-commit install

# Step 4: Determine the OS and print the correct virtual environment activation instructions
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    # Windows
    venv_path=$(poetry env info --path)

    # Check for PowerShell and cmd
    if [ -f "$venv_path/Scripts/Activate.ps1" ]; then
        # PowerShell
        echo "Please run the following command in PowerShell to activate the virtual environment:"
        echo "& \"$venv_path/Scripts/Activate.ps1\""
    else
        # cmd
        echo "Please run the following command in cmd to activate the virtual environment:"
        echo "\"$venv_path/Scripts/activate.bat\""
    fi
else
    # Unix-like systems (like OSX or Linux)
    shell_name=$(basename "$SHELL")

    echo "To activate the virtual environment, use the following command for your shell ($shell_name):"
    echo ""

    case "$shell_name" in
        (bash|zsh)
            echo "source \".venv/bin/activate\""
            ;;
        (fish)
            echo "source \".venv/bin/activate.fish\""
            ;;
        (csh|tcsh)
            echo "source \".venv/bin/activate.csh\""
            ;;
        (*)
            echo "Unsupported shell: $shell_name"
            echo "Please refer to the documentation for your shell on how to activate a virtual environment."
            ;;
    esac
fi
