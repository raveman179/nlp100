"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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
        self.phrase = "".join([morph.surface for morph in morphs]) # 文節

def show_dependency(chunks):
    for i, chunk in enumerate(chunks):
        line = "{}  {}\t＝＞ dst[{}] srcs{}".format(i, chunk.phrase, chunk.dst, chunk.srcs)
        print(line)

def src_to_dst(chunks):
    symbols = r"[()（）、。「」『』〈〉]"
    symbol_pat = re.compile(symbols)

    for i, chunk in enumerate(chunks):
        src_phrase = symbol_pat.sub("", chunk.phrase)
        dst_phrase = symbol_pat.sub("", chunks[chunks[i].dst].phrase)
        
        print("{}\t{}".format(src_phrase, dst_phrase))

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

    src_to_dst(chunks)