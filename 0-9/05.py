# coding: utf-8

sentence = "i am an NLPer"
# sen_list = [i,am,an,NLPer]
sen_list = sentence.split(" ")

def genNgram(sentence, N):
    result = [sentence[i:i+N] for i in range(len(sentence) - N + 1)]
    return result

print(genNgram(sentence, N=2))

print(genNgram(sen_list, N=2))