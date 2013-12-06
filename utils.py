def FromString(str):
    k = []
    v = []
    for line in str.split("\n"):
        if line.find(';') == 0: #comment line
            continue
        ls = line.split('=')
        if len(ls) < 2: #undefined or empty line
            continue
        k.append(ls[0].strip().lower() )
        v.append(ls[1].strip().lower() )
    return (k,v)

def Indeces(l, elm):
    ind = []
    for i in range(len(l)):
        if l[i]==elm:
            ind.append(i)
    return ind
        




