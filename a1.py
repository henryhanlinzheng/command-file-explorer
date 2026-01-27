from pathlib import Path

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

def option_value(options, flag):
    if flag in options:
        idx = options.index(flag)
        if idx + 1 < len(options):
            return options[idx + 1]
    return None

def L_cmd(path_str, options):
    '''
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.
    '''
    my_path = Path(path_str)
    if not my_path.exists():
        print("The specified path does not exist or is not a directory.")
        return
    
    target_file = option_value(options, "-s")
    target_ext = option_value(options, "-e")

    if "-r" in options:
        items = my_path.rglob('*')
    else:
        items = my_path.iterdir()

    for item in items:
        if "-f" in options and not item.is_file():
            continue
        if target_file:
            if item.name != target_file:
                continue
        if target_ext:
            if item.suffix.lstrip('.') != target_ext.lstrip('.'):
                continue
        print(f"{item}")

def C_cmd(path_str, options):
    '''
    -n Specify the name of the file to be created.
    '''
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_dir():
        print("ERROR")
        return
    
    if "-n" in options:
        name = option_value(options, "-n")
        if name is None:
            print("ERROR")
            return
        name = Path(name).name
        if not name.lower().endswith('.dsu'):
            name += '.dsu'
        new_file_path = my_path / name
        try:
            new_file_path.touch(exist_ok=False)
            print(f"{new_file_path}")
        except FileExistsError:
            print(f"{new_file_path} already exists.")
    return        
    

def D_cmd(path_str):
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_file():
        print("ERROR")
        return
    if my_path.suffix.lower() != '.dsu':
        print("ERROR")
        return
    my_path.unlink()
    print(f"{my_path} DELETED")
    return

def R_cmd(path_str):
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_file():
        print("ERROR")
        return
    if my_path.suffix.lower() != '.dsu':
        print("ERROR")
        return
    with my_path.open('r') as file:
        contents = file.read()
        if contents == "":
            print("EMPTY")
        else:
            print(contents)
    return

def run():
    '''
    L - List the contents of the user specified directory.
    Q - Quit the program.
    C - Create a new file in the specified directory.
    D - Delete the file.
    R - Read the contents of a file.
    '''
    user_input = input("Enter user command: ")

    cmd, path_str, options = parse_input(user_input)

    if cmd == "L":
            L_cmd(path_str, options)
    elif cmd == "C":
        C_cmd(path_str, options)
    elif cmd == "D":
        D_cmd(path_str)
    elif cmd == "R":
        R_cmd(path_str)
    elif cmd == "Q":
        return
    # print(command, path_str, options)

if __name__ == "__main__":
    run()

    # L /Users/henryzheng/Documents/ucirvine/2025-26/winter26/ics32
    