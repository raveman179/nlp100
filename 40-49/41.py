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

import pandas as pd
from pprint import pprint
import re
import collections

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
        の形で添え字を渡すとn個目の係り元リストが帰ってくるようにする。
        """
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

    def dst_prams(self, prams):
        """
        渡された係り先パラメータをパースする。
        また、係り先をsrcsに追加する。

        srcsにsrcs[index]が存在するなら:
            何もしない
            存在しないなら:
                srcs.append

        """
        params_lst = params.split("\s")
        index = params_lst[0]
        to_dst = params_lst[1]

        #係り元存在チェック





        if self.srcs[to_dst-1:to_dst]:
            self.srcs[to_dst].append(index)
        else:
            lst = []
            lst.append(index)
            self.srcs[to_dst].insert(to_dst, lst)


        return index, 


    def join_surface(self):
        """
        morph.surfaceを結合して文節ごとに返す
        """
        self.surface = []
         
    # def src_to_dst(self, index, dst):
    #     """
    #     以下の形でformatで文節を返す
    #     0 人工知能　＝＞　dst(17) srcs[]
    #     """
    #     self.index = index
    #     print(self.index + " " + join_surface)
        

filename = "40-49/ai.ja.txt.parsed"
with open(filename, mode='r', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

explain_list = blocks[2].split('\n')
phrase_count = [i for i in explain_list if i.startswith('*')]

# pprint(explain_list)

# for word in explain_list:
#     if word.startswith('*'):
#         params = Chunk.dst_prams(word)

    
    
    
    
    # else:    
    #     attr = re.split('\t|,', word)
    #     morph.surface = attr[0] 
    #     morph.base = attr[7]
    #     morph.pos = attr[1]
    #     morph.pos1 = attr[2]
    #     line = morph.worddict()
    #     morph.morph_list.append(line)



