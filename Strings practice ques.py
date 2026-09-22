#LEVEL 1
#1.String as i/p and its length
'''string = input('Enter a string:')
print(len(string))'''

#2.printing first and last char of string
'''string = input('Enter a string:')
print(string[0])
print(string[len(string)-1])'''

#3.printing every char on sep line
'''string = input('Enter a string:')
for i in string:
    print(i)'''

#4.Count vowels in string
'''string = input('Enter a string:')
v_count = 0
for i in string:
    if i in ['a','e','i','o','u']:
        v_count += 1
print(v_count)'''

#5.count consonants in string
'''string = input('Enter a string:')
c_count = 0
for i in string:
    if i not in ['a','e','i','o','u']:
        c_count += 1
print(c_count)'''

#6.strings in upper and lowercases
'''string = input('Enter a string:')
print(string.upper())
print(string.lower())'''

#7.check str starts with'Py'
'''string = input('Enter string:')
print(string.startswith('Py'))'''

#8.count particular char in string
'''string = 'My name is Jeevitha. I\'m currently pursuing B.E CSE(AIML) at KRCT'
count = 0
for i in string:
    if i == 'i':
        count += 1
print(count)'''

#LEVEL 2
#9.indexing & slicing
'''s='PythonProgramming'
print(s[0:6])
print(s[12::])
print(s[2:9])
print(s[0:len(s):2])
print(s[1:len(s):2])'''

#10.reversing the string
#using 'rev' variable
'''string = input('Enter a string:')
rev =""
for ch in string:
    rev = ch + rev
print(rev)'''










