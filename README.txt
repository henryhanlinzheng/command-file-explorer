This project is a command-based file explorer tool based in Python using pathlib that allows the user to find and filter files/directories. It parses custom commands (ie. L to list contents in a specific directory), and is supported with options such as recursive search (-r), file-only filtering (-f), search by filename (-s) and extension (-e). 

COMMAND FORMAT: [COMMAND] [INPUT] [[-]OPTION] [INPUT]

L - Lists files and directories in a specified path.
    Options:
    -r : List contents recursively through all subdirectories
    -f : Show only files (exclude directories)
    -s <filename> : Filter by specific file name
    -e <extension> : Filter by file extension
C - Creates a new .dsu file in the specified directory.
    Required option:
    -n : Specify name of file to create
R - Reads and displays the contents of a .dsu file.
D - Deletes a .dsu file.
Q - Exits the program.

The program will display ERROR if:
    1. An invalid command is entered
    2. Invalid options are provided for a command
    3. A specified path does not exist
    4. Attempting to read/delete a non-.dsu file
    5. Attempting to create a file that already exists
    6. Required options are missing