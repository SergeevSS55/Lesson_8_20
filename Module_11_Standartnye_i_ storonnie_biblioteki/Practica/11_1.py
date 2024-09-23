from PIL import Image
from PIL import ImageDraw, ImageFont


# im = Image.open('photo.jpg')
#
# print(im.format, im.size, im.mode)
# w, h = im.size
#
# out = im.resize((w//2, h//2))
#
# out.show()

# print(dir(Image))

def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('photo.jpg')
im_2 = new_photo('sun.png')
# im_2.show()
w, h = im.size

im.paste(im_2, (w - 1185, h - 900))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('Waltographui.ttf', 30)
draw.text((0, 0), 'Hello, bro', font=font, fill='red')

im.show()
