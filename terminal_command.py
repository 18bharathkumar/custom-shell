terminal_command = [
    'xterm',
    '-fa', 'Monospace',
    '-fs', '16',
    '-bg', 'black',
    '-fg', 'green',
    '-xrm', 'XTerm*selectToClipboard: true',  # Enables clipboard access
    '-e', 'bash', '-c', '''
        echo "Welcome to Moti Patli Shell";
        echo " ";
        echo "The Shell Created By Bharath Kumar From RVCE";
        echo " ";

        while true; do
            echo "My Shell: $HOME/";
            echo " ";
            read -p "Enter command: " command;
            case $command in
                create*)
                    filename=$(echo $command | cut -d " " -f 2-)
                    python3 -c "
import ctypes  # Import ctypes here
lib = ctypes.CDLL('./code.so')
lib.createFile.argtypes = [ctypes.c_char_p]
lib.createFile.restype = ctypes.c_int
filename = '$filename'
result = lib.createFile(filename.encode('utf-8'))
if result == 0:
    print(f'File \\"{filename}\\" created successfully.')
elif result == 1:
    print(f'File \\"{filename}\\" already exists.')
else:
    print('Error creating the file.')
                    "
                    ;;

                delete*)
                    filename=$(echo $command | cut -d " " -f 2-)
                    python3 -c "
import ctypes  # Import ctypes here
lib = ctypes.CDLL('./code.so')
lib.deleteFile.argtypes = [ctypes.c_char_p]
lib.deleteFile.restype = ctypes.c_int
filename = '$filename'
result = lib.deleteFile(filename.encode('utf-8'))
if result == 0:
    print(f'File \\"{filename}\\" deleted successfully.')
elif result == 1:
    print(f'File \\"{filename}\\" does not exist.')
else:
    print('Error deleting the file.')
                    "
                    ;;

                rename*)
                    old_filename=$(echo $command | cut -d " " -f 2)
                    new_filename=$(echo $command | cut -d " " -f 3)
                    if [ -f "$old_filename" ]; then
                        mv "$old_filename" "$new_filename"
                        echo "File renamed from $old_filename to $new_filename"
                    else
                        echo "File $old_filename does not exist."
                    fi
                    ;;

                ls)
                    python3 -c "
import ctypes  # Import ctypes here
lib = ctypes.CDLL('./code.so')
lib.listFiles.argtypes = []
lib.listFiles.restype = ctypes.c_int
result = lib.listFiles()
if result == 0:
    print('Files listed successfully.')
else:
    print('Error listing files.')
                    "
                    ;;

                pwd)
                    python3 -c "
import ctypes  # Import ctypes here
import os  # Import os to get the current working directory
print(f'Current directory: {os.getcwd()}')
                    "
                    ;;

                help)
                    python3 -c "
print('Available commands:')
print('1. create <filename> - Create a new file')
print('2. delete <filename> - Delete a file')
print('3. rename <old_filename> <new_filename> - Rename a file')
print('4. ls - List files in the current directory')
print('5. pwd - Print the current directory path')
print('6. help - Display this help message')
print('7. ping <website> - Ping a website')
print('8. vs <filename> - Open a file in Visual Studio Code')
print('9. color <bg> <fg> - Change terminal background and foreground color')
print('10. font <font> <size> - Change terminal font and size')
print('11. nano <filename> - Open file in Nano editor')
print('12. grep <text> <filename> - Search for text in a file')
print('13. cat <filename> - Display file content')
print('14. whoami - Display the current user')
print('15. sudo login - Log in as root (password required)')
print('16. clear - Clear the terminal screen')
                    "
                    ;;

                ping*)
                    website=$(echo $command | cut -d " " -f 2-)
                    ping -c 4 $website
                    ;;

                vs*)
                    filename=$(echo $command | cut -d " " -f 2-)
                    code $filename
                    ;;

                color*)
                    bg=$(echo $command | cut -d " " -f 2)
                    fg=$(echo $command | cut -d " " -f 3)
                    echo -e "\\e]11;#$bg\\a"
                    echo -e "\\e]10;#$fg\\a"
                    ;;

                font*)
                    font=$(echo $command | cut -d " " -f 2)
                    size=$(echo $command | cut -d " " -f 3)
                    echo -e "\\e]710;$font-$size\\a"
                    ;;

                nano*)
                    filename=$(echo $command | cut -d " " -f 2-)
                    if [ ! -f $filename ]; then
                        touch $filename
                    fi
                    nano $filename
                    ;;

                grep*)
                    text=$(echo $command | cut -d " " -f 2)
                    filename=$(echo $command | cut -d " " -f 3)
                    grep "$text" "$filename"
                    ;;

                cat*)
                    filename=$(echo $command | cut -d " " -f 2-)
                    cat $filename
                    ;;

                whoami)
                    whoami
                    ;;

                "sudo login")
                    echo "Enter your password: "
                    read -s password
                    if [ "$password" == "admin" ]; then
                        echo "You are now logged in as root."
                    else
                        echo "Incorrect password."
                    fi
                    ;;

                clear)
                    clear
                    ;;

                *)
                    echo "Invalid command. Try again.";
                    ;;

            esac;
        done
    '''
]
