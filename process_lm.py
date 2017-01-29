
import sys
import nltk

for line in sys.stdin:
    line = line.replace("="," ")
    for sentence in nltk.sent_tokenize(line):
        print(' '.join(nltk.word_tokenize(sentence)).lower())



