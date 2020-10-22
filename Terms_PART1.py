def term(t,n):
    L=[1]
    c=L[0]
    p=1
    q=1
    def y(x):
        return 2*x+1
    for i in range(1,n):
        if (i%2==0):
            c=c+y(p)
            L=L+[c]
            p=p+1
        else:
            c=c+q
            L=L+[c]
            q=q+1
    return L[t]
