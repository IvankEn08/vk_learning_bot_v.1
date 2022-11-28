# здесь описан сам алгоритм игры в карточки, используемый в тренировке

from random import randint

s = 'Слово1=Слово2\nСлово3=Слово4\nСлово5=Слово6' # пример строки
mass = s.splitlines ()

mass_2 = []
mass_3 = []

for i in mass: # делаем из строки s массив вида ['Слово1', 'Слово2' и т.д.]
    for j in range (len (i)):
        if i [j] == "=":
            mass_2.append (i [:j])
            mass_2.append (i [j + 1:])
mass_3 = mass_2

while len (mass_3) != 0:
    print ("Как переводится это слово?")
	
    number = randint (0, len (mass_3) - 1) # генерация чётных чисел
    while number % 2 != 0:
        number = randint (0, len (mass_3) - 1)
			
    print (mass_3 [number])
    word = str (input ())
	
    if word == mass_3 [number + 1]: # чётные - лицевые части карточек, нечётные - обратные
        print ("Ты умничка")
        mass_3.pop(number + 1)
        mass_3.pop(number)
    else:
        print ("Неправильно! Правильным переводом было: ", mass_2 [number + 1])
    print ('\n')

print ("Ты умничка и выполнил план по повторению на сегодняшний день, УРА!")