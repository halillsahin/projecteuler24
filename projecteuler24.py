import itertools
liste="0123456789"
x=list(liste)
a=[i for i in itertools.permutations(x,10)]
a.sort()
print(a[999999])