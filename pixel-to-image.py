#Write a program that consumes pixel values and creates an image.
from PIL import Image

def convert(code):
    if code == "R":
        return (237, 28, 36)
    elif code == "B":
        return (0, 0, 0)
    elif code == "Y":
        return (255, 242, 0)
    else:
        return (255, 255, 255)

input_text_file = open(r"C:\Users\srina\OneDrive\Desktop\CS240-HW\Homework 1\awesome_picture.txt","r")
lines = input_text_file.readlines()

h = len(lines)
w = len(lines[0].split())

img = Image.new(mode="RGB", size=(w, h), color=(0, 0, 0))

for y in range(h):
    pixels = lines[y].split()

    for x in range(len(pixels)):
        pixel = pixels[x]
        img.putpixel((x, y), convert(pixel))

img.save("smiley2.png")
img.show()