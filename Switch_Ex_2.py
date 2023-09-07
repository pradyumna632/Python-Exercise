def match_alt(command):
    match command.split():
        case["north"] | ["go","north"]:
            print("going north")
        case["get", obj] | ["pick","up",obj] | ["pick",obj,"up"]:
            print(f"Picking up: {obj}")    

# match_alt("north")  
# match_alt("go north")
# match_alt("get GIRLFRIEND")    
# match_alt("pick up GIRLFRIEND")  
# match_alt("pick GIRLFRIEND up")  



