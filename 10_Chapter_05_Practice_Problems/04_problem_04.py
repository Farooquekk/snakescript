s = set()
s.add(1)
s.add(1.0) # 1 and 1.0 are considered the same in a set
s.add('1')
print(s)
print(len(s))