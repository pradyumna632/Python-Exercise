#  Structural Pattern Matching
# We can put pattern inside another pattern 

def match_capture_subpattern(command):
    match command.split():
        case["go", ("north" | "south" | "east" | "west") as direction]:
            print(f"going {direction}")

match_capture_subpattern("go north")
match_capture_subpattern("go east")

