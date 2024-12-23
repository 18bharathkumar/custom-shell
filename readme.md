
# Moti Patli Shell

## Description

Moti Patli Shell is a custom terminal shell designed to provide basic file and system operations in a user-friendly manner. It includes commands for creating, deleting, and managing files, as well as utilities for directory and system interactions. This shell is built using Bash and Python, with additional functionalities powered by a shared library (`code.so`).

## Features

- **File Operations**: Create, delete, list, and view files.
- **System Commands**: Get the current directory, display user info, and clear the terminal.
- **Customizations**: Change terminal background, foreground colors, and font styles.
- **Third-Party Integrations**: Open files in Visual Studio Code or Nano editor.
- **Advanced Utilities**: Use commands like `grep` to search within files or `ping` to test network connectivity.

## How to Run the Project

1. **Prerequisites**:

   - Ensure Python 3 is installed.
   - Compile the `code.so` shared library using `gcc` if not already compiled.
     ```bash
     gcc -shared -o code.so -fPIC code.c
     ```
   - Install necessary tools like `xterm`, `nano`, and `Visual Studio Code` (optional).

2. **Start the Shell**:
   Run the following command to start the Moti Patli Shell:

   ```bash
   python3 run_shell.py
   ```

3. **Available Commands**:

   - `create <filename>`: Create a new file.
   - `delete <filename>`: Delete a file.
   - `ls`: List all files in the current directory.
   - `pwd`: Display the current directory path.
   - `help`: Show a list of all available commands.
   - `ping <website>`: Test the connectivity to a website.
   - `vs <filename>`: Open a file in Visual Studio Code.
   - `color <bg> <fg>`: Change the terminal background and foreground colors (e.g., `color black green`).
   - `font <font> <size>`: Change the terminal font and size.
   - `nano <filename>`: Open a file in Nano editor.
   - `grep <text> <filename>`: Search for specific text in a file.
   - `cat <filename>`: Display the content of a file.
   - `whoami`: Show the current logged-in user.
   - `sudo login`: Log in as root (password: `admin`).
   - `clear`: Clear the terminal screen.
   - `rename <old_filename> <new_filename>`: Rename a file.

## Notes

- Ensure the `code.so` shared library is present in the same directory as the shell script.
- Custom commands rely on the shared library and Bash utilities, so proper permissions are required.

Enjoy using the Moti Patli Shell!
