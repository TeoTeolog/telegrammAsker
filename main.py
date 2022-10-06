import telebot
import random
from telebot import types

facts = 'С другой стороны рамки и место обучения кадров требуют от нас анализа дальнейших направлений развития. Товарищи!'
thinks = 'С другой стороны рамки и место обучения кадров требуют от нас анализа дальнейших направлений развития. Товарищи!'
facts = facts.split(' ')
thinks = thinks.split(' ')

# Создаем бота
bot = telebot.TeleBot('5677823217:AAEV3P1WTh8xZO77EMS6ZKTN-9si9HzjG7Y')


class BotBrain:

    def __init__(self):
        self.curChatAction = None
        self.actionSwitcher = None

    def setCurAction(self, event):
        self.curChatAction = event

    def doCurChatAction(self, *args):
        answer = self.curChatAction(*args)
        # switcher action и установка curAction в нужный
        return answer


botBrain = BotBrain()


def callBack(message):
    if message.text.strip() == 'хтонь':
        return random.choice(facts)
    elif message.text.strip() == 'Поговорка':
        return random.choice(thinks)
    return 'Ошибка'


botBrain.setCurAction(callBack)


def addButtons(buttonList):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in buttonList:
        item = types.KeyboardButton(i)
        markup.add(item)
    return markup


@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = addButtons(['факт', 'хор', 'хтонь'])
    bot.send_message(m.chat.id,
                     str(m.chat.id)+' Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = botBrain.doCurChatAction(message)
    markup = addButtons(['фактs', 'хорs', 'хтонь'])
    bot.send_message(message.chat.id, answer, reply_markup=markup)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
