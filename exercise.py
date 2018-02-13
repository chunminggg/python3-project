from PIL import Image
import os
img = Image.open('launchImage.jpg')
new_img = img.resize((750,1334),Image.ANTIALIAS)
new_img.save('example-new.jpg',quality=100)
