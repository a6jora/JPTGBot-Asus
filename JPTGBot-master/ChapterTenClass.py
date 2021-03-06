from ChapterClass import ChapterClass


class ChapterTenClass(ChapterClass):

    def __init__(self):
        dictionary = {'оживленный':'にぎやか',
                      '有名 - знаменитый':'ゆうめい',
                      '親切 - добрый':'しんせつ',
                      '暇 - свободный (о времени)':'ひま',
                      '便利 - удобный':'べんり',
                      'красивый, симпатичный, чудесный':'すてき',
                      '低い - низкий':'ひくい',
                      'вкусный':'おいしい',
                      '忙しい - занятый':'いそがしい',
                      '楽しい - веселый':'たのしい',
                      '黒い - черный':'くろい',
                      '桜 - сакура':'さくら',
                      '車 - машина':'くるま',
                      '所　- место':'ところ',
                      '寮 - общежитие':'りょう',
                      '生活 - жизнь, быт':'せいかつ',
                      '仕事 - работа':'しごと',
                      'как':'どう',
                      'какой, что за..':'どんな',
                      'который из (трех и более предметов)':'どれ'}
        super().__init__(dictionary)
