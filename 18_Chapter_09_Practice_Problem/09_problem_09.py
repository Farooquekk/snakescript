with open('09_file_01.txt') as f:
    contents_01 = f.read()

with open('09_file_02.txt') as f:
    contents_02 = f.read()

if(contents_01==contents_02):
    print('Yes both files contents is same')
else:
    print('Both files contents are different')
