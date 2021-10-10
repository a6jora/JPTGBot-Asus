from ChapterClass import ChapterClass


class ChapterThirteenClass(ChapterClass):

    def __init__(self):
        dictionary = {'月曜日 - понедельник': 'げつようび',
                      '火曜日 - вторник': 'かようび',
                      '水曜日 - среда': 'すいようび',
                      '木曜日 - четверг': 'もくようび',
                      '金曜日 - пятница': 'きにょうび',
                      '土曜日 - суббота': 'どようび',
                      '日曜日 - воскресенье': 'にちようび',
                      '一日 - 1 число': 'ついたち',
                      '二日 - 2 число': 'ふつか',
                      '三日 - 3 число': 'みっか',
                      '四日 - 4 число': 'よっか',
                      '五日 - 5 число': 'いつか',
                      '六日 - 6 число': 'むいか',
                      '七日 - 7 число': 'なのか',
                      '八日 - 8 число': 'ようか',
                      '九日　- 9 число': 'ここのか',
                      '十日 - 10 число': 'とおか',
                      '十四日 - 14 число': 'じゅうよっか',
                      '二十四日 - 24 число': 'にじゅうよっか',
                      '二十日 - 20 число': 'はつか',
                      '一月 - 1 месяц': 'いちがつ'}
        super().__init__(dictionary)
