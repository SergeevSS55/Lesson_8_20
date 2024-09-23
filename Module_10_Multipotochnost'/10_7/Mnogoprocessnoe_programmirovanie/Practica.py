import datetime
import multiprocessing as mp
from PIL import Image
from queue import Empty


# def resize_Image(image_paths, queue):
#     for image_path in image_paths:
#         image = Image.open(image_path)
#         image = image.resize((800, 600))
#         queue.put((image_path, image))  # image.save(image_path)
#
#
# def change_color(queue):
#     while True:
#         try:
#             image_path, image = queue.get(timeout= 5) # если в очередь ничего не поступает в течение 5 сек
#         except Empty:
#             break
#         image = image.convert('L')  # метод - "L" делает картинку ЧБ
#         image.save(image_path)
#
# if __name__ == '__main__':
#     data = []
#     queue = mp.Queue()
#
#     # for image in range(1, 201):
#     data.append(f'./Image/img_1.jpg')  # data.append(f'./Image/img_{image}.jpg')
#
#     resize_process = mp.Process(target=resize_Image, args=(data, queue))
#     change_process = mp.Process(target=change_color, args=(queue, ))
#
#     start = datetime.datetime.now()
#
#     resize_process.start()
#     change_process.start()
#
#     resize_process.join()
#     change_process.join()
#
#     end = datetime.datetime.now()
#
#     print(end - start)



def resize_Image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        image.save(image_path)
        pipe.send(image_path)  # image.save(image_path)
    stop_event.set()

def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv # если в очередь ничего не поступает в течение 5 сек
        image = Image.open(image_path)
        image = image.convert('L')  # метод - "L" делает картинку ЧБ
        image.save(image_path)

if __name__ == '__main__':
    data = []
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event
    # for image in range(1, 201):
    data.append(f'./Image/img_1.jpg')  # data.append(f'./Image/img_{image}.jpg')

    resize_process = mp.Process(target=resize_Image, args=(data, conn1, stop_event))
    change_process = mp.Process(target=change_color, args=(conn2, stop_event))

    start = datetime.datetime.now()

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()

    end = datetime.datetime.now()

    print(end - start)