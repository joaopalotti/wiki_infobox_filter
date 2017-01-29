import wikipedia
import sys

title_file_input = sys.argv[1]
outdir = sys.argv[2]

def download_to(title, dst):
    try:
       #page = wikipedia.page(title)
       suggestion = wikipedia.search(title, results=1, suggestion=True)[0]
       page = wikipedia.page(suggestion)
    except:
        print("Not found: %s" % (title))
        return
    content = page.content

    with open(dst, "w") as f:
        f.write(content)


wikipedia.set_lang("en")
with open(title_file_input, "r") as titles_file:
    for title in titles_file.readlines():
        title = title.strip()
        download_to(title, os.path.join(outdir, title.replace(" ","_")))



