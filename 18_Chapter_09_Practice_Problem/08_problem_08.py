with open('08_this.txt') as f:
    content=f.read()


with open('08_this_copy.txt','w') as f:
    f.write(content)
 