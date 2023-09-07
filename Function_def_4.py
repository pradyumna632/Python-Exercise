def Studeent_info(*args, **kwargs):
    print(args)
    print(kwargs)

animals = ['cat','dog','chicken']   
info = {'name':'john', 'age':20}

Studeent_info(*animals,**info)    