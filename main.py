import telebot
import schedule
import time
import datetime

rozklad = [{
	'1':[{
			0: 'Понедельник',
			1: "-----",
			2: 'Мат. Экономика | Лекция\n    405 лк',
			3: ['Дискретка | Лекция\n    104а рк', 'Дискретка | Лекция\n    104а рк'],
			4: 'Физ-ра',
		}],
	'2':[{
			0: 'Вторник',
			1: "Теор. Вер. | Лекция\n    413 лк",
			2: 'Численные методы | Лекция\n    307 гк',
			3: ['Теор. Вер. | Практика\n    402 лк', 'Теор. Вер. | Практика\n    402 лк'],
			4: '-----'
		}],
	'3':[{
			0: 'Среда',
			1: '-----',
			2: '-----',
			3: ['Численные методы | Практика\n    202б рк', 'Мат. Экономика | Практика\n    411 лк'],
			4: 'Физ-ра'
		}],
	'4':[{
			0: 'Четверг',
			1: "Современные технологии прогр. | Практика\n    304 лк",
			2: 'Современные технологии прогр. | Практика\n    304 лк',
			3: ['Дифф. уравнения | Лекция\n    413 лк', 'Дифф. уравнения | Лекция\n    413 лк'],
			4: 'Дифф. уравнения | Практика\n    404 лк'
		}],
	'5':[{
			0: 'Пятница',
			1: "-----",
			2: 'WEB-прогр. | Практика\n    304 лк',
			3: ['Дискретка | Практика\n    202а рк', 'WEB-прогр. | Практика\n    304 лк'],
			4: '-----'
		}]
	}]


bot = telebot.TeleBot('662931082:AAEwU55ZVpylddfg75lAnSIs1CQ-SKWfZjA')




# Счет недели. Если она чётная, то это чиситель(True), а если нечётная, то знаменатель(False)
def numerator():
    if int(datetime.date.today().isoweekday()) < 5:
        if int(datetime.date.today().isocalendar()[1]) % 2 == 0:
            return 1
        return 0
    if int(datetime.date.today().isocalendar()[1]) % 2 == 0:
        return 0
    return 1



def main_message():
    if datetime.date.today().isoweekday() >= 5:
        b = 1
    else:
        b = datetime.date.today().isoweekday() + 1
    a = rozklad[0][str(b)]
    tomorrowdate = datetime.date.today() + datetime.timedelta(days = 1)
    if numerator() == 1:
        main_message = a[0][0] + '  ' + tomorrowdate.strftime("%d.%m.%Y") +'\n\nЧислитель\n\n1. ' + a[0][1] + '\n2. ' + a[0][2] + '\n3. ' + a[0][3][0] + '\n4. ' + a[0][4] 
    elif numerator() == 0:
        main_message =  a[0][0] + '  ' + tomorrowdate.strftime("%d.%m.%Y") +'\n\nЗнаменатель\n\n1. ' + a[0][1] + '\n2. ' + a[0][2] + '\n3. ' + a[0][3][1] + '\n4. ' + a[0][4]
    bot.send_message('-1001322716320', main_message)

schedule.every().day.at("23:55").do(main_message)
while True:
    schedule.run_pending()
bot.polling(none_stop=True, interval = 0)
