#creating list
'''a = []
for i in range(0,5):
    num = int(input('Enter a number '+str(i)+':'))
    a.append(num)
print(a)'''

'''list= [1,2,3,4]
print(list)'''

#printing elements of list
'''items = [10,'hello',3.14,True]
for i in items:
    print(i)'''

'''items = [10,20,30]
i = 0
while i < len(items):
    print(items[i])
    i += 1'''

#List slicing:-
'''num = [2,4,6,8,9,10,12,14]
print(len(num))
print(num[1:])
print(num[2:6])
print(num[:8])
print(num[0:len(num)])'''

#Nested lists:-
'''list_1 = [1,2,3]
list_2 = [4,5,6]
print('Two list together')
print(list_1,list_2)
print('list inside list')
print([list_1,list_2])'''

#Nested list indices:-
'''a = [101,102]
b = ['Adam','Bella']
print([a,b]) #[[101, 102], ['Adam', 'Bella']]
print(len([a,b]))
print([a,b][0])
print([a,b][1])
print([a,b][0][0])
print([a,b][0][1])
print([a,b][1][0])
print([a,b][1][1])'''

#list concatenation:-
'''list_1 = [10,20,30]
list_2 = [40,50,60]
print(list_1 + list_2)'''

#Replacing the values in list:-
'''num = [10,2,3,4,50,60]
num[1:4] = [20,30,40]
print(num)'''

#highest & lowest values in list:-
'''a = [10,30,50,20]
print(min(a))
print(max(a))'''

'''b = ['Diana','Michael','Elvis']
print(min(b))
print(max(b))
b.sort()
print(b)'''

#Adding the elements in list:-
#append()
'''num = [10,20,30]
print(num)
num.append(40)
print(num)

num.append([40,50])
print(num)

res = num.append(60) #[10,...,60]
print(res) #none'''

#extend()
'''num.extend([70,80])
print(num)

ans = num.extend([90,100]) #[10,...,100]
print(ans) #none'''

#insert()
'''num = [2,4,8,10]
num.insert(2,6)
print(num)

exam = [1,2,4,5]
print(exam.insert(2,3))'''

#Deleting the elements in list:-
#remove()
'''example = [10,20,30,40,20]
example.remove(20)
print(example)

print(example.remove(30)) #none'''

#pop()
'''ans = [10,20,30,40]
ans.pop()
print(ans)'''

'''num = [20,40,60,80]
num.pop(1) #index value
print(num)'''

'''var = [10,20,30,40]
res = var.pop()
print(res)    #40'''

#del()
'''num = [2,4,6,8,10,12,14,16]
del num[2:4]
print(num)'''

#clear()
'''num = [1,2,3,4,5]
num.clear()
print(num)'''

'''a = [11,22,33,44]
b = a.clear()
print(b) #none'''

#Searching the elements in list:-
#index()
'''num = [10,20,30,40,30,30,40]
ans = num.index(30)
print(ans)'''

#count()
'''num = [10,20,30,40,20,50]
ans = num.count(20)
print(ans)'''

#Arranging the elements in list:-
#sort()
'''num = [9,3,5,2,1,4,6,8,7,0]
num.sort()
print(num)

num.sort(reverse = True)
print(num)'''

#reverse
'''num = [6,4,5,1,9]
num.reverse()
print(num)'''

#copy
'''a = [1,2,3]
print(a)
b = a.copy()
print(b)'''

'''num = [1,2,3]
res = num.copy()
res.append(4)
print(num)
print(res)'''

'''num = [1,2,3]
res = num
num.append(4)
print(num)
print(res)'''

#---------------------------#
#PRACTICE QUESTIONS:-
#1.Create a list of 5 numbers. Print the first, last, and middle element.
'''a = [10,20,30,40,50]
print(a[0])
print(a[len(a)-1])
print(a[len(a)//2])'''

#2.Print all elements of a list using a while loop (instead of for).
'''a = [2,4,6,8,10]
i = 0
while i < len(a):
    print(a[i])
    i += 1'''

