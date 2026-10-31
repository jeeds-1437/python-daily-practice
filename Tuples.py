#Creating tuple
'''tup = (1,2,3,4)
print(tup)

num = [1,2,3,4]
print(tuple(num))#tuple constructor

mixed_data = (True, 7.5, ['Geeks','For','Geeks'], (10,20))
print(mixed_data)'''

#Accessing elements
'''tup = (1,2,3,4,5,6,7,8)
print(len(tup))
print(tup[0:])
print(tup[::-1])'''

#print elements of tuple
'''a = (10,20,30,40)
for i in a:
    print(i)'''

'''a = (10,20,30,40)
i = 0
while i < len(a):
    print(a[i])
    i += 1'''

#sum of elements
'''a = tuple(map(int, input().split()))
print(a)
sum = 0
i = 0
while i < len(a):
    sum += a[i]
    i += 1
print(sum)'''

#count even and odd in tuple
'''a = tuple(map(int,input().split()))
print(a)
even_count = 0
odd_count = 0
for i in a:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print('Even counts:',even_count)
print('Odd counts:',odd_count)'''

#checking even or odd in tuple
'''a = tuple(input().split())
print(a)
print(type(a[0]))
for i in a:
    if int(i) % 2 == 0:
        print('Even')
    else:
        print('Odd')'''

#largest and smallest elements
'''a = 10,78,19,67
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print('Max:',largest)

a = 10,78,19,67
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print('Min:',smallest)'''


'''a = 110,78,19,67
lar = a[0]
sma = a[len(a)-1]
for i in a:
    if i > lar:
        lar = i
    if i < sma:
        sma = i
print('Max:',lar)
print('Min:',sma)'''

#counting occurence of element
'''a = tuple(map(int, input().split()))
print(a)
count = 0
target = 19
i = 0
while i < len(a):
    if a[i] == target:
        count += 1
    i += 1
print('Count of 19:',count)'''
    
#index of element
'''a = tuple(map(int,input().split()))
target = 10
for i in range(len(a)):
    if a[i] == target:
        print('Element found at:',i)'''

#new tuple having only +ve no.
'''num = (10,20,-8,6,-1)
ans=()
for i in range(len(num)):
    if num[i] > 0:
        ans = ans + (num[i],)# 'single element of tuple'
print(ans)

num = [10,20,-8,6,-1]
ans = []
for i in range(len(num)):
    if num[i] > 0:
        ans = ans + [num[i]]
print(ans)'''

#reversing the tuple
'''num = (1,2,3,4)
rev = ()
i = 0
while i < len(num):
    rev = (num[i],) + rev
    i += 1
print(rev)'''

'''num = (1,2,3,4)
print(num[::-1])'''

#second largest distinct
'''num = (10,60,40,60,30)
largest = max(num)
second = num[0]
for i in num:
    if i != largest and i > second:
        second = i
print(second)'''

'''num=(60,60,40,30)
l=max(num)
s=num[-1]
for i in range(len(num)):
    if num[i]==l:
        continue
    else:
        if num[i]>s:
            s=num[i]
print(s)'''

#finding common elements in tuple
'''a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = ()
for i in a:
    for j in b:
        if int(i) == int(j) not in c:
            c += (int(i),)
print(c)'''

    





















