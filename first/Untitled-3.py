ACCOUNT = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if ACCOUNT == user_account and password == user_password:
    print('success')
else:
    print('fail')
