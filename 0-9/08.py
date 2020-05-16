# coding: utf-8
sentence = 'I am an NLPer'

def cipher(sen):
    asc = 0
    for i in range(len(sen)):
        if sen[i].islower(): 
            crpt = chr(219 - ord(sen[i]))
            sen = sen[:i] + crpt + sen[i+1:]
    return sen

crypt_sen= cipher(sentence)
re_crypt_sen = cipher(crypt_sen)

print(crypt_sen)
print(re_crypt_sen)

