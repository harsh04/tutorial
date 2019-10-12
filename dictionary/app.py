import json
from difflib import get_close_matches as gcm

data = json.load(open('dictionary\data.json'))

def meaning(word):
    if word in data:
        return '\n'.join(data[word])
    elif word.lower() in data:
        return '\n'.join(data[word.lower()])
    elif word.title() in data:
        return '\n'.join(data[word.title()])
    else:
        similar = gcm(word, data.keys(), n=1)
        ans = input(f'Do you mean {similar[0]}? Enter y or n: ')
        if ans == 'y':
            return meaning(similar[0])
        else:    
            return f'{word} not present in dictionary'

while True:
    word = input('Enter word : ')
    if word == '\end':
        break
    else: 
        print('--------------------------------------------------------')
        print(meaning(word))
        print('--------------------------------------------------------')