#3.Append and insert the values
'''a = [1,2,3]
a.append(4)
print(a)
a.insert(0,0)
print(a)'''

#4.Replacing the 2nd element
'''num = [10,20,30]
num[1] = 99
print(num)'''

#5.Remove vs Pop vs Del
'''a = [5,10,15,20]
a.remove(15)
print(a)
del a[0]
print(a)
a.pop()
print(a)'''

#6.Finding the index
'''list = [2,4,6,8,10]
a = list.index(8)
print(a)'''

#7.Counting the occurences
'''list = [1,2,2,3,2,4]
ans = list.count(2)
print(ans)'''

#8.Slicing
'''num = [10,20,30,40,50]
print(num[1:4])
print(num[::-1])'''

#9.Sum,Max,Min
'''list = [3,7,2,9,5]
print(sum(list))
print(max(list))
print(min(list))'''

#10.Matrix access
'''a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print([a,b,c])
print([a,b,c][1][1])
print([a,b,c][1])'''

#--------------------------------#
#1.Print elements with index
'''a = [2,4,6,8,10]
for i in range(len(a)):
    print(a[i],'-',i)'''

'''a = [2,4,6,8,10]
i = 0
while i < len(a):
    print(a[i],'-',i)
    i += 1'''

#2.Reverse traversal using while
'''a = [2,4,6,8,10]
i = len(a)- 1
while i>=0:
    print(a[i],end=' ')
    i -= 1'''

'''a = [2,4,6,8,10]
i = 0
while i < len(a):
    print(a[len(a)-1-i],end=' ')
    i += 1'''

#3.Sum of elements
'''a = [10,10,10,10]
sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print(sum)'''

'''a = [10,10,10,10]
sum = 0
i = 0
while i < len(a):
    sum += a[i]
    i += 1
print(sum)'''

#4.Traverse & maximum element in list
'''a = []
for i in range(5):
    num = int(input('Enter a number '+str(i)+':'))
    a.append(num)
print(a)

a.sort()
print(a)
print('The maximum element in list is ',a[len(a)-1])
print('The minimum element in list is ',a[0])'''

#5.Traverse & print all even,odd
'''a = []
for i in range(5):
    num = int(input('Enter number '+str(i)+':'))
    a.append(num)
print('List',a)

even_list=[]
odd_list=[]
for j in a:
    if j % 2 == 0:
        even_list.append(j)
    else:
        odd_list.append(j)
print('Even no. list:',even_list)
print('Odd no. list:',odd_list)'''

#6.Count the strings in list
'''a = ['Michael',1958, 6.5,'Diana',True,False,'Elvis']
count_str = 0
for i in a:
    if type(i) == str:
         count_str += 1
print(count_str)'''
        
#7.Search element
'''a = []
for i in range(4):
    num = int(input('Enter number '+str(i)+':'))
    a.append(num)
print('The list:',a)
i = 0
while i < len(a):
    if a[i] == 44:
        print(a.index(a[i]))
    i += 1'''

#8.Nested list traversal
'''a = []
b = []
c = []
for i in range(3):
    num = int(input('Enter number '+str(i)+':'))
    a.append(num)
print(a)
for j in range(3):
    num = int(input('Enter number '+str(j)+':'))
    b.append(num)
print(b)
for k in range(3):
    num = int(input('Enter number '+str(k)+':'))
    c.append(num)
print(c)
print([a,b,c])
for l in [a,b,c]:
    print(l,end='\n')'''

#9.Filter by above 50
'''a = []
for i in range(6):
    num = int(input('Enter number '+str(i)+':'))
    a.append(num)
print('List:',a)
new_list=[]
i = 0
while i < len(a):
    if a[i] > 50:
        new_list.append(a[i])
    i += 1
print(new_list)'''

#10.Index based traversal (while)
'''a = []
for i in range(4):
    num =int(input('Enter number '+str(i)+':'))
    a.append(num)
print('List:',a)
i = 0
while i < len(a):
    print(a[i],end='\n')
    i += 1'''
        













