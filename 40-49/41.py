"""
41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．
本章の残りの問題では，ここで作ったプログラムを活用せよ．

* 0 17D 1/1 0.388993
人工	名詞,一般,*,*,*,*,人工,ジンコウ,ジンコー
知能	名詞,一般,*,*,*,*,知能,チノウ,チノー

出力例
0 人工知能　＝＞　dst(17) srcs[]

* 2 3D 0/0 0.758984
AI	名詞,一般,*,*,*,*,*
* 3 17D 1/5 0.517898
〈	記号,括弧開,*,*,*,*,〈,〈,〈
エーアイ	名詞,固有名詞,一般,*,*,*,*
〉	記号,括弧閉,*,*,*,*,〉,〉,〉
）	記号,括弧閉,*,*,*,*,）,）,）
と	助詞,格助詞,引用,*,*,*,と,ト,ト
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
、	記号,読点,*,*,*,*,、,、,、

出力例

2 AI ＝＞　dst(3) srcs[]
3 〈エーアイ〉)とは、　＝＞　dst(17) srcs[2]

もし、文字列の一番初めの文字が'*'なら
    \sで区切ってリストにする
    phrase_num = 
"""

from pprint import pprint
import re

class Morph:
    def __init__(self, line):
        """
        cabochaでパースした形態素の行を一行づつ加工して、
        クラス変数として読み込む。
        """
        surface, attribute = line.split('\t')
        attr = attribute.split(',')
        self.surface = surface
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]

class Chunk:
    def __init__(self, morphs, dst):
        """
        srcs・・・[[1個目の文節の係り元],[2個目の文節の係り元],[3個目の文節の係り元]・・・・・]
        の形で添え字を渡すとn個目の係り元リストが帰ってくるようにする・・・？
        """
        self.morphs = morphs
        self.dst = dst  # 係り先インデックス番号
        self.srcs = []  # 係り元インデックス番号のリスト
        self.phrase = morphs.surface # 文節

filename = "40-49/ai.ja.txt.parsed"
with open(filename, mode='r', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')
    explain_list = blocks[2].split('\n')

# pprint(explain_list)

# print(explain_list[0].split()
    chunks = []
    morphs = []
    dst = "17"
    morphs.append(Chunk(Morph(explain_list[1]), '17'))

    print(morphs)



    # '*'で始まる要素をカウントして、個数分の空きリストをchunk.srcsに追加
    # 係り元を入れるリストを作る。
    # chunk.srcs = [[] for l in explain_list if l.startswith('*')]
    # pram = []

    # explain_listの中身を読み取る
    # for word in explain_list:
        
    #     # wordが係り受け分析結果の場合
    #     if word.startswith('*'):
    #         pram = word.split()
    #         chunk.dst = pram[2][:-1]
    #         chunk.srcs[int(chunk.dst)].append(index)



        
        # # surfaceに値が代入されている場合
        # elif surface != '':
        #     sentence = chunk.surface
        #     sentence.append(surface)

        #     #かかり先が存在する場合のコードを考える        

        # # wordが形態素分析結果の場合
        # else:
        #     morph = Morph(word)
        #     surface += morph.surface


    # リストをフォーマットして出力する
    
    




