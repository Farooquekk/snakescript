import os

with open('11_file.txt') as f:
    content = f.read()
with open('11_renamed_by_python.txt','w') as f:
    f.write(content)

if(os.path.exists('11_file.txt')):
    os.remove('11_file.txt')
    print('File Deleted Successfully')
else:
    print('File not found...')