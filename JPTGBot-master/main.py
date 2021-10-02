import telebot

from ChapterAdjectiveClass import ChapterAdjectiveClass
from ChapterOneClass import ChapterOneClass
from ChapterThreeClass import ChapterThreeClass
from ChapterTwoClass import ChapterTwoClass
from ChapterFiveClass import ChapterFiveClass
from ChapterFourClass import ChapterFourClass
from ChapterSixClass import ChapterSixClass

TOKEN = "1913192559:AAEFpgqawEKF-xies_tr0cnU5y2d3IqZ00A"

bot = telebot.TeleBot(TOKEN)
global word
chapter1 = ChapterOneClass()
chapter2 = ChapterTwoClass()
chapter3 = ChapterThreeClass()
chapter4 = ChapterFourClass()
chapter5 = ChapterFiveClass()
chapter6 = ChapterSixClass()
chapter27 = ChapterAdjectiveClass()
chapters = [chapter1, chapter2, chapter3, chapter4,chapter5,
            chapter6]
data = {}
word = ['', '']
current_chapter = chapter1


@bot.message_handler(commands=['start'])
def start(message):
    data[message.chat.id] = 0
    menu(message)


def menu(message):
    bot.send_message(message.chat.id, 'Выберите номер главы: \n'
                                      '1. Глава 1\n'
                                      '2. Глава 2\n'
                                      '3. Глава 3\n'
                                      '4. Глава 4\n'
                                      '5. Глава 5　(глаголы)\n'
                                      '6. Глава 6\n'
                                      '7. Глава 7\n'
                                      '\n'
                                      'для выхода отправтье "exit"')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global word, current_chapter
    if message.text.lower() == 'exit':
        data[message.chat.id] = 0
        menu(message)
    elif data[message.chat.id] == 0:
        try:
            data[message.chat.id] = 1
            current_chapter = chapters[int(message.text) - 1]
            bot.send_message(message.chat.id, f'Выбрана Глава {message.text} \nДля перехода в меню отправьте: exit')
        except Exception as ex:
            menu(message)
    elif data[message.chat.id] == 2:
        if message.text == word[1]:
            bot.send_message(message.chat.id, 'Верно')
        else:
            bot.send_message(message.chat.id, f'Правильный ответ: {word[1]}')
        print(word[1])
        data[message.chat.id] = 1
    if data[message.chat.id] == 1:
        word = current_chapter.random_word()
        print(word)
        bot.send_message(message.chat.id, f'Слово: {word[0]}')
        data[message.chat.id] = 2
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
