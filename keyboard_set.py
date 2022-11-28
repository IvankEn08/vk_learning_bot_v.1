# заранее заготовленные клавиатуры для отправки

from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class kb:

	keyboard = VkKeyboard(one_time=True)
	keyboard.add_button('Работа со списками', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Тренировка', color=VkKeyboardColor.PRIMARY)

	keyboard_add = VkKeyboard(one_time=True)
	keyboard_add.add_button('Создать новый список',
	                        color=VkKeyboardColor.POSITIVE)
	keyboard_add.add_line()
	keyboard_add.add_button('Импортировать список', color=VkKeyboardColor.PRIMARY)
	keyboard_add.add_button('Поделиться списком', color=VkKeyboardColor.PRIMARY)
	keyboard_add.add_line()
	keyboard_add.add_button('Редактировать мои списки',
	                        color=VkKeyboardColor.PRIMARY)
	keyboard_add.add_line()
	keyboard_add.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

	keyboard_train = VkKeyboard(one_time=True)
	keyboard_train.add_button('Настроить напоминания',
	                          color=VkKeyboardColor.PRIMARY)
	keyboard_train.add_button('Выбор режима', color=VkKeyboardColor.PRIMARY)
	keyboard_train.add_line()
	keyboard_train.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

	keyboard_selfcheck = VkKeyboard(one_time=True)
	keyboard_selfcheck.add_button('Текстовые определения',
	                              color=VkKeyboardColor.PRIMARY)
	keyboard_selfcheck.add_line()
	keyboard_selfcheck.add_button('Билеты по фотографиям',
	                              color=VkKeyboardColor.PRIMARY)
	keyboard_selfcheck.add_line()
	keyboard_selfcheck.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

	keyboard_mode = VkKeyboard(one_time=True)
	keyboard_mode.add_button('Режим самопроверки', color=VkKeyboardColor.PRIMARY)
	keyboard_mode.add_button('Режим автопроверки', color=VkKeyboardColor.PRIMARY)
	keyboard_mode.add_line()
	keyboard_mode.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

	keyboard_choose_mode = VkKeyboard(one_time=True)
	keyboard_choose_mode.add_button('Режим автопроверки',
	                                color=VkKeyboardColor.PRIMARY)
	keyboard_choose_mode.add_button('Режим самопроверки',
	                                color=VkKeyboardColor.PRIMARY)
	keyboard_choose_mode.add_line()
	keyboard_choose_mode.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

	keyboard_continue = VkKeyboard(one_time=True)
	keyboard_continue.add_button('Продолжить', color=VkKeyboardColor.PRIMARY)

	keyboard_question = VkKeyboard(one_time=True)
	keyboard_question.add_button('Да', color=VkKeyboardColor.NEGATIVE)
	keyboard_question.add_button('Нет', color=VkKeyboardColor.POSITIVE)

	keyboard_edit = VkKeyboard(one_time=True)
	keyboard_edit.add_button('Редактировать список',
	                         color=VkKeyboardColor.PRIMARY)
	keyboard_edit.add_button('Удалить список', color=VkKeyboardColor.PRIMARY)
	keyboard_edit.add_line()
	keyboard_edit.add_button('В меню', color=VkKeyboardColor.NEGATIVE)
