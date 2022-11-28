# функции, используемые в работе бота

import vk_settings
import keyboard_set
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

kb = keyboard_set.kb()
vk = vk_settings.vk

vkapi = vk_settings.vkapi
longpoll = vk_settings.longpoll
upload = vk_settings.upload
VkEventType = vk_settings.VkEventType
get_random_id = vk_settings.get_random_id
from random import randint


class Main:

	def get_name(
	  self, user_id):  # запрос имени, фамилии и пола юзера. пока не используется
		info = vk.method('users.get', {"user_id": user_id, 'fields': 'sex'})
		f_n = info[0]['first_name']
		l_n = info[0]['last_name']
		gend = info[0]['sex']
		return (f_n, l_n, gend)

	def write_msg(self, user_id, message):  # отправка сообщения
		vk.method('messages.send', {
		 'peer_id': user_id,
		 'message': message,
		 "random_id": get_random_id()
		})

	def msg_kb(self, user_id, message,
	           keyboard):  # отправка необходимой клавиатуры и сообщения
		vk.method(
		 'messages.send', {
		  'peer_id': user_id,
		  'message': message,
		  'random_id': get_random_id(),
		  'keyboard': keyboard.get_keyboard()
		 })

	def menu(self, event_reserved, keyboard):  # отправка клавиатуры меню
		vk.method(
		 'messages.send', {
		  'peer_id': event_reserved.user_id,
		  'message': 'Главное меню',
		  'random_id': get_random_id(),
		  'keyboard': keyboard.get_keyboard()
		 })

	def go_to_menu(
	  self, event_reserved, keyboard
	):  # "заглушка" для ещё нереализованных функций, отправляющая в меню
		vk.method(
		 'messages.send', {
		  'peer_id': event_reserved.user_id,
		  'message': 'В ближайшем будущем!',
		  'random_id': get_random_id(),
		  'keyboard': keyboard.get_keyboard()
		 })
		pic = randint(30, 34)
		s = "photo-217311909_4572390" + str(pic)
		vk.method(
		 "messages.send", {
		  "peer_id": event_reserved.user_id,
		  "message": "",
		  "attachment": s,
		  "random_id": 0
		 })

	def greetings(self, event_reserved):  # приветствие нового юзера
		vk.method(
		 'messages.send', {
		  'peer_id': event_reserved.user_id,
		  'message':
		  "Привет! Теперь ты заложник нашего бота и больше никогда не сможешь выбраться отсюда. Ты будешь учиться до конца своих дней. Удачиииии",
		  "random_id": get_random_id()
		 })

	def send_new_kb(
	  self, mass, user_id,
	  message):  # создание и отправка клавиатуры со списками человека
		keyboard_send_new_kb = VkKeyboard(one_time=True)
		for i in mass:
			print('add button', str(i))
			keyboard_send_new_kb.add_button(str(i), color=VkKeyboardColor.PRIMARY)
		#keyboard_send_new_kb.add_button (str (i), color=VkKeyboardColor.PRIMARY)
		vk.method(
		 'messages.send', {
		  'peer_id': user_id,
		  'message': message,
		  'random_id': get_random_id(),
		  'keyboard': keyboard_send_new_kb.get_keyboard()
		 })

	def unknown_word(self, event_reserved):  # реакции на незнакомые слова
		wrong_answers = [
		 "Ха-ха, смешная шутка!",
		 "Признаться честно я вообще не понял что ты хочешь нам сказать, но послушать было очень интересно",
		 "Чё?",
		 "Я вообще ничего не понял",
		 "Ты точно в порядке? Ты чё пишешь-то?",
		 "Не ну тут мои полномочия это... всё!",
		 "И как мне это понимать...",
		 "Сам разбирайся с тем, что ты написал, понял?!",
		 "И чё мне с этим делать?",
		]

		wrong_answer_request = wrong_answers[randint(0, len(wrong_answers) - 1)]

		vk.method(
		 'messages.send', {
		  'peer_id': event_reserved.user_id,
		  'message': wrong_answer_request,
		  "random_id": get_random_id()
		 })
