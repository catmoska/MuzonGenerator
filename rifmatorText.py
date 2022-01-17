from Text import *

# рачитавает бал рифми
def osenkaf(text):
    return rifmatorSlov(text)*zanret(text)*sisloSlov(text)

# виберает лучий текст из масива
def rifmatorTest(masResin, t = False):
    sislo = len(masResin)
    osenka = []

    for i in range(sislo):
        osenka.append(0)

    for i in range(sislo):
        osenka[i] = osenkaf(masResin[i])

    del(sislo)

    otvet = 0
    for i in range(len(osenka)):

        if i == len(osenka)-1:
            break

        if osenka[otvet] < osenka[i+1]:
            otvet = i+1

    if osenka[otvet] <= 0.05:
        print("EROR: ответ неронки имеить очень мало балов")
        return "ответ неронки имеить очень мало балов?"
    if t:
        # if osenka[otvet] <= 0.3:
            # print("EROR: ответ неронки имеить мало балов")   #############################
        return masResin[otvet]
    else:
        # if osenka[otvet] <= 0.3:
            # print("EROR: ответ неронки имеить мало балов")  ###################################
        return otvet

# нормализатор числа от 0 до 1
def normaliz(A):
    if A >= 1:
        return 1
    elif A <= 0.01:
        return 0
    else:
        return A


# осенивает качество рифми (незделан)
def rifmatorSlov(text):
    return normaliz(1)

# провераит на запрети и ненузний слова текст
def zanret(text):
    mas = sistkaSKraiov(rasiedinenia(text))
    del(text)
    ball = 0.6
    ii = 0
    for i in mas:
        if i == '"' or i == "'" or i == '\n' or i == "_" or i == "/" or i == "=" or i == "+" or i == "*" or \
                i == "«" or i == "»" or i == "`" or i == "@" or i == "#" or i == "№" or i == "$" or i == "%" or\
                i == "^" or i == "&" or i == "[" or i == "]" or i == "{" or i == "}" or i == "~" or i == "\xa0" \
                or i == "\xa1" or i == "\xa2" or i == "\xa3" or i == "\xa4" or i == "\xa5" or i == "\xa6" \
                or i == "\xa7" or i == "\xa8" or i == "\xa9":
            return 0
        elif i == ":" or i == ";":
            ball -= 0.05
        elif i == "," or i == "." or i == "-" or i == "—" or i == "!" or i == "?":
            ball += 0.05
        elif i == "(" or i == ")" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or \
                i == "6" or i == "7" or i == "8" or i == "9":
            ball -= 0.1
            return 0.1   # времиний бан связи с синтезатором речи
        elif i.lower() == "a" or i.lower() == "b" or i.lower() == "c" or i.lower() == "d" or i.lower() == "e" or \
                i.lower() == "f" or i.lower() == "g" or i.lower() == "h" or i.lower() == "i" or i.lower() == "j" or \
                i.lower() == "k" or i.lower() == "l" or i.lower() == "m" or i.lower() == "n" or i.lower() == "o" or \
                i.lower() == "p" or i.lower() == "q" or i.lower() == "r" or i.lower() == "s" or i.lower() == "t" or \
                i.lower() == "u" or i.lower() == "v" or i.lower() == "w" or i.lower() == "x" or i.lower() == "y" or \
                i.lower() == "z":
            if i.lower() == "h":
                u = ''
                for r in range(7):
                    u += mas[r+ii].lower()
                    if u == "http://":
                        return 0
            ball -= 0.03
        ii += 1
    return normaliz(ball)

# проверяет зилателное число слов для алгоритма
def sisloSlov(text):
    i = nodsotSlov(text)
    del (text)
    if i < 2 or i > 15:
        return 0
    return normaliz(-0.04 * (i-8)*(i-8) + 1.1)











