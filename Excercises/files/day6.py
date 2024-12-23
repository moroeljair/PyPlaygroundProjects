prompt = 'Add a new member: '
i = input(prompt)
file = open('files/members.txt','a+')
file.write(f'\n {i}')
