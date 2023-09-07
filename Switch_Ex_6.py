def Switch1(lst):
    match lst:
        case [_]:
            print("One Element")
        case[_,_]:
            print("Two Elemets") 
        case[x,y,z]:
            print(F"Three elements {x},{y},{z}")
        # case[x,y,z,*a]:
        #     print(F"Therr elements or more")
        #     print(*a)
        case[x,y,z,_,*a]:
            print(f"Four elements or more")
            print(*a)
        case _:
            print("None")                   


# Switch1([1])    #One Element
# Switch1([1,1])  #Two Elements
# Switch1([1,2,3])    #Three Elements 1,2,3
# Switch1([1,2,3,4,5,6])  # Three elements or more a = 4,5,6
Switch1([1,2,3,4,5,6,7,8,9,0])  # Four elements or more 5 6 7 8 9 0 if case is above three elements 
# Switch1(1)  #None


