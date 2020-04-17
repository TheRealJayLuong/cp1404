"""Display the number by using list function"""
numbers = [5,20,1,2,3]
for number in numbers:
    print("Number is :",number)

print("The first number is",numbers[0])
print("The last number is",numbers[-1])
print("the smallest number is",min(numbers))
print("the largest number is",max(numbers))
print("the average number is",sum(numbers)/len(numbers))
print("-------------")
"""checking valid name in user list that have given """
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_username = input("Enter your name")
if get_username in usernames:
    print("Access granted")
else:
    print("Access denied")
