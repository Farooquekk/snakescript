l = ["Harry","Farooque","Babar","Arbab","Talha","Ada Dogesh"]

print(l)
def rem(l,word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))

    return n
    

output  = rem(l,"ar")
print(output)