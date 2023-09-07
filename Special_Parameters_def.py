#  Posiional only and keyword only arguments
# 

def f(a,b,c):
    # Normal function with three arguments 
    print(f" {a=}, {b=}, {c=} ")

def calling_normal_args():
    f(1,2,3) #Positional arguments
    f(a=1,b=2,c=3)  #Keyword Argumnets. The order of argumnets doesn't matter in keyword argumnts.

calling_normal_args()    








