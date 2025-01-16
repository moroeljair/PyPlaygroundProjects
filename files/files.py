with open("new.txt", "w") as file:
    file.writelines(['Hello\n','My\n','Name\n',"is Jair\n"])

with open("new.txt", "r") as f:
    
    l2 = f.readlines()
    print(l2)