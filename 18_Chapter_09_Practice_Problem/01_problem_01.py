f = open('01_poem.txt')
content = f.read()

if('twinkle' in content.lower()):
    print('The Word Twinkle is present in the Content..')
else:
    print('The Word Twinkle is not present in the Content...')

f.close()