n=int(input())
l=[]
for i in range(1,n+1):
    if int(i**3)<n+1:
        l.append(int(i**3))
print(l)