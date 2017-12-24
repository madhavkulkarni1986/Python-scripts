'''
Python module to find the count each number of word in a web url.
The module accepts a url as input and prints the count of each word, extracted from the url, and prints to the console.

Syntax and Example:
      python3 word_counter.py http://exampleurl.com
'''

from urllib.request import urlopen
import sys

def count_words(url):
    with urlopen(url) as contents:
        words = dict()
        for line in contents:
            lwords=line.decode('utf-8').split()
            for word in lwords:
                if word in words:
                    words[word]=words[word]+1
                else:
                    words[word]=1
    return words

def print_count(words):
    for word in words:
        print(word," : ",words[word])

def main(url):
    words=count_words(url)
    print_count(words)

if(__name__ == '__main__'):
    main(sys.argv[1])
