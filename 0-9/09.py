# coding: utf-8
import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

def wordrandom(sentence):
    senlist=sentence.split()
    for i in range(len(senlist)):
        word = senlist[i]
        if len(word) > 4:
            ran = "".join(random.sample(word[1:-1], len(word)-2))
            r_word = [word[0],ran,word[-1]]        
            senlist[i] = "".join(r_word)
    result = " ".join(senlist)
    return result

print(sentence)
print(wordrandom(sentence))