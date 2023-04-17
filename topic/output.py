
import os
import shutil
import yaml
from model import Article

dir = "output"
yamlPath = dir + os.sep + "metadata.yaml"

def output(arts):

    if not os.path.exists(dir):
        os.makedirs(dir)

    for art in arts:
        if not hasattr(art, 'content'):
            arts.remove(art)
            continue

        if len(art.content) == 0:
            arts.remove(art)
        outPath = dir + os.sep + art.title.replace(" ", "_") + ".txt"
        toTxt(art.content, outPath)
    toMetadataInYamlFormat(arts, yamlPath)

def reset():
    if os.path.exists(dir):
        shutil.rmtree(dir)


def toMetadataInYamlFormat(arts, yamlPath):
    print("Write to metadata: " + yamlPath)
    data = {
        "articles": arts
    }

    yaml.emitter.Emitter.prepare_tag = lambda self, tag: ''
    with open(yamlPath, 'w') as out:
        yaml.dump(data, out, default_flow_style=False, encoding="utf8", allow_unicode=True)
        
def toTxt(art, outPath):
    print("Write output to: " + outPath)
    outputFile = open(outPath, "w")
    outputFile.writelines(art)