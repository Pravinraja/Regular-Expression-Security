import re #regular expression package
print('Input a strong password: ')
password = input()
if re.match(r'^([a-zA-Z0-9@#$%^&+=]{12})$', password): # use re.match to check for casing, length, numbers, and special char
    print('Password is ok')
else:
    print('Password is not ok')