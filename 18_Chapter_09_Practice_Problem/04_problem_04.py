word = 'Donkey'

with open('04_file.txt','r') as f:
    content=f.read()

contentNew = content.replace(word,'######')

with open('04_file.txt','w') as f:
    f.write(contentNew)
     
