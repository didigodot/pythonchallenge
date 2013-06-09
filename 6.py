from PIL import Image, ImageMath
im = Image.open('oxygen.png')
size = im.size
print [im.getpixel((x, 45)) for x in range(size[0])]

