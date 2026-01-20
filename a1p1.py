from pathlib import Path

def L_options(cmds):
    '''
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.
    '''
    pass

def L_cmd(path_str, options):
    '''
    my_path = Path(path_str)
    if my_path.exists() and my_path.is_dir():
        for item in my_path.iterdir():
            print(f"{item}")
    else:
        print("The specified path does not exist or is not a directory.")
    '''
    # L_options(cmds)
    print(path_str, options)

def parse_input(cmds):
    parts = cmds.split()
    
    if not parts:
        return
    
    command = parts[0]
    split_index = len(parts)
    
    for i in range(1, len(parts)):
        if parts[i].startswith('-'):
            split_index = i
            break

    path_str = ' '.join(parts[1:split_index])
    options = parts[split_index:]

    return command, path_str, options

def run():
    '''
    L - List the contents of the user specified directory.
    Q - Quit the program.
    '''
    user_input = input("Enter user command: ")

    cmd, path_str, options = parse_input(user_input)

    if cmd == "L":
        L_cmd(path_str, options)
    elif cmd == "Q":
        exit()
    # print(command, path_str, options)

if __name__ == "__main__":
    run()

    # /Users/henryzheng/Documents/ucirvine/2025-26/winter26/ics32
    