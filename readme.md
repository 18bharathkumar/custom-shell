# Moti Patli Shell

## Description

Moti Patli Shell is a custom terminal shell designed to provide basic file and system operations in a user-friendly manner. It includes commands for creating, deleting, and managing files, as well as utilities for directory and system interactions. This shell is built using Bash and Python, with additional functionalities powered by a shared library (`code.so`).

## Features

- **File Operations**: Create, delete, rename, list, and view files.
- **System Commands**: Get the current directory, display user info, and clear the terminal.
- **Customizations**: Change terminal background, foreground colors, and font styles.
- **Third-Party Integrations**: Open files in Visual Studio Code or Nano editor.
- **Advanced Utilities**: Use commands like `grep` to search within files or `ping` to test network connectivity.

## How to Run the Project

1. **Prerequisites**:

   - Ensure Python 3 is installed.
   - Compile the `code.so` shared library using `gcc` if not already compiled:
     ```bash
     gcc -shared -o code.so -fPIC code.c
     ```
   - Install necessary tools like `xterm`, `nano`, and `Visual Studio Code` (optional).

2. **Start the Shell**:
   Run the following command to start the Moti Patli Shell:

   ```bash
   python3 run_shell.py


# File Operations
create <filename>       # Create a new file
delete <filename>       # Delete a file
rename <old_filename> <new_filename>  # Rename a file
ls                      # List all files in the current directory

# Directory & System Info
pwd                     # Display the current directory path
whoami                  # Show the current logged-in user

# Editing and Searching
nano <filename>         # Open a file in Nano editor
grep <text> <filename>  # Search for specific text in a file
cat <filename>          # Display the content of a file

# Network & Utilities
ping <website>          # Test the connectivity to a website
clear                   # Clear the terminal screen

# Customization
vs <filename>           # Open a file in Visual Studio Code
color <bg> <fg>         # Change terminal background and foreground colors
font <font> <size>      # Change terminal font and size

# Root Access
sudo login              # Log in as root (password: 'admin')

# Help
help                    # Show a list of all available commands
