import telebot

from ChapterAdjectiveClass import ChapterAdjectiveClass
from ChapterOneClass import ChapterOneClass
from ChapterJCountClass import ChapterJCountClass
from ChapterTwoClass import ChapterTwoClass
from ChapterVerbClass import ChapterVerbClass
from ChapterThreeClass import ChapterThreeClass
from ChapterFourClass import ChapterFourClass
from ChapterFiveClass import ChapterFiveClass
from ChapterSixClass import ChapterSixClass
from ChapterSevenClass import ChapterSevenClass
from ChapterEightClass import ChapterEightClass
from ChapterNineClass import ChapterNineClass
from ChapterTenClass import ChapterTenClass
from ChapterElevenClass import ChapterElevenClass
from ChapterTwelveClass import ChapterTwelveClass
from ChapterThirteenClass import ChapterThirteenClass
from ChapterFourteenClass import ChapterFourteenClass


TOKEN = "1913192559:AAEFpgqawEKF-xies_tr0cnU5y2d3IqZ00A"

bot = telebot.TeleBot(TOKEN)
global word
chapter1 = ChapterOneClass()
chapter2 = ChapterTwoClass()
chapter3 = ChapterThreeClass()
chapter4 = ChapterFourClass()
chapter5 = ChapterFiveClass()
chapter6 = ChapterSixClass()
chapter7 = ChapterSevenClass()
chapter8 = ChapterEightClass()
chapter9 = ChapterNineClass()
chapter10 = ChapterTenClass()
chapter11 = ChapterElevenClass()
chapter12 = ChapterTwelveClass()
chapter13 = ChapterThirteenClass()
chapter14 = ChapterFourteenClass()
chapter15 = ChapterVerbClass()
chapter16 = ChapterAdjectiveClass()
chapter17 = ChapterJCountClass()
chapters = [chapter1, chapter2, chapter3, chapter4,chapter5,
            chapter6, chapter7, chapter8, chapter9 ,chapter10,
            chapter11, chapter12, chapter13, chapter14, chapter15,
            chapter16, chapter17]
data = {}
word = ['', '']
current_chapter = chapter1


@bot.message_handler(commands=['start'])
def start(message):
    data[message.chat.id] = 0
    menu(message)


def menu(message):
    bot.send_message(message.chat.id, 'Выберите номер главы: \n'
                                      '1. Слова: 1 - 20\n'
                                      '2. Слова: 21 - 40\n'
                                      '3. Слова: 41 - 60\n'
                                      '4. Слова: 61 - 80\n'
                                      '5. Слова: 81 - 100\n'
                                      '6. Слова: 101 - 120\n'
                                      '7. Слова: 121 - 140\n'
                                      '8. Слова: 141 - 160\n'
                                      '9. Слова: 161 - 180\n'
                                      '10. Слова: 181 - 200\n'
                                      '11. Слова: 201 - 220\n'
                                      '12. Слова: 221 - 240\n'
                                      '13. Японскиие даты и дни недели\n'
                                      '14. Семья\n'
                                      '15. Глаголы\n'
                                      '16. Прилагательные\n'
                                      '17. Японскиие числительные\n'
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
