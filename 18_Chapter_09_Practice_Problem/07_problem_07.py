with open('06_file.txt','r') as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if('python' in line):
        print(f"Yes python is present at line number : {lineno}")
        break
    lineno+=1
else:
        print('python is not present....')

