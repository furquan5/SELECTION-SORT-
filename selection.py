def selection(L):

    for i in range(len(L)):
        bigindex=0
        for j in range(len(L)-i):
            if L[bigindex]<L[j]:
                bigindex=j
        L[bigindex],L[j]=L[j],L[bigindex]

L=[24,16,14,11,6]
selection(L)

