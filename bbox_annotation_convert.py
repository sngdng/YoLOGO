import os
from collections import defaultdict

SOURCE_DIR = os.getcwd()

classes = []

with open('class.txt', "r") as f:
    for line in f.readlines():
        classes.append(line.split()[-1])
f.close()

def convertAnnotation(filename, newAnnotation):
    with open(filename, "r") as f:
        listeAnnotation = f.readlines()
        for i in range(1, len(listeAnnotation)):
            bbox = listeAnnotation[i].split()
            newAnnotation[filename].append(bbox[0] + "," + bbox[1] + "," + bbox[2] + "," + bbox[3] + "," + str(classes.index(bbox[4])))
    f.close()

if __name__ == '__main__':
    new_Annotation = defaultdict(list)
    dir = os.listdir(SOURCE_DIR + "/Labels/")
    for filename in dir:
        convertAnnotation(SOURCE_DIR + "/Labels/" + filename, new_Annotation)
    with open('annotation.txt', "w") as f:
        for fileName in new_Annotation:
            f.write(SOURCE_DIR + "/Images/" + fileName.split("/")[-1] + " " + " ".join(new_Annotation[fileName]) + "\n")
    f.close()