def command_split(command):
    match command.split():
        case ["make"]:
            print("Default Make")
        case ["make", cmd]:
            print(f"Make command found: {cmd}")
        case ["Restart"]:
            print("Restarting")
        case ["re", *files]:
            print(f"Deleting files: {files}")
        case _:
            print("didn't match")
            
command_split("make")
command_split("make clean")
command_split("Restart")
command_split("re a b c")
command_split("doesnt match")