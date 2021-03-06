from ChapterClass import ChapterClass


class ChapterNineClass(ChapterClass):

    def __init__(self):
        dictionary = {'鮪 - тунец':'まぐろ',
                      '蝦 - креветка':'えび',
                      'краб':'かに',
                      'кальмар':'いか',
                      '蛸 - осьминог':'たこ',
                      '貝 - ракушка, моллюски':'かい',
                      '調味料 - приправы':'ちょうみりょう',
                      'соевый соус':'しょうゆ',
                      '砂糖 - сахар':'さとう',
                      '塩 - соль':'しお',
                      'мисо':'みそ',
                      '油 - масло, жир':'あぶら',
                      'перец':'こしょう',
                      'японский хрен, васаби':'わさび',
                      '分かります - понимать, знать':'わかります',
                      'ненавистный':'きらい',
                      '上手 - умелый':'じょうず',
                      '下手 - неумелый':'へた',
                      '静か - тихий, спокойный':'しずか'}
        super().__init__(dictionary)
