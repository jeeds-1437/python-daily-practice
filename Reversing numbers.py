
#reversing a number using while loop
'''num = 1234
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 +digit
    num //= 10
print(rev)'''

#reversing a number using for loop
'''num = int(input('Enter a number:'))
length = len(str(num))
rev = 0
for i in range(length):
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)'''

#to check a number is palindrome or not
'''num = int(input('Enter a number:'))
temp = num
rev = 0
while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print(rev)
if rev == num:
    print('The number is a Palindrome')
else:
    print('The number is not a Palindrome')'''


