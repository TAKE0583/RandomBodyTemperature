import random

C = 0
D = int(input('生成したい数を入力してください--->'))
f = open('myfile.txt', 'w', encoding='UTF-8')

while(C < D):
    A = (random.uniform(35.8, 36.9))
    B = round(A, 1)
    f.write(str(B) + '\n')
    C+=1
f.close()