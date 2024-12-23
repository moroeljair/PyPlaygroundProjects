with open('../files/doc.txt', 'r') as file:
    cont = file.read()

print(cont)

date = input("Enter today's date:  ")
mood = input("How do you rate your mood today from 1 to 10?")
journal = input("Let your thoughts flow: \n")

with open(f'../files/journal/{date}','w') as file:
    file.write(mood + 2 * '\n')
    file.write(journal)

