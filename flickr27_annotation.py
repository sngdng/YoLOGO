import os
from collections import defaultdict

#brand = ["Adidas", "Apple", "BMW", "Citroen", "Coca Cola", "DHL", "Fedex", "Ferrari", "Ford", "Google", "Heineken", "HP", "McDonalds", "Mini", "Nbc", "Nike", "Pepsi", "Porsche", "Puma", "Red Bull", "Sprite", "Starbucks", "Intel", "Texaco", "Unisef", "Vodafone", "Yahoo"]

brand = ["Fedex", "Nike", "Intel", "Apple", "Mini"]

SOURCE_DIR = os.getcwd()

train_data = SOURCE_DIR + "/data/train_annotation.txt"

new_annotation = defaultdict(list)

with open(train_data, "r") as data:
    lines = data.readlines()
    for line in lines:
        strLine = line.split()
        path = SOURCE_DIR + "/data/images/" + strLine[0]
        if strLine[1] in brand:
            class_id = brand.index(strLine[1])
            if(not strLine[-4] + "," + strLine[-3] + "," + strLine[-2] + "," + strLine[-1] + "," + str(class_id) in new_annotation[path]):
                new_annotation[path].append(strLine[-4] + "," + strLine[-3] + "," + strLine[-2] + "," + strLine[-1] + "," + str(class_id))

with open("flickr5_train.txt", "w") as f:
    for path in new_annotation:
        f.write(path + " " +" ".join(new_annotation[path]) + "\n")
f.close()
