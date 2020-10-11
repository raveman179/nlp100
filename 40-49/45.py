"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
 この文は「作り出す」という１つの動詞を含み，「作り出す」に係る文節は「ジョン・マッカーシーは」，
 「会議で」，「用語を」であると解析された場合は，次のような出力になるはずである．

作り出す	で は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""

from pprint import pprint
from collections import defaultdict
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

def verbs_extract(chunks):
    """
    chunk内のposが動詞の物のbaseをkey,
    chunk.srcsで参照する文節が助詞のものをvalueとしてsetに追加する

    key
    """
    verbs_dict = defaultdict(list)
    verbs = ""
    pos_base = set()

    for chunk in chunks:
        for chunk_morph in chunk.morphs:
            if chunk_morph.pos == "動詞":
                verbs = chunk_morph.base
                break
        else:
            continue

        #　助詞がかかっている動詞と判定されないものが有る

        for src in chunk.srcs:
            for morph in chunks[src].morphs:
                if morph.pos == "助詞":
                    pos_base.add(morph.base)
                    continue

        if not verbs or len(pos_base) == 0:
            break
        else:
            verbs_dict[verbs].append(set(pos_base))
            # verbs_dict[verbs][0].add(set(pos_base))
            verbs = ""
            pos_base = set()

    return verbs_dict

filename = "40-49/ai.ja.txt.parsed"
with open(filename, mode='r', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')
    explain_list = [b.split('\n') for b in blocks]
    # pprint(explain_list)

    chunks = [] # Chunkオブジェクトのリスト

    morphs = []
    dst = ""
    pram = []

   # explain_listの中身を読み取る
    for explain in explain_list:
        for i, word in enumerate(explain):
            # wordが係り受け分析結果の場合
            if explain[0] == '':
                continue
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

    #phraseから記号を削除する
    for chunk in chunks:
        chunk.phrase = del_symbol(chunk.phrase)

    
    # print(len(chunks))
    # [print(i, c.phrase) for i, c in enumerate(chunks)]
    # pprint(blocks[24])
    # [print(str(i), e)for i, e in enumerate(explain_list)]
    pprint(verbs_extract(chunks))