import json
import re
import sys


keywords = ["[Gg]lobal [Hh]istory","[Ww]orld [Hh]istory"]

print "filename\tkeyword"

for line in sys.stdin:
    filename = re.search(r'"doi": "([^"]*)"',line).groups()[0]
    matches = []
    for keyword in keywords:
        if re.search(keyword,line):
            matches.append(keyword)
    print "%s\t%s" %(filename,"--".join(matches))
            
