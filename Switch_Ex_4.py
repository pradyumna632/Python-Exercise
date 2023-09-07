def match_guard(command,exits):

    # Match(Switch) statement started
    match command.split():
        case ["go", direction] if direction in exits:
            print(f"Going {direction}")
        case ["go", _]:     # _ is wildcard that mathes anything if no function matches
            print(f"Can't go that way!")

match_guard("go north", exits=["east", "south"])
match_guard("go north", exits=["north"])
