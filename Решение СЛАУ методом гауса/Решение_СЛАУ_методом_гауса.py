def GausMethod(a):#приведение к ступенчатому виду

    n=len(a)
    m=len(a[0])
    for i in range(n):

        for j in range(i+1,n):
            
            if a[j][i]!=0:
                kf=float(a[i][i]/a[j][i])
                for c in range(m):
                    a[j][c]=a[j][c]*kf
                    a[j][c]=a[i][c]-a[j][c]
            print(a)
def BackwardPass(a,dictonary):#обратный проход
   
     for i in range(1,m):

         if i==1:
             dictonary[m-i]=round(a[m-1-i][m-i]/a[m-i-1][m-i-1])
         else:
            sum=0
            list_my=[k for k in range(1,m)]
            
           
            for j in reversed(list_my):
               

               if j+1 in dictonary:
                    sum=sum+a[m-i-1][j]*dictonary[j+1]

            dictonary[m-i]=round(((a[m-1-i][m-1]-sum))/(a[m-i-1][m-i-1]))



     


s=str(input())
s=s.split()
n=int(s[0])
m=int(s[1])
m=m+1
a=[[0 for j in range(m)] for i in range(n)]
dictonary={}

for i in range (n):#считываем данные
    inp=str(input())
    a[i]=inp.split()
    for j in range(m):
        a[i][j]=float(a[i][j])

GausMethod(a)
BackwardPass(a,dictonary)





