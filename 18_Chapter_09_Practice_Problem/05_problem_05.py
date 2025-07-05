words = ['Donkey', 'bad', 'ganda']

with open('04_file.txt','r') as f:
    content=f.read()

for word in words:
    content = content.replace(word,'#'*len(word))



with open('04_file.txt','w') as f:
    f.write(content)
     
