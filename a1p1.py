from pathlib import Path

def cmd_portal(cmds):
    if cmds[0] == "L":
        L_cmd(cmds)
    elif cmds[0] == "Q":
        exit()

def L_cmd(cmds):
    my_path = Path(cmds[1])
    if my_path.exists() and my_path.is_dir():
        for item in my_path.iterdir():
            if item.is_file():
                print(f"File: {item.name}")
            elif item.is_dir():
                print(f"Directory: {item.name}")
    else:
        print("The specified path does not exist or is not a directory.")

def run():
    user_input = input("Enter user command: ")
    cmds = user_input.split(" ")
    cmd_portal(cmds)

if __name__ == "__main__":
    run()