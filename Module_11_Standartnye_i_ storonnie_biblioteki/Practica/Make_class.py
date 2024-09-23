from PIL import Image
from PIL import ImageDraw, ImageFont


class PostMaker:

    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))
        self.image.show()

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((paste_image.size[0] // 2, paste_image.size[1] // 2))
        self.image.paste(paste_image, (200, 200))
        self.image.show()

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('Waltographui.ttf', 30)
        draw.text((150, 100), text, font=font)
        self.image.show()


image = PostMaker('photo.jpg')
image.paste('sun.png')
image.upgrade('Hello')
