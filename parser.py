import mwparserfromhell
from xml.etree import cElementTree as ET
import sys

"""
Define the list of keywords in a file called keywords.def.
This script will then download this list and use it to collect all wikipedia articles that contain one of those keywords in their infobox.

This script get a slightly modified dump file as input. You will need to download a wikipedia dump and modify its workspace.
Just change the first line of the dump from <mediawiki namespace......> to <mediawiki>.

"""

wfilename = sys.argv[1]
wiki = ET.parse(wfilename)

with open("keywords.def", "r") as reqfile:
    requirements = [row.strip() for row in reqfile.readlines()]

for page in wiki.findall("page"):
    revision = page.find("revision")
    title = page.findtext("title")

    if revision and title:
        text = revision.findtext("text")
        try:
            parsed = mwparserfromhell.parse(text)
        except:
            continue

        for template in parsed.filter_templates():
            template_name = template.name.lower()

            if "infobox" in template.name.lower():
                for requirement in requirements:
                    if template.has(requirement):
                        print("%s" % (title))
                        break



