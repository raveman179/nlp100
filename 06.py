# coding: utf-8
sen_1 = 'paraparaparadise'
sen_2 = 'paragraph'

def genNgram(sentence, N):
    result = [sentence[i:i+N] for i in range(len(sentence) - N + 1)]
    return result

def in_se(bigram):
    in_se = 'in se' if 'se' in bigram else 'not in se'
    return in_se

X_bigram = genNgram(sen_1, 2)
Y_bigram = genNgram(sen_2, 2)
X_Y_and =set(X_bigram) & set(Y_bigram)
X_Y_or = set(X_bigram + Y_bigram)
X_Y_diff = set(X_bigram) ^ set(Y_bigram)

print(X_Y_and)
print(X_Y_or)
print(X_Y_diff)

print('X bi-gram ' + in_se(X_bigram))
print('Y bi-gram ' + in_se(Y_bigram))