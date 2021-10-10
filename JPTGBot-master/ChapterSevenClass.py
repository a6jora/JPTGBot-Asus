from ChapterClass import ChapterClass


class ChapterSevenClass(ChapterClass):

    def __init__(self):
        dictionary = {'紅茶 - черный чай': 'こうちゃ',
                      '牛乳　- молоко': 'ぎゅうにゅう',
                      'お酒 - крепкое спиртное, саке': 'おさけ',
                      'お米 - рис': 'おこめ',
                      '切ります - резать': 'きります',
                      '送ります - посылать, отправлять': 'おくります',
                      'давать': 'あげます',
                      'получать': 'もらいます',
                      '貸します- давать в долг': 'かします',
                      '借ります - брать в долг': 'かります',
                      '教えます - преподавать': 'おしえます',
                      '習います - изучать': 'ならいます',
                      'звонить': 'かけます',
                      '手　- рука': 'て',
                      'палочки для еды': 'はし',
                      'ножницы': 'はさみ',
                      '紙 - бумага': 'かみ',
                      '花 - цветок': 'はな',
                      '荷物 - багаж,груз, посылка': 'にもつ',
                      'お金 - деньги': 'おかね'}
        super().__init__(dictionary)
