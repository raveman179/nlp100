"""
ーーーーーーーーーー実験用ーーーーーーーーーー
"""

class Morph:
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
        self.morph_list = []

    def worddict(self):
        morphdict = {"surface":self.surface, "base":self.base, "pos":self.pos, "pos1":self.pos1}
        return morphdict

class Chunk(Morph):
    def __init__(self):
        super().__init__()
        # self.morphs = self.morph_list
        self.morphs = []
        self.dst = ""
        self.srcs = []
        self.chunk_list = []

morph = Morph()
morph.morph_list.append("0")

chunks = Chunk()
morph.morph_list = chunks.morphs
# chunks.morphs.append("1")
# chunks.morphs.append("2")

chunks.morphs.append("1")
chunks.morphs.append("2")

print(morph.morph_list)