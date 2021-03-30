
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
    
    
    
def Formain(X):
    
    I=[1,1,2]

    def y(x):
        for i in range(x):
            if (term(i,i+1)>x):
                N=i
                break
        t=0
        a=0
        for i in range(N):
            if (a==0):
                t=t+I[-term(i,N+1)]
                a=a+1
            elif (a==1):
                t=t+I[-term(i,N+1)]
                a=a+1
            elif (a==2):
                t=t-I[-term(i,N+1)]
                a=a+1
            else:
                t=t-I[-term(i,N+1)]
                a=0
        return t



    for i in range(3,X+1):
        I=I+[y(i)]
    print(I[X])
    
    
    
    
    
print("This program is made by Ajay Mehra, and I want to say that it took me 2 days for writing this code and it was fun writing this, This program is designed for finding number of partitions (search partitions Number Theory (Wikipedia)) for any numbers ")
a=int(input("Type any number I will find answer for you"))
Formain(a)
