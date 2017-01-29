import kenlm
import glob
import gzip
import os
import sys
import chardet
from byeHTML import byeHTML

filesdir = sys.argv[1]

filenames = glob.glob(os.path.join(filesdir, "*"))

model_simple = kenlm.LanguageModel('simplewiki.o3.arpa')
model_en     = kenlm.LanguageModel('enwiki.o3.arpa')

def find_encoding(doc_full_path):
    # http://chardet.readthedocs.io/en/latest/usage.html
    # This method uses the traditional chardet to find out the encoding used in a file
    if doc_full_path.endswith(".gz"):
        f = gzip.open(doc_full_path, mode="rb")
    else:
        f = open(doc_full_path, mode="rb")

    rawdata = f.read()
    return chardet.detect(rawdata)["encoding"]

for filename in filenames:
    encoding = find_encoding(filename)

    if filename.endswith(".gz"):
        with gzip.open(filename, mode="rt", encoding=encoding, errors="surrogateescape") as f:
            content = str(f.read()) # Explicitly convert from bytes to str
    else:
        with open(filename, encoding=encoding, errors="surrogateescape", mode="r") as f:
            content = f.read()

    text = byeHTML(content, preprocesshtml="justext", forcePeriod=False).get_text()

    print("%s,%.3f,%.3f" % (filename, model_simple.score(text), model_en.score(text)))

