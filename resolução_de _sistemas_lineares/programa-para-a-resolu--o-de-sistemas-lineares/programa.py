import csv
n=0
s=[]
t=[]
t1=[]
t2=[]
r=[]
v=0
a=0
b=0
c=0
m=-2
largura=-1
altura=0
with open("resolução_de _sistemas_lineares\\dados.csv") as csv_file:
    csv_reader= csv.reader(csv_file,delimiter=',')
    csv_reader.__next__()
# onde eu  pego as fuções
    for row in csv_reader:
        largura=int(len(row))
        altura=altura+1
        for i in row:   
            t.append(int (i))
        s.append(list (t))
        t.clear()
#escalonamento com a primeira e segunda linha
for j in range (1,altura):
    for i in s[j]:
        n=(((s[0][0])*-1)*i)
        t.append(int(n))
        a=a+1
        if(a==largura):
            a=0
            del s[j]
            s.insert(j, list(t))  
            t.clear()
#comtas feitas
for i in range(1,altura): 
    for j in range(largura):
        n=s[0][j]+s[i][j]
        t.append(int(n))
        a=a+1
        if(a==largura):
            a=0
            del s[i]
            s.insert(i, list(t))  
            t.clear()
# comclusão
n=0
while a!=altura:
    a=a+1
    if (b!=altura):
        for j in s[-2]:
            t2.append(int(j))
    for i in s[-1]:
        t.append(int(i))
        n=n+i
    n=n-t[-1]
    n=t[-1]/n
    r.append(int(n))
    del s[-1]
    if b!=altura:
        b=a+1
        v=t2[m]*n
        t2.insert(m+1,v)
        del t2[m-1]
        m=m-1
        if b>2:
            for i in range(1,len(r)):
                v=t2[-i-1]*r[i-1]
                t2.insert(-i,v)
                del t2[i]
    
    if a<3:
        del s[-1]
        s.append(list(t2))        
    t.clear() 
    t2.clear()
    print(f'x{a}={n}')
    n=0
