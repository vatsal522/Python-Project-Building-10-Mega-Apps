import json
import os
import difflib 
if os.path.exists('data.json'):
    data=json.load(open('data.json'))
    print('path checked and verified ')
    print('Enter exit() to exit the program ')
else:
    print('Dataset not found')


while True:
    def translate(w):
        w=w.lower()
        if w in data:
            return data[w]
        elif w=='exit()':
            exit()
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        else:
            difflib.get_close_matches(w,data.keys(),2,0.6)
            return "Did you mean {} instead of {} ?".format(difflib.get_close_matches(w,data.keys(),2,0.6),w)
    word=input('Enter word to find meaning: ')
    output=translate(word)
    if type(output)==list:
        for x in output:
            print(x)
            print("")

        print("-------------")
    else:
        print(output)
