import sqlite3
from random import randint

dict0 = dict()


def add_list_vk(list_name, list_value, user_id):  # add new list
	cursor.execute('INSERT INTO LISTS (list_name, list_value) VALUES (?, ?)',
	               (list_name, list_value))
	conn.commit()

	cursor.execute('''SELECT id
                  FROM ID 
                  WHERE user_id = ''' + str(user_id) + " AND tg = " + '0')
	conn.commit()
	us_id = int(cursor.fetchone()[0])
	print(us_id)

	cursor.execute(
	 "SELECT list_id FROM LISTS WHERE list_value = '{}'".format(list_value))
	conn.commit()
	li_id = cursor.fetchone()

	cursor.execute('''SELECT users_lists
                  FROM ID
                  WHERE id = ''' + str(us_id))
	conn.commit()
	li_ids = cursor.fetchone()
	print(li_id)
	if li_ids[0] != None:
		res = li_ids[0] + ' ' + str(li_id[0])
	else:
		res = str(li_id[0])
	print(res)
	cursor.execute("UPDATE ID SET users_lists = '{0}'".format(res) +
	               'WHERE id = ' + str(us_id))
	conn.commit()


def registr_vk(user_id: int, user_name: str, user_surname: str,
               username: str):  # register new user
	try:
		cursor.execute(
		 'INSERT INTO ID (tg, user_id, user_name, user_surname, username) VALUES(?, ?, ?, ?, ?)',
		 (0, user_id, user_name, user_surname, username))
		conn.commit()
	except:
		pass


def get_id(user_id: str):
	cursor.execute('''SELECT id FROM ID WHERE user_id = ''' + str(user_id) +
	               " AND tg = " + '0')
	conn.commit()
	return int(cursor.fetchone()[0])


def select_list(list_name: str, user_id: str):
	cursor.execute(
	 'SELECT id FROM ID WHERE user_id = {} AND tg = 0'.format(user_id))
	conn.commit()
	us_id = int(cursor.fetchone()[0])
	cursor.execute(
	 "SELECT list_value FROM LISTS WHERE list_name = '{0}' AND list_id IN (SELECT users_lists FROM ID WHERE user_id = {1} AND tg = 0)"
	 .format(list_name, user_id))
	conn.commit()
	res = cursor.fetchone()[0]
	# dict0 = {id: [w1, f1], [w2, f2]}
	list1 = []
	print(res.split('\n'))
	for i in res.split('\n'):
		list1.append(tuple(map(lambda x: x.strip(), i.split('='))))
	dict0[us_id] = list1
	print(dict0)
	return res


def delete(list_name: str, user_id: str):
	cursor.execute('''SELECT id FROM ID WHERE user_id = ''' + str(user_id) +
	               " AND tg = " + '0')
	conn.commit()
	us_id = int(cursor.fetchone()[0])
	cursor.execute(
	 'SELECT users_lists FROM ID WHERE user_id = {} AND tg = 0'.format(user_id))
	conn.commit()
	lists = cursor.fetchone()[0]
	lists = ', '.join(lists.split())
	cursor.execute(
	 "SELECT list_id FROM LISTS WHERE list_name = '{0}' AND list_id IN ({1})".
	 format(list_name, lists))
	conn.commit()
	res = cursor.fetchone()[0]
	res1 = lists.replace(str(res) + ', ', '')
	cursor.execute("UPDATE ID SET users_lists = '{0}' WHERE id = {1}".format(
	 res1, us_id))
	conn.commit()


def import_list(list_name: str, author_id: str, user_id: str):
	"""cursor.execute('''SELECT id FROM ID WHERE user_id = ''' + str(author_id))
  conn.commit()
  ath_id = int(cursor.fetchone()[0])"""
	cursor.execute('''SELECT id FROM ID WHERE user_id = ''' + str(user_id))
	conn.commit()
	us_id = int(cursor.fetchone()[0])
	cursor.execute('''SELECT users_lists
                  FROM ID
                  WHERE id = ''' + str(author_id))
	conn.commit()
	li_ids_ath = cursor.fetchone()[0]
	cursor.execute('''SELECT users_lists
                  FROM ID
                  WHERE id = ''' + str(us_id))
	conn.commit()
	li_ids_us = cursor.fetchone()[0]
	cursor.execute("""SELECT list_id FROM LISTS WHERE list_name = '{0}'
    AND list_id IN ({1})""".format(list_name, li_ids_ath))
	conn.commit()
	li_id = cursor.fetchone()[0]
	cursor.execute("UPDATE ID SET users_lists = '{0}'".format(li_ids_us + ' ' +
	                                                          str(li_id)) +
	               'WHERE id = ' + str(us_id))
	conn.commit()


def get_lists(user_id: int):  # list of lists of user
	cursor.execute(
	 'SELECT users_lists FROM ID WHERE user_id = {} AND tg = 0'.format(user_id))
	conn.commit()
	lists = cursor.fetchone()[0].split()
	res = []
	for list1 in lists:
		cursor.execute(
		 'SELECT list_name FROM LISTS WHERE list_id = {}'.format(list1))
		conn.commit()
		a = cursor.fetchone()
		res.append(a[0])
	return res


def edit_list(list_name: str, list_value: str, user_id):
	cursor.execute('''SELECT id FROM ID WHERE user_id = ''' + str(user_id) +
	               " AND tg = " + '0')
	conn.commit()
	us_id = int(cursor.fetchone()[0])
	cursor.execute('''SELECT users_lists
                  FROM ID
                  WHERE id = ''' + str(us_id))
	conn.commit()
	li_ids = cursor.fetchone()[0]
	li_ids = ', '.join(li_ids.split())
	print(li_ids)
	cursor.execute("""SELECT list_id FROM LISTS WHERE list_name = '{0}'
  AND list_id IN ({1})""".format(list_name, li_ids))
	conn.commit()
	li_id = cursor.fetchone()[0]
	print(li_id, 'efsefsef', list_value)
	cursor.execute(
	 "UPDATE LISTS SET list_value = '{0}' WHERE list_id = {1}".format(
	  list_value, li_id))
	conn.commit()


def create():  # create table
	cursor.execute("""CREATE TABLE IF NOT EXISTS ID (
    id           INTEGER PRIMARY KEY AUTOINCREMENT
                         UNIQUE
                         NOT NULL,
    tg           INTEGER NOT NULL,
    user_id      INTEGER NOT NULL
                         UNIQUE,
    user_name    TEXT    NOT NULL,
    user_surname TEXT,
    username     TEXT,
    users_lists  TEXT
);
  """)
	conn.commit()
	cursor.execute("""CREATE TABLE IF NOT EXISTS LISTS (
    list_id    INTEGER PRIMARY KEY AUTOINCREMENT
                       UNIQUE
                       NOT NULL,
    list_name  TEXT    NOT NULL,
    list_value TEXT    NOT NULL);
  """)
	conn.commit()


conn = sqlite3.connect('database.db', check_same_thread=True)
cursor = conn.cursor()
