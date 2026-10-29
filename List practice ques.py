#Find sum of elements in list
'''a=[]
for i in range(5):
    num = int(input('Enter num'+str(i + 1)+':'))
    a.append(num)
print('List elements are:',a)
sum = 0
for j in a:
    sum += j
print('The sum of the elements are',sum)'''

#Max & Min elements in list
'''a = []
for i in range(4):
    num = int(input('Enter num'+str(i + 1)+':'))
    a.append(num)
print('List:',a)
a.sort()
print(a)
print('The minimum element in list is ',a[0])
print('The maximum element in list is ',a[len(a)-1])'''

#Largest and smallest element in list
'''a =[] #[43,78,23,80]
for i in range(4):
    num = int(input('Enter number'+str(i + 1)+':'))
    a.append(num)
print('List:',a)
max_ele = a[0]
for i in a:
    if i > max_ele:
        max_ele = i
print(max_ele)'''

'''a = [68,80,19,24]
b = a[0]
for i in a:
    if i < b:
        b = i
print('Min:',b)'''

#Second largest element
#--using sort,index
'''list = [101,104,103,102]
list.sort()
print(list)
print('Second largest element:',list[len(list)-2])'''

#--using max()
'''list = [43,78,23,80,19]
largest = max(list) #80
second = list[0]
for i in list:
    if i != largest and i > second:
        second = i
print(second)'''


#Difference between .sort() and sorted()
#-- sort()
'''a =[]
for i in range(5):
    num = int(input('Enter number'+str(i + 1)+':'))
    a.append(num)
print('List:',a)
a.sort()
print('The sorted list:',a)'''

#-- sorted()
'''a = []
for i in range(5):
    num = int(input('Enter number'+str(i + 1)+':'))
    a.append(num)
print('List:',a)
result = sorted(a)
print('The sorted list:',result)
print('Original list:',a)'''

#Difference between reverse() and [::-1]
#-- reverse()
'''list = []
i = 0
while i <= 4:
    num = int(input('Enter number'+str(i + 1)+':'))
    list.append(num)
    i += 1
print('List:',list)
list.reverse()
print('Reversed list:',list)'''

#-- [::-1]
'''list = []
i = 0
while i <= 3:
    num = int(input('Enter number'+str(i + 1)+':'))
    list.append(num)
    i += 1
print('List:',list)
result = list[::-1]
print('Reversed list:',result)'''

#Removing duplicates in list
'''list = [] #101 102 101 103 102 104
i = 0
while i<=5:
    num = int(input('Enter number'+str(i + 1)+':'))
    list.append(num)
    i += 1
no_duplics = []
for i in list:
    if i not in no_duplics:
        no_duplics.append(i)
print('List without duplics:',no_duplics)'''

'''a = [101,102,101,103,102,104]
b = list(set(a))
print(sorted(b))
print(b)'''

#count the even & odd elements
'''num = input('Enter numbers:').split(',')
''''''a = list(num)
print('List:',a)
print(type(a))
print(type(a[0]))''''''
e_c = 0
o_c = 0
for i in num:
    if int(i)%2==0:
        e_c += 1
    else:
        o_c += 1
print('Even count:',e_c)
print('Odd count:',o_c)'''

#Search for a number & print its index if found
'''num = [10,24,19,6]
target = 19
for i in range (len(num)):
    if num[i] == target:
        print('Target at',i)'''

'''num = input().split()
target = 19
for i in range(len(num)):
    if int(num[i]) == target:
        print(i)'''

'''num = input().split()
target = 14
i = 0
while i < len(num):
    if int(num[i]) == target:
        print('Target at:',i)
    i += 1
else:
    print('No target is found')'''

#count no of elements in list
'''a = input().split()
target = 12
count = 0
for i in a:
    if int(i) == target:
        count+=1
print(count)'''

#reverse list without reverse() and slicing
'''a = [1,2,3,4]
rev = []
for i in a:
    rev = [i] + rev
print(rev)'''

#counting +ve & -ve numbers
'''num = [50,-3,96,-2]
pos_c = 0
neg_c = 0
for i in num:
    if i > 0:
        pos_c += 1
    else:
        neg_c += 1
print(pos_c)
print(neg_c)'''

#list having +ve numbers
'''num_list = input().split()
pos_num_list = []
for i in num_list:
    if int(i) > 0:
        pos_num_list.append(int (i))
print(pos_num_list)'''

'''num = [90,-10,3,-19,45,14,-9]
pos = []
for i in num:
    if i > 0:
        pos+= [i]
print(pos)'''

'''num = input().split()
pos = []
for i in num:
    if int(i) > 0:
        pos+= [int(i)]
print(pos)'''

'''num = input().split()
pos = []
i = 0
while i < len(num):
    if int(num[i]) > 0:
        pos += [int(num[i])]
    i += 1
print(pos)'''

#-----------aabbbccc----------------
'''for i in range(0,3):
    print(chr(97+i)*(i+2),end='')'''
#-----------------------------------

#Removing the duplicates without changing the order
'''num = [101,102,101,103,101,104]
ans = []
for i in num:
    if i not in ans:
        ans = ans + [i]
print(ans)'''

#Common element in 2 lists
'''a = [1,5,4,3,2]
b = [8,9,7,4,6]
for i in a:
    for j in b:
        if i == j:
            print('The common element in lists',i)'''

'''a = input().split()
b = input().split()
for i in a:
    for j in b:
        if int(i) == int(j):
            print('Common element',int(i))'''

'''a = [101,103,104,106]
b = [105,107,108,104]
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i]==b[j]:
            print('Common element:',a[i])
        j += 1
    i += 1'''

#returning only distinct common elements in list
'''a = [1,1,2]
b = [1,3]
c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c += [i] #(or) c.append(i)
            #print('Common element:',i)
print(*c) #list unpacking'''

#returns the common element with flag var
#--for loop
'''a = input().split()
b = input().split()
flag = False
for i in a:
    for j in b:
        if int(i) == int(j):
            flag = True
            print('Common element:',int(i))
            break
if flag == False:
    print('Common element is not found')'''

#--while loop
''''a = input().split()
b = input().split()
flag = False
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if int(a[i]) == int(b[j]):
            flag = True
            print('Common element:',int(a[i]))
            break
        j += 1
    i += 1
if flag == False:
    print('Common element is not found!')'''










