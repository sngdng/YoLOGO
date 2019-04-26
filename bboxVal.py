from PIL import Image, ImageFont, ImageDraw
import os


with open('flickr5_train.txt', "r") as f:
    liste = f.readlines()
    for i in range(len(liste)):
        string = liste[i].split(" ")
        coord = string[1].split(",")
        image = Image.open(string[0])
        draw = ImageDraw.Draw(image)
        top, left, bottom, right = int(coord[1]), int(coord[0]), int(coord[3]), int(coord[2])

        draw.rectangle(
                [left + 10, top + 10, right - 10, bottom - 10],
                outline=(0,0,0))
        image.save('bbox/'+string[0].split('/')[-1])
