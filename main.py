import funcs
import keyboard_set
import vk_settings
import database_funcs as database
from random import randint

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

		elif request == 'Начать' or request == '/start' or request == 'start' or request == 'Start' or request == 'начать':
			Main.greetings(event)
			database.registr_vk(user_id=event.user_id,
			                    user_name=Main.get_name(event.user_id)[0],
			                    user_surname=Main.get_name(event.user_id)[1],
			                    username=1)
			print("Новый юзер зарегистрирован! ", int(event.user_id),
			      Main.get_name(event.user_id)[0],
			      Main.get_name(event.user_id)[1])
			Main.menu(event, kb.keyboard)

		elif request == "Работа со списками":
			Main.msg_kb(event.user_id, 'Выберите режим', kb.keyboard_add)

			for event_mode in longpoll.listen():
				if event_mode.type == VkEventType.MESSAGE_NEW and event_mode.to_me:
					request_mode = event_mode.text

					if request_mode == "Создать новый список":
						Main.msg_kb(event_mode.user_id, "Какой режим выбираете?",
						            kb.keyboard_mode)

						for event_create_new in longpoll.listen():
							if event_create_new.type == VkEventType.MESSAGE_NEW and event_create_new.to_me:
								request_create_new = event_create_new.text

								if request_create_new == "Режим автопроверки":
									Main.msg_kb(
									 event_create_new.user_id,
									 'Что вы хотите учить? Текстовые определения или билеты по фотографиям?',
									 kb.keyboard_selfcheck)

									for event_selfcheck in longpoll.listen():
										if event_selfcheck.type == VkEventType.MESSAGE_NEW and event_selfcheck.to_me:
											request_selfcheck = event_selfcheck.text

											if request_selfcheck == "Текстовые определения":
												Main.write_msg(event_selfcheck.user_id,
												               'Как будет называться Ваш список?')
												print("ожидание названия")

												for event_list_name in longpoll.listen():
													if event_list_name.type == VkEventType.MESSAGE_NEW and event_list_name.to_me:
														request_list_name = event_list_name.text

														list_name = request_list_name
														print("название записано")
														Main.write_msg(
														 event_list_name.user_id,
														 'Теперь пришлите, пожалуйста, определения, которые Вы хотите выучить в формате:\nтермин1=определение1 \nтермин2=определение2'
														)

														for event_text_termins in longpoll.listen():
															if event_text_termins.type == VkEventType.MESSAGE_NEW and event_text_termins.to_me:
																print("определение записано")
																request_text_termins = event_text_termins.text

																text_termins = request_text_termins
																print(list_name, text_termins, event_text_termins.user_id)
																database.add_list_vk(list_name, text_termins,
																                     event_text_termins.user_id)
																Main.write_msg(
																 event_text_termins.user_id,
																 "Отлично! Мы запомнили ваш список. Простите, что вам приходится пользоваться нашим ботом"
																)
																Main.msg_kb(event_text_termins.user_id, "Продолжим?)",
																            kb.keyboard_continue)
																print("записано в базу")
																break
															print("ожидание сообщений?")
														break

											elif request_selfcheck == "Билеты по фотографиям":
												Main.go_to_menu(event_selfcheck, kb.keyboard)
												break

											elif request_selfcheck == "В меню":
												Main.menu(event_selfcheck, kb.keyboard)
												break

											else:
												Main.msg_kb(
												 event_create_new.user_id,
												 'Что вы хотите учить? Текстовые определения или билеты по фотографиям?',
												 kb.keyboard_selfcheck)
									break

								elif request_create_new == "Режим самопроверки":
									Main.go_to_menu(event_create_new, kb.keyboard)

								elif request_mode == "В меню":
									Main.menu(event, kb.keyboard)
									break

								else:
									Main.msg_kb(
									 event_mode.user_id,
									 'Какой список Вы хотите учить? С автоматической проверкой или нет?',
									 kb.keyboard_mode)
						break

					elif request_mode == "Редактировать мои списки":
						# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите отредактировать?', keyboard_ с названиями списков, созданных человеком)
						Main.msg_kb(event_mode.user_id, "Что конкретно Вы хотите?",
						            kb.keyboard_edit)

						for event_edit in longpoll.listen():
							if event_edit.type == VkEventType.MESSAGE_NEW and event_edit.to_me:
								request_edit = event_edit.text

								if request_edit == "Редактировать список":
									# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите отредактировать?', keyboard_ с названиями списков, созданных человеком)
									print(str(database.get_lists(event_edit.user_id)[0]))
									Main.send_new_kb(database.get_lists(event_edit.user_id),
									                 event_edit.user_id,
									                 'Какой из своих списков вы хотите отредактировать?')

									for event_edit_name in longpoll.listen():
										if event_edit_name.type == VkEventType.MESSAGE_NEW and event_edit_name.to_me:
											request_edit_name = event_edit_name.text

											if request_edit_name in database.get_lists(event_edit_name.user_id):
												Main.write_msg(event_edit_name.user_id,
												               "Такой список у вас сейчас")
												# кидаем список, ждём ответ
												Main.write_msg(
												 event_edit_name.user_id,
												 database.select_list(request_edit_name, event_edit_name.user_id))
												Main.write_msg(event_edit_name.user_id,
												               "Измените его и пришлите мне изменённый список")
												for event_edit_list in longpoll.listen():
													if event_edit_list.type == VkEventType.MESSAGE_NEW and event_edit_list.to_me:
														request_edit_list = event_edit_list.text

														Main.write_msg(event_edit_list.user_id,
														               "Сейчас попробую изменить этот список!")
														try:
															database.edit_list(request_edit_name, request_edit_list,
															                   event_edit_name.user_id)
															Main.write_msg(event_edit_list.user_id, "Отлично! Получилось!")
														except:
															Main.write_msg(event_edit_list.user_id,
															               "Странно... не получается что-то")
														break

												Main.msg_kb(event_edit_name.user_id, "Продолжить?",
												            kb.keyboard_continue)

											else:
												Main.write_msg(event_edit_name.user_id,
												               "Извините, такого списка у вас нет")
												Main.msg_kb(event_edit_name.user_id, "Продолжить?",
												            kb.keyboard_continue)
											break
									'''if request_edit == "Редактировать список":
									#Main.send_new_kb ()
									Main.go_to_menu (event_edit, kb.keyboard)
									break'''

								elif request_edit == "Удалить список":
									# Main.msg_kb (event.user_id,'Какой из своих списков вы хотите удалить?', keyboard_ с названиями списков, созданных человеком)
									Main.send_new_kb(database.get_lists(event_edit.user_id),
									                 event_edit.user_id,
									                 'Какой из своих списков вы хотите удалить?')

									for event_delete_name in longpoll.listen():
										if event_delete_name.type == VkEventType.MESSAGE_NEW and event_delete_name.to_me:
											request_delete_name = event_delete_name.text

											if request_delete_name in database.get_lists(
											  event_delete_name.user_id):
												Main.write_msg(event_delete_name.user_id,
												               "Такой список у вас сейчас")
												# кидаем список, ждём ответ
												Main.write_msg(
												 event_delete_name.user_id,
												 database.select_list(request_delete_name,
												                      event_delete_name.user_id))
												Main.msg_kb(event_delete_name.user_id,
												            "Вы уверены, что хотите его удалить?",
												            kb.keyboard_question)

												for event_delete_confirm in longpoll.listen():
													if event_delete_confirm.type == VkEventType.MESSAGE_NEW and event_delete_confirm.to_me:
														request_delete_confirm = event_delete_confirm.text

														if request_delete_confirm == "Да":
															try:
																database.delete(request_delete_name,
																                event_delete_confirm.user_id)
																Main.write_msg(event_delete_confirm.user_id,
																               "Отлично! Получилось!")
															except:
																Main.write_msg(event_delete_confirm.user_id,
																               "Странно... не получается что-то")

															Main.msg_kb(event_delete_confirm.user_id, "Продолжить?",
															            kb.keyboard_continue)
														else:
															Main.write_msg(event_delete_confirm.user_id, "И слава богу!")
															Main.msg_kb(event_delete_confirm.user_id, "Продолжить?",
															            kb.keyboard_continue)
														break
											break
									#Main.go_to_menu (event_edit, kb.keyboard)
									#break

								elif request_edit == "В меню":
									print("Хочу в меню")
									Main.menu(event_edit, kb.keyboard)
									break

								else:
									Main.msg_kb(
									 event_edit.user_id,
									 'Что вы хотите делать? Редактировать список, удалить его или вернуться в меню?',
									 kb.keyboard_edit)

					elif request_mode == "Поделиться списком":
						# Main.msg_kb (event.user_id,'Каким из своих списков вы хотите поделиться?', keyboard_ с названиями списков, созданных человеком)
						# достаём из БД номер этого списка и присылаем челику
						# КЛАВА СО СПИСКАМИ СОЗДАННЫХ ЧЕЛОВЕКОМ
						#Main.write_msg (event_mode.user_id, database.select_list (request_mode, event_mode.user_id))
						Main.send_new_kb(database.get_lists(event_mode.user_id),
						                 event_mode.user_id,
						                 'Каким из своих списков вы хотите поделиться?')

						for event_share_name in longpoll.listen():
							if event_share_name.type == VkEventType.MESSAGE_NEW and event_share_name.to_me:
								request_share_name = event_share_name.text

								if request_share_name in database.get_lists(event_share_name.user_id):
									Main.write_msg(
									 event_mode.user_id,
									 'Чтобы другой человек смог найти ваши списки, передайте ему, пожалуйста, этот номер: '
									 + str(database.get_id(event_mode.user_id)) +
									 ' и название выбранного списка: ' + request_share_name)
								Main.menu(event_mode, kb.keyboard)
								break

					elif request_mode == "Импортировать список":
						Main.write_msg(
						 event_mode.user_id,
						 "Введите, пожалуйста, переданные вам владельцем списка значения в формате:\nчисло=название списка"
						)

						for event_recieved_data in longpoll.listen():
							if event_recieved_data.type == VkEventType.MESSAGE_NEW and event_recieved_data.to_me:
								request_recieved_data = event_recieved_data.text
								print(request_recieved_data)
								for i in range(len(request_recieved_data)):
									if request_recieved_data[i] == "=":
										recieved_id = request_recieved_data[:i]
										recieved_list_name = request_recieved_data[i + 1:]
								break
						print(recieved_id, recieved_list_name)
						Main.write_msg(event_recieved_data.user_id,
						               "Сейчас попробую найти этот список!")
						try:
							database.import_list(recieved_list_name, recieved_id,
							                     event_recieved_data.user_id)
							Main.write_msg(event_recieved_data.user_id, "Отлично! Получилось!")
						except:
							Main.write_msg(event_recieved_data.user_id,
							               "Странно... не получается что-то")

					elif request_mode == "В меню":
						Main.menu(event_mode, kb.keyboard)
						break

					else:
						Main.msg_kb(event_mode.user_id, "Что Вы выбираете?", kb.keyboard_add)
					break
		elif request == "Тренировка":
			Main.msg_kb(event.user_id, 'Что выбираете?', kb.keyboard_train)

			for event_train_start in longpoll.listen():
				if event_train_start.type == VkEventType.MESSAGE_NEW and event_train_start.to_me:
					request_train_start = event_train_start.text

					if request_train_start == 'Выбор режима':
						Main.msg_kb(event_train_start.user_id, "Какой режим выбираете?",
						            kb.keyboard_choose_mode)

						for event_train_choose_mode in longpoll.listen():
							if event_train_choose_mode.type == VkEventType.MESSAGE_NEW and event_train_choose_mode.to_me:
								request_train_choose_mode = event_train_choose_mode.text

								if request_train_choose_mode == 'Режим автопроверки':
									#Main.write_msg (event_train_choose_mode.user_id, (database.get_lists))
									Main.write_msg(
									 event_train_choose_mode.user_id,
									 "Я буду присылать лицевую сторону карточки. Ваша задача написать мне что находится на её обратной части, а я уже проверю :)"
									)
									Main.write_msg(
									 event_train_choose_mode.user_id,
									 "Если всё будет плохо, то Вы всегда можете написать 'Стоп'")
									Main.send_new_kb(database.get_lists(event_train_choose_mode.user_id),
									                 event_train_choose_mode.user_id,
									                 'Какой из своих списков вы выбираете?')
									#Main.go_to_menu(event_train_start, kb.keyboard)
									#break
									for event_choose_train_list in longpoll.listen():
										if event_choose_train_list.type == VkEventType.MESSAGE_NEW and event_choose_train_list.to_me:
											request_choose_train_list = event_choose_train_list.text
											if request_choose_train_list in database.get_lists(
											  event_choose_train_list.user_id):
												# Тренировка ааааааааа
												str_cards = database.select_list(request_choose_train_list,
												                                 event_choose_train_list.user_id)
												list_cards = str_cards.splitlines()
												mass_cards = []

												for i in list_cards:
													for j in range(len(i)):
														if i[j] == "=":  # split
															mass_cards.append(i[:j])
															mass_cards.append(i[(j + 1):])
												print(mass_cards)

												word = 'example'
												while len(mass_cards) != 0:
													print(word == "Стоп")
													if word == "Стоп":
														break
													Main.write_msg(event_choose_train_list.user_id,
													               "Какая пара у этого слова?")

													number = randint(0, len(mass_cards) - 1)  # генерация чётных
													while number % 2 != 0:
														number = randint(0, len(mass_cards) - 1)
													Main.write_msg(event_choose_train_list.user_id,
													               mass_cards[number])

													for event_answer in longpoll.listen():
														if event_answer.type == VkEventType.MESSAGE_NEW and event_answer.to_me:
															request_answer = event_answer.text
															word = request_answer

															print(word)
															print(mass_cards[number + 1])
															if word == mass_cards[number + 1]:
																Main.write_msg(event_choose_train_list.user_id, "Ты умничка")
																mass_cards.pop(number + 1)
																mass_cards.pop(number)
																print(mass_cards)
																print('number = ', number)
															else:
																#answer =
																Main.write_msg(
																 event_choose_train_list.user_id,
																 "Неправильно! Правильным словом было: " +
																 mass_cards[number + 1])
																#Main.write_msg (event_choose_train_list.user_id, '\n')
															break

												if "Стоп" not in word:
													print('Стоп-слово: ', word)
													Main.write_msg(
													 event_choose_train_list.user_id,
													 "Ты умничка и выполнил план по повторению на сегодняшний день, УРА!"
													)
													Main.msg_kb(event_choose_train_list.user_id,
													            "Какой режим выбираете?", kb.keyboard_choose_mode)
												else:
													Main.write_msg(
													 event_choose_train_list.user_id,
													 "Ты меня расстроил... Старайся так не делать в следующий раз")
													Main.msg_kb(event_choose_train_list.user_id,
													            "Какой режим выбираете?", kb.keyboard_choose_mode)
												break
											break

								elif request_train_choose_mode == 'Режим самопроверки':
									Main.go_to_menu(event_train_start, kb.keyboard)
									break

								elif request_train_choose_mode == 'В меню':
									Main.menu(event_train_choose_mode, kb.keyboard)

								else:
									Main.msg_kb(event_train_choose_mode.user_id, "Какой режим выбираете?",
									            kb.keyboard_choose_mode)

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
			Main.unknown_word(event)
			Main.menu(event, kb.keyboard)
