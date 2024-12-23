password = input('Enter new password: ')
result = []
result_dic = {}

if len(password) >= 8:
    result.append(True)
    result_dic['length'] = True
else:
    result.append(False)
    result_dic['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit=True

result.append(digit)
result_dic['digit'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)
result_dic['uppercase'] = uppercase

print(result_dic)
print('Values of dic: ',result_dic.values())

if all(result):
    print('Strong password')
else:
    print('Weak Password')

if all(result_dic.values()):
    print('Strong password')
else:
    print('Weak password!!')
