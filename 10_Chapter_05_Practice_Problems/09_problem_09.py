s = {8,7,12,'Farooque',[1,2,3]} # This will raise a TypeError because lists are not hashable

s[4][0]=100 # This will raise a TypeError because sets are unordered and do not support indexing
# s.add(100) # This will raise a TypeError because sets cannot contain mutable types like lists