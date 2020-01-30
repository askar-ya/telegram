import PIL
import requests
from PIL import Image
from urllib.request import urlopen
from urllib import request as urlrequest
proxy_host = '117.1.16.131:8080'    # host and port of your proxy
url = 'https://api.telegram.org/file/bot1096065958:AAGteV4doPSt3q-7eLm40f4qE2GZtWFgF-M/photos/file_1.jpg'

req = urlrequest.Request(url)
req.set_proxy(proxy_host, 'http')

img = Image.open(urlrequest.urlopen(req))
img.save('123.jpg')

r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('123.jpg', 'rb'),
    },
    headers={'api-key': '2c9b0572-8797-46f4-ae43-477531a3bc9d'}
)

url = r.json()
url = url['output_url']

image = Image.open(urlopen(url))
image.save('123.jpg')