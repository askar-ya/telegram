import conf
import telebot
import json
import PIL
import requests
from PIL import Image
from urllib.request import urlopen
from urllib import request as urlrequest
from telebot import apihelper


TOKEN = str(conf.TOKEN)

apihelper.proxy = {'https':conf.proxy}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def main(message):
	bot.send_message(message.chat.id, 'Подаждите секунду 🥺')	
	img = message.json
	img = img['photo']
	img = img[1]
	img = img['file_id']
	img = bot.get_file(img)
	img = img.file_path
	img = str(img)

	url = 'https://api.telegram.org/file/bot'+TOKEN+'/'+img
	proxy_host = '117.1.16.131:8080'

	req = urlrequest.Request(url)
	req.set_proxy(proxy_host, 'http')

	name = str(message.chat.id) + '.jpg'

	img = Image.open(urlrequest.urlopen(req))
	img.save(name)
	r = requests.post("https://api.deepai.org/api/colorizer",files={'image': open(name, 'rb'),},headers={'api-key': '2c9b0572-8797-46f4-ae43-477531a3bc9d'})
	url = r.json()
	url = url['output_url']

	image = Image.open(urlopen(url))
	image.save(name)

	bot.send_photo(message.chat.id, url)

@bot.message_handler(content_types=['text'])
def chat(message):
	if message.text == '/start':
		sti = open('sticker.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)
		bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ крашу ч.б. фото.'.format(message.from_user, bot.get_me()),
		parse_mode='html')
	if message.text == 'знаешь Марата?':
		bot.send_message(message.chat.id, 'Да, тот ещё плов😍')	
	if message.text == 'Рекардо':
		sti = open('rec.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)		

@bot.message_handler(content_types=['document'])
def exd(message):
	bot.send_message(message.chat.id, 'отправь фото, а не файл')

@bot.message_handler(content_types=['voice'])
def exa(message):
	bot.send_photo(message.chat.id, 'http://risovach.ru/upload/2016/11/mem/ya-konechno-ne-budu_128534441_orig_.jpg')


bot.polling(none_stop=True)
