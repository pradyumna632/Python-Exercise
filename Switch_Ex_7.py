class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case point(x=0,y=0):
            print("Origin")
        case point(x=0,y=y):
            print(f"y={y}")
        case point(x=x,y=0):
            print(f"x={x}")
        case point():
            print("Somewhere Else")
        case _:
            print("Not a point") 


Point(1,var)
Point(1,y=var)
Point(x=1,y=var)
Point(y=var,x=1)