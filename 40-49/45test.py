from pprint import pprint
import re
from graphviz import Digraph
from collections import defaultdict

G = Digraph(format='png')
G.attr('node', shape='circle', fontname='TakaoPGothic')

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
        self.phrase = "".join([morph.surface for morph in morphs]) # 文節


with open('./ans45.txt', 'w') as f:
  for sentence in sentences:
    for chunk in sentence.chunks:
      for morph in chunk.morphs:
        if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
          cases = []
          for src in chunk.srcs:  # 見つけた動詞の係り元chunkから助詞を探す
            cases = cases + [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞']
          if len(cases) > 0:  # 助詞が見つかった場合は重複除去後辞書順にソートして出力
            cases = sorted(list(set(cases)))
            line = '{}\t{}'.format(morph.base, ' '.join(cases))
            print(line, file=f)
          break