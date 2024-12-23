import subprocess
import ctypes
from tkinter import *
from terminal_command import terminal_command  # Import the terminal_command array

# Load the shared object file (make sure 'code.so' is in the same directory as this Python file)
lib = ctypes.CDLL('./code.so')

# Set argument and return types for the C functions
lib.listFiles.argtypes = []
lib.listFiles.restype = ctypes.c_int

# Function to call the C 'ls' command and return output
def list_files():
    result = lib.listFiles()
    if result == 0:
        return "Files listed successfully."
    else:
        return "Error listing files."

# Function to handle commands entered in the shell
def handle_command(command):
    if command.strip() == 'ls':  # When 'ls' is typed
        output = list_files()  # Call the C function to list files
        return output  # Return the output of the 'ls' command
    else:
        return f"Unknown command: {command}"  # Handle unknown commands

# Function to launch the shell with the custom interface in xterm
def open_shell():
    try:
        # Run the xterm shell with the custom command list
        subprocess.Popen(terminal_command)  # Using Popen to launch xterm and keep it open
    except Exception as e:
        print(f"Error occurred: {e}")

# GUI Setup
root = Tk()
root.title("File Operations")

# Instructions
Label(root, text="My Shell has been opened automatically.").pack(pady=10)

# Automatically open the shell without waiting for button click
open_shell()

root.mainloop()
