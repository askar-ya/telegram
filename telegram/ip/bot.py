import conf
import telebot
import json
import requests
import ipaddr
from telebot import apihelper

TOKEN = conf.TOKEN

apihelper.proxy = {'https':conf.proxy}
bot = telebot.TeleBot(TOKEN)

def search(ip, message):
	dot = 0
	slash = 0
	for i in ip:
		if i == '.':
			dot += 1
		if i == '/':
			slash += 1
	if dot == 3 and slash == 1:
		bot.send_sticker(message.chat.id, open('yes.webp', 'rb'))
		mask = ipaddr.IPv4Network(ip)
		ip = str(mask.netmask)
		return(ip)
	else:
		bot.send_sticker(message.chat.id, open('eror.webp', 'rb'))
		return('Не могу найти адрес!!(')

@bot.message_handler(content_types=['text'])
def main(message):
	if message.text == '/start':
		bot.send_sticker(message.chat.id, open('hai.webp', 'rb'))	
		bot.send_message(message.chat.id, 'Привет!!\nЯ могу найти адрес сети.\nНужно сообщение типа:\n\n192.192.45.1/25')
	else:
		ip = message.text		
		bot.send_message(message.chat.id, search(ip, message))

bot.polling(none_stop=True)