#Write a program that reads an image and prints its pixel values.
from PIL import Image

def convert(color):
    red, green, blue = color[:3]

    if red == 0 and green == 162 and blue == 232:
        return "B" # Blue
    elif red == 34 and green == 177 and blue == 76:
        return "G" # Green
    elif red == 84 and green == 38 and blue == 34:
        return "D" # Dark Brown
    elif red == 136 and green == 0 and blue == 21:
        return "R" # Red
    elif red == 181 and green == 230 and blue == 29:
        return "L" # Lime green
    elif red == 185 and green == 122 and blue == 87:
        return "T" # Tan
    elif red == 255 and green == 255 and blue == 255:
        return "W" # White
    else:
        return f"({red}, {green}, {blue})"


image_file = Image.open(r"C:\Users\srina\OneDrive\Desktop\CS240-HW\Homework 1\Landscape.png").convert("RGB")
width, height = image_file.size

with open("output.txt", "w") as output_file:
    for y in range(height):
        for x in range(width):
            color = image_file.getpixel((x, y))
            converted_color = convert(color)

            output_file.write(converted_color)
            output_file.write(" ")

        output_file.write("\n")