# jsonnotes.py - module to read a json file and return it as a dictionary

import json

def readjsonfile(filename) -> {}:
    file = open(filename)
    text = file.read()
    dict = json.loads(text)
    return dict
