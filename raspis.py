import telebot
from telebot import types
import mysql.connector
import datetime
from datetime import date

nowt = date.today()
y = int(nowt.strftime('%Y'))
m = int(nowt.strftime('%m'))
d = int(nowt.strftime('%d'))
# print(nowy,nowm,nowd)
c = datetime.date(y, m, d).isocalendar().week
# cet = 'четная'
# necet = 'нечетная'
# print(c)

conn = mysql.connector.connect(database='service_db', username='root', password='qazwsxedc')
cursor = conn.cursor()

token = "5740428804:AAGZM-PoCfMgProGVyWbK_mR4kMeGIWqiP0"
bot = telebot.TeleBot(token)
command_list = ['/help', '/Расписание', '/KAKAYANEDELA', '/mtuci', '/start', 'На ПН', 'На ВТ', ' На СР', 'На ЧТ',
                'На ПТ', 'На СБ', 'На тек нед', 'На след нед']


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/Расписание", "/KAKAYANEDELA")
    bot.send_message(message.chat.id, 'Привет зайка <3. Хочешь узнать свежую информацию о МТУСИ?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def sart(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/mtuci", "/start")
    bot.send_message(message.chat.id, 'тута полезные сылОЧКИ', reply_markup=keyboard)


@bot.message_handler(commands=['mtuci'])
def start2(message2):
    bot.send_message(message2.chat.id, 'сайт МТУСИ - https://mtuci.ru/')


@bot.message_handler(commands=['Расписание'])
def start(message):
    keyboard2 = types.ReplyKeyboardMarkup()
    keyboard2.row("/start", "На ПН", "На ВТ", "На СР", "На ЧТ", "На ПТ", "На СБ", "На тек нед", "На след нед")
    bot.send_message(message.chat.id, 'Выбери какое нужно', reply_markup=keyboard2)


@bot.message_handler(commands=['KAKAYANEDELA'])
def start2(message):
    if c % 2 == 0:
        bot.send_message(message.chat.id, 'УХАХАХА ОНА ЧЕТНАЯ')
    elif c % 2 != 0:
        bot.send_message(message.chat.id, 'АХАХАХХААХ НЕЧЕТНАЯ')
    else:
        bot.send_message(message.chat.id, 'шо ты буровишь')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "на пн":
        if c % 2 == 0:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.pn")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'ЭХ понедельник(чет):\n{fullr}')
        else:
            bot.send_message(message.chat.id, 'Седня занятий нет, почиль броу.')

    elif message.text.lower() == "на вт":
        if c % 2 == 0:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'(на вторник(да-да это четная неделя)):\n{fullr}')
        else:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik_nechet")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'(нечет вторник):\n{fullr}')

    elif message.text.lower() == "на ср":
        bot.send_message(message.chat.id, 'Мега чил(на чет и нечет)')

    elif message.text.lower() == "на чт":
        if c % 2 == 0:
            bot.send_message(message.chat.id, 'Седня Чилим')
        else:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cetverg_nechet")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'четверг (эх нечет):\n{fullr}')

    elif message.text.lower() == "на пт":
        if c % 2 == 0:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'вау четная пятница:\n{fullr}')
        else:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza_nechet")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'нечетная пятница:\n{fullr}')

    elif message.text.lower() == "на сб":
        if c % 2 == 0:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'суббота УРА(четная):\n{fullr}')
        else:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota_nechet")
            cursor.execute(rasp)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')

            bot.send_message(message.chat.id, f'нечетная суббота:\n{fullr}')

    elif message.text.lower() == "на тек нед":
        if c % 2 == 0:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.pn")
            rasp2 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik")
            rasp5 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza")
            rasp6 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota")
            cursor.execute(rasp)
            fullr += '        ПОНЕДЕЛЬНИК \n'
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        ВТОРНИК \n'
            cursor.execute(rasp2)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        CРЕДА - ЧИЛЛ\n\n        ЧЕТВЕРГ-тоже чилл \n \n'
            fullr += '        ПЯТНИЦА \n'
            cursor.execute(rasp5)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СУББОТА \n'
            cursor.execute(rasp6)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')

            bot.send_message(message.chat.id, f'Текучащя неделя(четная):\n{fullr}')
        else:
            fullr = str()
            rasp2 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik_nechet")
            rasp4 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cetverg_nechet")
            rasp5 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza_nechet")
            rasp6 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota_nechet")
            fullr += '        ПОНЕДЕЛЬНИК \n\n'
            fullr += '        ВТОРНИК \n'
            cursor.execute(rasp2)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СРЕДА - ЧИЛЛ\n\n'
            fullr += '        ЧЕТВЕРГ \n'
            cursor.execute(rasp4)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        ПЯТНИЦА \n'
            cursor.execute(rasp5)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СУББОТА \n'
            cursor.execute(rasp6)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            bot.send_message(message.chat.id, f'Текучащя неделя(не четкая):\n{fullr}')

    elif message.text.lower() == "на след нед":
        if c % 2 == 0:
            fullr = str()
            rasp2 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik_nechet")
            rasp4 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cetverg_nechet")
            rasp5 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza_nechet")
            rasp6 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota_nechet")
            fullr += '        ПОНЕДЕЛЬНИК ЧИЛИМ  \n\n'
            fullr += '        ВТОРНИК \n'
            cursor.execute(rasp2)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СРЕДА - ЧИЛЛ\n\n'
            fullr += '        ЧЕТВЕРГ \n'
            cursor.execute(rasp4)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        ПЯТНИЦА \n'
            cursor.execute(rasp5)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СУББОТА \n'
            cursor.execute(rasp6)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            bot.send_message(message.chat.id, f'След неделя(четная):\n{fullr}')
        else:
            fullr = str()
            rasp = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.pn")
            rasp2 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.wtornik")
            rasp5 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.patniza")
            rasp6 = ("SELECT n_uroka, predmet, n_cabinet, time, prepod FROM raspisanie2.cubota")
            cursor.execute(rasp)
            fullr += '        ПОНЕДЕЛЬНИК \n'
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        ВТОРНИК \n'
            cursor.execute(rasp2)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        CРЕДА - ЧИЛЛ\n\n        ЧЕТВЕРГ-тоже чилл \n \n'
            fullr += '        ПЯТНИЦА \n'
            cursor.execute(rasp5)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')
            fullr += '        СУББОТА \n'
            cursor.execute(rasp6)
            for (n_uroka, predmet, n_cabinet, time, prepod) in cursor:
                aa = (("{}|  {}  {}  {}  {}".format(n_uroka, predmet, n_cabinet, time, prepod)))
                fullr += str(aa)
                fullr += str('\n')
                fullr += '———————————————————————————————'
                fullr += str('\n')
                fullr += str('\n')

            bot.send_message(message.chat.id, f'Следующая неделя(нечетная):\n{fullr}')

    elif message.text.lower() not in command_list:
        bot.send_message(message.chat.id, 'шо ты буровиш ')


bot.polling(none_stop=True, interval=0)
