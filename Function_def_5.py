def foo():
    global s  # With Global Keyword
    s+='i Won'
    print(s)

s='i lost'
foo()