from Terms_PART1 import *
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
