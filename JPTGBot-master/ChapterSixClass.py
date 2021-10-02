from ChapterClass import ChapterClass


class ChapterSixClass(ChapterClass):

    def __init__(self):
        dictionary = {'起きます - просыпаться, вставать':'おきます',
                      '寝ます - спать':'ねます',
                      '働きます - работать':'はたらきます',
                      '休みます - отдыхать':'やすみます',
                      '勉強します - учиться':'べんきょうします',
                      '終わります - заканчиваться':'おわります',
                      '銀行 - банк':'ぎんこう',
                      '郵便局 - почтовое отделение':'ゆうびんきょく',
                      '図書館 - библиотека':'としょかん',
                      '美術館　- музей':'びじゆつかん',
                      '今 - сейчас':'いま',
                      '半 - половина':'はん',
                      '何時 - сколько времени':'なんじ',
                      '何分 - сколько минут':'なんぷん',
                      '午前 - первая половина дня':'ごぜん',
                      '午後 - вторая половина дня':'ごご',
                      '朝 - утро':'あさ',
                      '昼 - середина дня':'ひる',
                      '晩 - вечер':'ばん',
                      '夜 - вечер':'よる',
                      'позавчера':'あととい',
                      'вчера':'きのう',
                      '今日　- сегодня':'きょう',
                      '明日 - завтра':'あした',
                      'послезавтра':'あさって',
                      '行きます - идти':'いきます',
                      '帰ります - возвращаться, уходить домой':'かえります',
                      '学校 - школа':'',
                      '駅 - станция':'えき',
                      '飛行機 - самолет':'ひこうき',
                      '船 - корабль':'ふね',
                      '電車 - поезд':'でんしゃ',
                      '地下鉄　- метро':'ちかてつ',
                      '新幹線 - скоросной поезд "синкансен"':'しんかんせん',
                      '自転車 - велосипед':'じてんしゃ',
                      '歩いて - пешком':'あるいて'}
        super().__init__(dictionary)