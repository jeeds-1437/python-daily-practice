#WHILE LOOP
'''i=1
while (i<=5):
    print(i)
    i+=1'''

#using break statement
'''i=1
while(i<=5):
    if(i==3):
        break
    print(i)
    i+=1'''

#using continue statement
'''i = 1
while i <= 5:
    if i == 3:
        i +=1
        continue 
    print(i)
    i+=1'''

#PRINT 1 TO 10
'''i = 1
while i<=10:
    print(i,end=' ')
    i += 1'''

#PRINT 10 TO 1
'''i = 10
while i >= 1:
    print(i,end =' ')
    i-=1'''

#EVEN NO. 1 TO 20
'''i = 1
while i <=20:
    if i%2 == 0:
        print(i,end = ' ')
    i += 1'''

#ODD NO. 1 TO 20
'''i = 1
while i <=20:
    if i % 2 == 1:
        print(i,end=' ')
    i +=1'''

#SUM OF n NATURAL NUMBERS
'''i=1
n=int(input("Enter the number:"))
while (i<=n): 
    sum = n * ((n+1)/2) 
    i += 1
print("The sum of n Natural numbers is ",sum)'''

'''(or)sum = 0
inside loop --> sum = sum + i'''

#REVERSING NUMBERS
'''num = int(input("Enter number to be reversed:"))
rev = 0
while (num != 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)'''

#ATM BALANCE
'''balance = 10000
while (True):
    print('---ATM Menu---')
    print('1.Check balance')
    print('2.Withdraw')
    print('3.Exit')
    choice = int(input("Enter your choice (1-3):"))
    if (choice == 1):
        print('Your balance is ',balance)
    elif(choice == 2):
        amount = int(input("Enter the amount to be withdraw: "))
        if(amount <= balance):
                balance -= amount
                print('Withdrawn done!,remaining balance is ',balance)
        else:
                print('Insufficient balance')
    elif(choice == 3):
        print("Thankyou! Come again!")
        break
    else:
        print("Invalid choice")'''

#NUMBER GUESSING GAME
'''import random
secret_num = random.randint(1,100)
while True:
    print('Number guessing game...!')
    guess_num = int(input("Enter your guess (1-100):"))
    if guess_num < secret_num:
        print("Too low! Try again!")
    elif guess_num > secret_num:
        print("Too high! Try again!")
    else:
        print("You win!!")
        break'''

#LOGIN AFTER 3 ATTEMPTS
'''correct_password = 1403
i = 1
while i <= 3:
    password = int(input("Enter your password: "))
    if (password == correct_password):
        print("login is done!")
        break
    else:
        print("Incorrect password!,Try again..!")
    i += 1
else:
    print('Your account is blocked after too many attempts!')'''

#SIMPLE CALCULATOR USING EXIT
'''a = int(input("Enter a number_1: "))
b = int(input("Enter a number_2: "))
while True:
    print('Simple Calc Menu')
    print('1.Addition')
    print('2.Subraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Exit')
    choice = int(input("Your choice is: "))
    if choice == 1:
        print('Adding 2 numbers is ',a+b)
    elif choice == 2:
        print('Subracting 2 numbers is ',a-b)
    elif choice == 3:
        print('Multiplying 2 numbers is ',a*b)
    elif choice == 4:
        print('Dividing 2 numbers is ',a/b)
    elif choice == 5:
        print('Exit')
        break
    else:
        print('Invalid choice!')'''

#RIGHT TRIANGLE PATTERN
'''i = 1
while i <= 4:
    j = 1
    while j <= i:
        print ('*',end=' ')
        j += 1
    print()
    i += 1'''

#INVERTED RIGHT TRIANGLE
'''i = 4
while i >= 1:
    j = 1
    while j <= i:
        print('*',end=' ')
        j += 1
    print()
    i -= 1'''

#NUMBER TRIANGLE
'''i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(j,end=' ')
        j += 1
    print()
    i += 1'''

#INVERTED NUMBER TRIANGLE
'''i = 4
while i >= 1:
    j = 1
    while j <= i:
        print(j,end=' ')
        j += 1
    print()
    i -= 1'''

#FACTORIAL
'''fact = 1
n=int(input("Enter a num:"))
i = 1
while i<= n:
    fact = fact * i
    i += 1
print(fact)'''

#ARMSTRONG NUMBER
'''num = int(input("Enter a number:"))
length = len(str(num))
sum = 0
temp=num
while (temp > 0):
    digit = temp % 10
    sum = sum + digit ** length
    temp = temp // 10
print(sum)
if (num == sum):
    print("This armstrong number!")
else:
    print("This is not an armstrong number!")'''

'''for i in range(0,10):
    current = i
    if (i==0):
        previous = 0
    else:
        previous = i - 1
    sum = current + previous
print(sum)'''

#FIBONACCI SERIES
'''first = 0
second = 1
print(first)
print(second)
i = 0
while (i <= 7):
    next = first + second
    print(next)
    first = second
    second = next
    i+= 1'''

'''first = 0
second = 1
for i in range(0,8):
    next = first + second
    print(next,end=' ')
    first= second
    second=next'''





            
                    























