x=int(input())
sum=0
if x<0:
    print('Введите другое число')
else:
    for i in range(1,x+1):
        sum+=i
print(sum)