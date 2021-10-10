from ChapterClass import ChapterClass


class ChapterFiveClass(ChapterClass):

    def __init__(self):
        dictionary = {'晩 - вечер': 'ばん',
                      '夜 - вечер': 'よる',
                      'позавчера': 'あととい',
                      'вчера': 'きのう',
                      '今日　- сегодня': 'きょう',
                      '明日 - завтра': 'あした',
                      'послезавтра': 'あさって',
                      '行きます - идти': 'いきます',
                      '帰ります - возвращаться, уходить домой': 'かえります',
                      '学校 - школа': '',
                      '駅 - станция': 'えき',
                      '飛行機 - самолет': 'ひこうき',
                      '船 - корабль': 'ふね',
                      '電車 - поезд': 'でんしゃ',
                      '地下鉄　- метро': 'ちかてつ',
                      '新幹線 - скоросной поезд "синкансен"': 'しんかんせん',
                      '自転車 - велосипед': 'じてんしゃ',
                      '歩いて - пешком': 'あるいて',
                      '食べます　- есть, кушать': 'たべます',
                      '飲みます - пить': 'のみます'}
        super().__init__(dictionary)
