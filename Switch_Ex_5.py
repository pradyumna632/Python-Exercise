def Switch(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


# Switch((0,0))   # Output: origin
# Switch((0,1))   # Output: Y=1
# Switch((1,0))     # Output: X=1
# Switch((2,2))      # Output: X=2,Y=2
# Switch(())          # Output: raise Value Error




