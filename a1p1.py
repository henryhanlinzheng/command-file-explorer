from pathlib import Path

def cmd_portal(cmds):
    '''
    L - List the contents of the user specified directory.
    Q - Quit the program.
    '''
    if cmds[0] == "L":
        L_cmd(cmds)
    elif cmds[0] == "Q":
        exit()

def L_cmd(cmds):
    my_path = Path(cmds[1])
    if my_path.exists() and my_path.is_dir():
        for item in my_path.iterdir():
            print(f"{item}")
    else:
        print("The specified path does not exist or is not a directory.")

def run():
    user_input = input("Enter user command: ")
    cmds = user_input.split(" ")
    cmd_portal(cmds)
    # print(cmds)

if __name__ == "__main__":
    run()

    # /Users/henryzheng/Documents/UC Irvine/2025-26/WINTER 2026/ICS 32