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

def validate_options(command, options):
    """Return True if all options are valid for command, else False."""
    allowed = {
        'L': ['-r', '-f', '-s', '-e'],
        'C': ['-n'],
        'D': [],
        'R': [],
        'Q': []
    }
    cmd = command.upper()
    if cmd not in allowed:
        return False

    i = 0
    while i < len(options):
        opt = options[i]
        if not opt.startswith('-'):
            return False
        if opt not in allowed[cmd]:
            return False
        # flags that require a value
        if opt in ('-s', '-e', '-n'):
            if i + 1 >= len(options):
                return False
            if options[i + 1].startswith('-'):
                return False
            i += 2
        else:
            i += 1
    return True

def L_cmd(path_str, options):
    '''
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.
    '''
    my_path = Path(path_str)
    if not my_path.exists():
        print("ERROR")
        return
    
    target_file = option_value(options, "-s")
    target_ext = option_value(options, "-e")
    recursive = "-r" in options
    files_only = "-f" in options

    # Helper to check if a file matches filter criteria
    def should_print_file(item):
        if files_only and not item.is_file():
            return False
        if target_file and item.name != target_file:
            return False
        if target_ext and item.suffix.lstrip('.') != target_ext.lstrip('.'):
            return False
        return True

    def recursive_list(directory):
        try:
            # Sort items to ensure deterministic output
            items = sorted(directory.iterdir())
        except OSError:
            # Handle permission errors or missing paths gracefully
            return

        files = [i for i in items if i.is_file()]
        dirs = [i for i in items if i.is_dir()]

        # 1. Print Files First
        for f in files:
            if should_print_file(f):
                print(f)

        # 2. Process Directories
        for d in dirs:
            # Determine if we should print the directory name itself
            # We skip printing the directory if:
            # -f is on (files only)
            # OR we are searching for specific names/extensions (-s / -e)
            should_show_dir = not files_only and not target_file and not target_ext
            
            if recursive:
                if should_show_dir:
                    print(d)
                recursive_list(d)
            else:
                # Non-recursive listing of the directory
                if should_show_dir:
                    print(d)

    # Start the listing
    if recursive:
        recursive_list(my_path)
    else:
        # Non-recursive logic (just list current dir contents)
        # We reuse the same logic: Files first, then dirs
        try:
            items = sorted(my_path.iterdir())
        except OSError:
            print("ERROR")
            return
        files = [i for i in items if i.is_file()]
        dirs = [i for i in items if i.is_dir()]
        
        for f in files:
            if should_print_file(f):
                print(f)
        for d in dirs:
            if not files_only and not target_file and not target_ext:
                print(d)

def C_cmd(path_str, options):
    '''
    -n Specify the name of the file to be created.
    '''
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_dir():
        print("ERROR")
        return
    
    if "-n" not in options:
        print("ERROR")
        return
    
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
        print(f"ERROR")
    return        
    

def D_cmd(path_str):
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_file():
        print("ERROR")
        return
    if my_path.suffix.lower() != '.dsu':
        print("ERROR")
        return
    try:    
        my_path.unlink()
        print(f"{my_path} DELETED")
    except OSError:
        print("ERROR")
    return

def R_cmd(path_str):
    my_path = Path(path_str)
    if not my_path.exists() or not my_path.is_file():
        print("ERROR")
        return
    if my_path.suffix.lower() != '.dsu':
        print("ERROR")
        return
    try:    
        with my_path.open('r') as file:
            contents = file.read()
            if contents == "":
                print("EMPTY")
            else:
                print(contents, end='')
    except OSError:
        print("ERROR")
    return

def run():
    '''
    L - List the contents of the user specified directory.
    Q - Quit the program.
    C - Create a new file in the specified directory.
    D - Delete the file.
    R - Read the contents of a file.
    '''
    while True:
        user_input = input()
        parsed = parse_input(user_input)
        if not parsed:
            print("ERROR")
            continue
        cmd, path_str, options = parsed
        
        cmd = cmd.upper()
        if cmd not in ("L", "Q", "C", "D", "R"):
            print("ERROR")
            continue

        if not validate_options(cmd, options):
            print("ERROR")
            continue

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
    # C /Users/henryzheng/Documents/ucirvine/2025-26/winter26/ics32
    # D /Users/henryzheng/Documents/ucirvine/2025-26/winter26/ics32/test.dsu
    # R /Users/henryzheng/Documents/ucirvine/2025-26/winter26/ics32/test.dsu