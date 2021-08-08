v_1 = 3
v_2 = 5
word_1 = 'fizz'
word_2 = 'buzz'

for x in range(1,1000):
    if x%(v_1*v_2) == 0:
        print(word_1 + word_2)
    elif x%v_1 == 0:
        print(word_1)
    elif x%v_2 == 0:
        print(word_2)
    else:
        print(x)