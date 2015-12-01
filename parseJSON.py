import json
import copy
import sys




catalog = open("jsoncatalog.txt","w")
unigrams = open("unigrams.txt","w")
bigrams = open("bigrams.txt","w")

rewriteWordcounts=True

for file in sys.argv[1:]:
    for line in open(file):
        data = json.loads(line)
        metadata = copy.deepcopy(data)
        del metadata['data']
        metadata['filename'] = metadata['doi']
        del metadata['doi']
        catalog.write(json.dumps(metadata) + "\n")
        for key in metadata.keys():
            metadata[key.replace("-date","")] = metadata[key]
                
        if rewriteWordcounts:
            for line in data['data']['1-grams']:
                try:
                    unigrams.write(data['doi'] + "\t")
                    unigrams.write(line[0].encode("utf-8"))
                    unigrams.write("\t" + str(line[1]) + "\n")
                except UnicodeError:
                    sys.stderr.write(line[0] + "\n")
                    raise

            for line in data['data']['2-grams']:
                try:
                    bigrams.write(data['doi'] + "\t")
                    bigrams.write(line[0].encode("utf-8"))
                    bigrams.write("\t" + str(line[1]) + "\n")
                    #unigrams.write(u"\t".join([data['doi'],unicode(line[0]).encode("utf-8"),str(line[1])]) + "\n")
                except UnicodeError:
                    sys.stderr.write(line[0] + "\n")
                    raise
