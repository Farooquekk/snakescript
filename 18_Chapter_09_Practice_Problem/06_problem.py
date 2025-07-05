with open('06_file.txt','r') as f:
    contents = f.read()

    if('python' in contents):
        print("Yes python is present...")
    else:
        print('python is not present....')

