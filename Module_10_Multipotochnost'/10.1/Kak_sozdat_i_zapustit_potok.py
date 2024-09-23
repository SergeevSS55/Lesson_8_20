import requests
from datetime import datetime

time_start = datetime.now()
The_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []

for i in range(10):
    response = requests.get(The_URL)
    page_response = response.json()
    res.append(page_response)
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
print(res)
