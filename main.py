import random

S =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
N = int(input("Сколько символов в пароле ?"))
P = ""

for i in range(N):
    A = random.randint(0, len(S)-1)
    P += S[A]

print (P)
