from threading import Thread
from datetime import datetime
import requests

The_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []
time_start = datetime.now()

def func(url):
    response = requests.get(The_URL)
    page_response = response.json()
    res.append(page_response)

the_first = Thread(target=func, args=(The_URL, ))
the_second = Thread(target=func, args=(The_URL, ))
the_third = Thread(target=func, args=(The_URL, ))

the_first.start()
the_second.start()
the_third.start()

the_first.join()
the_second.join()
the_third.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
print(res)