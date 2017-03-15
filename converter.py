import os, re
import json
import pdb
import collections
from django.utils.text import slugify

sourceLink = 'http://gretil.sub.uni-goettingen.de/#Malayalam'
source = 'GRETIL'

def main():
    if not os.path.exists('cltk_json'):
        os.makedirs('cltk_json')

    for root, dirs, files in os.walk("."):
        path = root.split('/')
        for fname in files:
            if fname.startswith('chapter') or fname.endswith('txt'):
                #print((len(path) - 1) * '---', os.path.basename(root))
                title = fname.split('.')[0].title()
                work = {
                            'originalTitle': title,
                            'englishTitle': title,
                            'author': "Not Available",
                            'source': source,
                            'sourceLink': sourceLink,
                            'language': 'Malayalam',
                            'text': {},
                        }
                text = open(os.path.join(root, fname)).read().splitlines()
                text = [textNode.strip() for textNode in text if len(textNode.strip())]
                for i, textNode in enumerate(text):
                    work['text'][i] = textNode
                
                fname = slugify(work['source']) + '__' + slugify(work['englishTitle']) + '__' + slugify(work['language']) + '.json'
                fname = fname.replace(" ", "")
                with open('cltk_json/' + fname, 'w') as f:
                    json.dump(work, f)

if __name__ == '__main__':
    main()