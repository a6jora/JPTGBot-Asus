from ChapterClass import ChapterClass


class ChapterElevenClass(ChapterClass):

    def __init__(self):
        dictionary = {'очень':'とても',
                      'не очень (употр. с отрицанием)':'あまり',
                      'и к тому же, также':'そして',
                      '料理 - блюдо, еда':'りょうり',
                      '飲み物　- напиток':'のみもの',
                      '野球 - бейсбол':'やしゅう',
                      '音楽 - музыка':'おんがく',
                      '歌 - песня':'うた',
                      '歌舞伎 - кабуки':'かぶき',
                      '絵 - картина':'え',
                      '字 - буква, знак':'じ',
                      '細かいお金 - мелкие деньги, мелочь':'こまかいおかね',
                      '用事 - дело':'ようじ',
                      '約束 - обещание, договоренность':'やうそく',
                      'ご主人 - муж (чужой)':'ごしゅじん',
                      '夫 - муж (свой)':'おっと',
                      '奥さん - жена (чужая)':'おくさん',
                      '妻 = жена (своя)':'つま',
                      '早く - быстро, рано':'はやく',
                      'быть, находиться (об одушевленных предметах)':'います',
                      'быть, находиться (об неодушевленных предметах)':'あります'}
        super().__init__(dictionary)