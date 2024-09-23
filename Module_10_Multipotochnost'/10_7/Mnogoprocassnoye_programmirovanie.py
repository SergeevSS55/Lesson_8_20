import multiprocessing
from PIL import Image
import datetime


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


start = datetime.datetime.now()
image_path = f'./Image/img_1.jpg'
resize_image(image_path)
end = datetime.datetime.now()
print(end - start)
