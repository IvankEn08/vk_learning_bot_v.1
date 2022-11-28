# старая резервная версия бота для быстрой откатки отдельных функций

import funcs
import keyboard_set
import vk_settings
import database

database.create()

Main = funcs.Main()
kb = keyboard_set.kb()

vk = vk_settings.vk
vkapi = vk_settings.vkapi
longpoll = vk_settings.longpoll
upload = vk_settings.upload
VkEventType = vk_settings.VkEventType

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		request = event.text

		if request == 'В меню':
			Main.menu(event, kb.keyboard)

		elif request == 'Начать' or request == '/start':
			Main.greetings (event)
			database.registr_vk (user_id = event.user_id, user_name = Main.get_name (event.user_id) [0], user_surname=Main.get_name (event.user_id) [1], username = 1)
			print ("Новый юзер зарегистрирован! ", int (event.user_id), Main.get_name (event.user_id) [0], Main.get_name (event.user_id) [1])
			Main.menu (event, kb.keyboard)

		elif request == "Работа со списками":
			Main.msg_kb(event.user_id, 'Выберите режим', kb.keyboard_add)
	
		if request == "Создать новый список":
			Main.msg_kb (event.user_id, "Какой режим выбираете?", kb.keyboard_mode)

		if request == "Режим самопроверки":
			Main.msg_kb (event.user_id, 'Что вы хотите учить? Текстовые определения или билеты по фотографиям?', kb.keyboard_selfcheck)

		if request == "Текстовые определения":
			Main.write_msg(event.user_id, 'Как будет называться Ваш список?')
												
			for event_list_name in longpoll.listen():
				if event_list_name.type == VkEventType.MESSAGE_NEW and event_list_name.to_me:
					request_list_name = event_list_name.text	
					list_name = request_list_name
					Main.write_msg(event_list_name.user_id, 'Теперь пришлите, пожалуйста, определения, которые Вы хотите выучить в формате:\nтермин1=определение1 \nтермин2=определение2')
														
					for event_text_termins in longpoll.listen():
						if event_text_termins.type == VkEventType.MESSAGE_NEW and event_text_termins.to_me:
							request_text_termins = event_text_termins.text
																
							text_termins = request_text_termins
							print (list_name, text_termins, event_text_termins.user_id)
							database.add_list_vk (list_name, text_termins, event_text_termins.user_id)
							Main.write_msg (event_text_termins.user_id, "Отлично! Мы запомнили ваш список. Простите, что вам приходится пользоваться нашим ботом")
							Main.msg_kb (event_text_termins.user_id, "Продолжим?)", kb.keyboard_continue)
							print ("записано в базу")
							print ("ожидание сообщений?")

		elif request == "Билеты по фотографиям":
			Main.go_to_menu (event, kb.keyboard)

		elif request == "Режим автопроверки":
			Main.write_msg(event.user_id, 'Как будет называться Ваш список?')
												
			for event_auto_list_name in longpoll.listen():
				if event_auto_list_name.type == VkEventType.MESSAGE_NEW and event_auto_list_name.to_me:
					request_auto_list_name = event_auto_list_name.text
														
					auto_list_name = request_auto_list_name
					Main.write_msg(event_auto_list_name.user_id, 'Пришлите, пожалуйста, слова, которые вы хотите выучить в формате: \nслово1 = слово2 \nслово3 = слово4')
														
					for event_auto_text_termins in longpoll.listen():
						if event_auto_text_termins.type == VkEventType.MESSAGE_NEW and event_auto_text_termins.to_me:
							request_auto_text_termins = event_auto_text_termins.text
																
							auto_text_termins = request_auto_text_termins
							database.add_list_vk (auto_list_name, auto_text_termins, event_auto_text_termins.user_id)
							Main.write_msg (event_auto_text_termins.user_id, "Отлично! Мы запомнили ваш список. Простите, что вам приходится пользоваться нашим ботом")
							Main.msg_kb (event_auto_text_termins.user_id, "Продолжим?)", kb.keyboard_continue)
							break
					break

		elif request == "Редактировать мои списки":
						# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите отредактировать?', keyboard_ с названиями списков, созданных человеком)
			Main.msg_kb (event.user_id, "Что конкретно Вы хотите?", kb.keyboard_edit)
			
			for event_edit in longpoll.listen():
				if event_edit.type == VkEventType.MESSAGE_NEW and event_edit.to_me:
					request_edit = event_edit.text

					if request_edit == "Редактировать список":
									# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите отредактировать?', keyboard_ с названиями списков, созданных человеком)
									Main.go_to_menu (event_edit, kb.keyboard)
									break
									
					elif request_edit == "Удалить список":
						# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите удалить?', keyboard_ с названиями списков, созданных человеком)
						Main.go_to_menu (event_edit, kb.keyboard)
						break


		elif request_mode == "Поделиться списком":
			# Main.msg_kb (event.user_id,'Каким из своих списков вы хотите поделиться?', keyboard_ с названиями списков, созданных человеком)
			# достаём из БД номер этого списка и присылаем челику
			# КЛАВА СО СПИСКАМИ СОЗДАННЫХ ЧЕЛОВЕКОМ
			break

					elif request_mode == "В меню":
						Main.menu(event_mode, kb.keyboard)
						break

					else:
						Main.unknown_word (event)
						Main.msg_kb(event_mode.user_id, "Что Вы выбираете?", kb.keyboard_mode)
					break
		elif request == "Тренировка":
			Main.msg_kb(event.user_id, 'Что выбираете?', kb.keyboard_train)
			
			for event_train_start in longpoll.listen():
				if event_train_start.type == VkEventType.MESSAGE_NEW and event_train_start.to_me:
					request_train_start = event_train_start.text

					if request_train_start == 'Выбор режима':
						Main.msg_kb (event_train_start.user_id, "Какой режим выбираете?", kb.keyboard_choose_mode)						
						
						for event_train_choose_mode in longpoll.listen():
							if event_train_choose_mode.type == VkEventType.MESSAGE_NEW and event_train_choose_mode.to_me:
								request_train_choose_mode = event_train_choose_mode.text

								if request_train_choose_mode == 'Режим автопроверки':
									Main.go_to_menu(event_train_start, kb.keyboard)
									break

								elif request_train_choose_mode == 'Режим самопроверки':
									Main.go_to_menu(event_train_start, kb.keyboard)
									break 

								elif request_train_choose_mode == 'В меню':
									Main.menu (event_train_choose_mode, kb.keyboard)

								else:
									Main.msg_kb(event_train_choose_mode.user_id, "Какой режим выбираете?", kb.keyboard_choose_mode)
				
						break

					elif request_train_start == "Настроить напоминания":
						# сюда надо зафигачить таймер
						Main.go_to_menu(event_train_start, kb.keyboard)
						break

					elif request_train_start == "В меню":
						Main.menu(event_train_start, kb.keyboard)
						break

					else:
						Main.msg_kb(event_train_start.user_id, "Что выбираете?",
						            kb.keyboard_train)

		else:
			#Main.unknown_word(event)
			print(request)
			Main.unknown_word (event)
			Main.menu (event, kb.keyboard)