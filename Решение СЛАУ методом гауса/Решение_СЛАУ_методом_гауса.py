#GausMethod
""""
Напишите программу, которая решает систему линейных алгебраических уравнений методом Гаусса.

Формат входных данных: 

В первой строке задаются два числа: количество уравнений n (n≥1) и количество неизвестных m (m≥1). Далее идут n строк, каждая из которых содержит m+1 число. Первые m чисел — это коэффициенты i-го уравнения системы, а последнее, (m+1)-е число — коэффициент bi, стоящий в правой части i-го уравнения.
Формат выходных данных:
В первой строке следует вывести слово YES, если решение существует и единственно, слово NO в случае, если решение не существует, и слово INF в случае, когда решений существует бесконечно много. Если решение существует и единственно, то во второй строке следует вывести решение системы в виде m чисел, разделенных пробелом.
"""

def GausMethod(a):                                  #приведение к ступенчатому виду

    n=len(a)
    m=len(a[0])

    for i in range(n):

        for j in range(i+1,n):
            
            if i<m:

               if a[j][i]!=0 :
                    if a[i][i]!=0:

                        kf=float(a[i][i]/a[j][i])
                        for c in range(m):
                            a[j][c]=a[j][c]*kf
                            a[j][c]=a[i][c]-a[j][c]
                    else:                               #если в строке нунужный 0
                        other=0
                        stop=0
                        b1=[0 for j in range(m)]        #строка которую меняем
                        for z in range(m):
                            b1[z]=a[i][z]

                        a1=[0 for j in range(m)]        #строка на которю меняем
                        for k in range(i,n):
                            if a[k][i]!=0 and stop==0:              #Нашли эту строку
                               stop=1
                               other=k
                               for c in range(m):
                                    a1[c]=a[k][c]
                    
                        for d in range(m):              #меняем строки
                            a[i][d]=a1[d]
                        for z in range(m):
                            a[other][z]=b1[z]


def BackwardPass(a,dictonary):#обратный проход
   
     for i in range(1,m):

         if i==1:
             if abs(a[m-i-1][m-i-1])< 0.0000001:
                 return 0
             dictonary[m-i]=round(a[m-1-i][m-i]/a[m-i-1][m-i-1],13)
         else:
            sum=0
            list_my=[k for k in range(1,m)]
            
           
            for j in reversed(list_my):
               

               if j+1 in dictonary:
                    sum=sum+a[m-i-1][j]*dictonary[j+1]

            dictonary[m-i]=round(((a[m-1-i][m-1]-sum))/(a[m-i-1][m-i-1]),13)


def CheckZeroStrok(a,Libary):#проверка на нулевую строку

    for i in range(n-1,1,-1):
        zero=1
        for j in range(m):
            if abs(a[i][j])>1e-10:
                zero=0
        if zero==1:
            Libary[3]=Libary[3]+1




def CheckINF(a,Libary): #проверка на бесконечное кол во решений
    for i in range(n):
        if abs(a[i][m-1])<0.0000001 and abs(a[i][m-2])<0.0000001:
            Libary[0]=1


def CheckNo(a,Libarry):# проверка на "Нет решений"
    if abs(a[n-1][m-2])<1e-10 and  abs(a[n-1][m-1])>1e-10:
            Libary[1]=1


     


s=str(input())
s=s.split()
n=int(s[0])
m=int(s[1])
m1=m
m=m+1
a=[[0 for j in range(m)] for i in range(n)]
dictonary={}
Libary=[0 for j in range(4)] # здесь храним значения ["INF","NO","YES,"кол во нулевых строк"] 1 - значит условие верно
k=1


for i in range (n):#считываем данные
    inp=str(input())
    a[i]=inp.split()
    for j in range(m):
        a[i][j]=float(a[i][j])


GausMethod(a)
CheckZeroStrok(a,Libary)
n=n-Libary[3]
CheckINF(a,Libary)
CheckNo(a,Libary)

if (n<m1 or Libary[0]==1) and Libary[1]==0:
    inf=1
    print("INF")  
else :
    if Libary[1]!=1:

        k=BackwardPass(a,dictonary)
        if k==0:
             print("NO")

        
    if Libary[1]==1:
        print("NO")
    else :
        print("YES")
        k=1
        for i in range(len(dictonary)):
            print((dictonary[k]),end=" ")
            k=k+1




