#Control statements
#break stt in for loops:-
'''for i in range(1,6):
    if i == 3:
        break
    print(i)'''

'''for i in range(1,6):
    print(i)
    if i == 3:
        break'''

#break stt in while loops:-
'''i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1'''

'''i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1'''

#break & continue stt with string and loops:-
'''i = 0
a = 'GeeksforGeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        break
    print( a[i])
    i += 1'''

'''i = 0
a = 'Michael Jackson'
while i < len(a):
    if a[i] == ' ' or a[i] == 'J':
        break
    print( a[i],end=' ' )
    i += 1'''

'''i = 0
a = 'GeeksforGeeks'
while i < len(a):
    if (a[i] == 'e' or a[i] == 's'):
        i += 1
        continue
    print(a[i])
    i += 1'''

'''i = 0
a = 'GeeksforGeeks'
while i < len(a):
    print(a[i])
    if a[i] == 'e' or a[i] == 's':
        break
    i += 1'''

#Pass stt:
'''i = 0
a = 'Michael Jackson'
while i < len(a):
    i += 1
    pass
print('Value of i :',i)'''

#PRACTICE QUESTIONS
#for loop prints numbers from 1 to 10, but stops completely when it reaches 6 (use break).

#for loop prints numbers from 1 to 10, but skips printing 5 (use continue).

#for loop iterates through numbers 1 to 5, but does nothing when the number is 3 (use pass).:-
'''for i in range(1,11):
    if i == 6:
        break
    print(i)'''

'''i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1'''

'''for i in range(1,11):
    if i == 5:
        i += 1
        continue
    print(i)'''

'''i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1'''

'''for i in range(1,6):
    if i == 3:
        pass
    print(i)'''

'''i = 1
while i <= 5:
    i += 1
    pass
print(i)'''
