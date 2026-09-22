#SQUARE PATTERN
'''for i in range(1,5):
    for j in range(1,5):
        print('*',end='')
    print('\n')'''

#NUMBERS - SQUARE PATTERN
'''for i in range(1,5):
    for j in range(1,5):
        print(i,end=' ')
    print(end='\n')'''

#INCREASING STAR TRIANGLE
'''for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n')'''

#DECREASING STAR TRIANGLE
'''for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()'''

#NUMBERS - INVERTED PATTERN
'''for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

#HORIZONTAL NUMBERS
'''for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()'''

#CONTINUOUS NUMBERS
'''num=1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=' ')
        num = num+1
    print()'''

#ALPHABET NUMBERS
'''for i in range(1,5):
    for j in range(1,5):
        print(i,end=' ')
    print()'''

#RIGHT ANGLED NUMBER PATTERN
'''for i in range(5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

#INVERTED RIGHT ANGLED NUMBER PATTERN
'''for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

#RIGHT ALIGNED INCREASING PATTERN
'''for i in range(1,5):
    for j in range(5-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()'''

#RIGHT ALLIGNED DECREASING PATTERN
'''for i in range(1,5):
    for j in range(i-1):
        print(' ',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()'''


#square pattern with diagonal stars
'''n = 8
for i in range(1,9):
    for j in range(1,9):
        if i == 1 or i == 8:
            print('*',end=' ')
        elif j == 1 or j == 8:
            print('*',end=' ')
        elif i == j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hour glass
'''for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5:
            print('*',end=' ')
        elif (i == 2 and j == 2) or (i == 4 and j == 4):
            print('*',end=' ')
        elif (i + j )- 1 == 5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#diamond pattern
for i in range(1,8):
    for j in range(1,8):
        if i == 1 and j == 8:
            print('*',end='')
        elif i == 2 and j == 6 or j == 3 and j == 5:
            print('',end='')
        else:
            print('*',end='')
        
    print()
        
            
    


















