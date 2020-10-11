"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，Graphviz等を用いるとよい
"""

from pprint import pprint
import re
from graphviz import Digraph
from collections import OrderedDict

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

def show_dependency(chunks):
    for i, chunk in enumerate(chunks):
        line = "{}  {}\t＝＞ dst[{}] srcs{}".format(i, chunk.phrase, chunk.dst, chunk.srcs)
        print(line)

def del_symbol(sen):
    symbols = r"[()（）、。「」『』〈〉]"
    symbol_pat = re.compile(symbols)

    phrase = symbol_pat.sub("", sen)
    
    return phrase

def noun_to_verb(chunks):
    """
    名詞　=> 動詞の係受けをする文節を取り出して、
    src_to_dstに投げて出力する
    """
  
    for chunk in chunks:
        target_dst = ""
        morph = chunk.morphs

        for m in morph:
            if m.pos == '名詞':
                target_dst = chunks[chunk.dst].morphs
                break

        for d in target_dst:
            if d.pos == '動詞':
                src = chunk.phrase
                dst = chunks[chunk.dst].phrase
                sentence = [src, dst]
                phrase = list(map(del_symbol, sentence))
                print("{}\t{}".format(phrase[0], phrase[1]))
                break

def show_graph(chunks):
    chunklist = []
    for i, chunk in enumerate(chunks):
        chunklist.append(chunk.phrase + "(" + str(i) + ")")

    for i, chunk in enumerate(chunklist):
        src_phrase = chunk
        dst_phrase = chunklist[chunks[i].dst]
        if chunks[i].dst == -1:
            break       
        G.edge(src_phrase, dst_phrase)
    G.render('./44_result')


filename = "40-49/ai.ja.txt.parsed"
with open(filename, mode='r', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')
    explain_list = blocks[2].split('\n')

    chunks = [] # Chunkオブジェクトのリスト

    morphs = []
    dst = ""
    pram = []

   # explain_listの中身を読み取る
    for i, word in enumerate(explain_list):

        # wordが係り受け分析結果の場合
        if word.startswith('*') or len(word) == 0:
            # 文節の最後でchunksにChunkオブジェクトを追加する   
            if len(morphs) > 0:
                chunks.append(Chunk(morphs, dst))
                morphs = []
                if dst == -1:
                    break
            pram = word.split()
            dst = int(pram[2][:-1])

        # wordが形態素分析結果の場合
        elif len(word) != 0:
            morphs.append(Morph(word))

    #chunksリストを検索して、chunks.dstの中身から係り元リストsrcsを作る
    for index, sentence in enumerate(chunks):
        to_dst = sentence.dst
        chunks[to_dst].srcs.append(index)

    #phraseから記号を削除して、有向グラフを作成する
    for chunk in chunks:
        chunk.phrase = del_symbol(chunk.phrase)
         
    show_graph(chunks)