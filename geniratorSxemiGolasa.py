from config import *
from Text import *


def gen(massGPT):
    masGPT = razdelSlogovGPT(massGPT)
    razgovorNri = []
    razgovorKup = []
    for a in range(len(masGPT[0])):
        razgovorNri.append(obrobca(masGPT[0][a]))

    for a in range(len(masGPT[1])):
        for i in range(len(masGPT[1][a])):
            razgovorKup.append(obrobca(masGPT[1][a][i]))

    return [razgovorNri, razgovorKup]





def obrobca(mas):
    lenn = len(mas)
    kom = obrobcaMasKom(mas)
    spid = obrobcaSpid(kom, lenn)
    zborka =[]
    for i in range(lenn):
        zborka.append([spid[i], ((spid[i]-1)/2)+1, 1])
    return zborka





def obrobcaMasKom(mas):
    masKom = []
    for i in range(len(mas)):
        if mas[i] == "," or mas[i] == "." or mas[i] == "\n":
            masKom.append(i)
    return masKom

def obrobcaSpid(mas, lenn):
    znasenia = []
    if len(mas) == 0:
        if lenn % 2 == 0:
            for i in range(lenn):
                x = i-lenn/2
                znasenia.append(formul1(x, lenn))
            return znasenia
        else:
            for i in range(lenn):
                x = i-(lenn-1)/2
                znasenia.append(formul2(x, lenn))
            return znasenia
    mas.append(lenn)
    for y in range(len(mas)):
        if y == 0:
            u = mas[0]
        else:
            u = abs(mas[y-1]-mas[y])

        if u % 2 == 0:
            for i in range(u):
                x = i - u / 2
                znasenia.append(formul1(x, u))
        else:
            for i in range(u):
                x = i - (u - 1) / 2
                znasenia.append(formul2(x, u))
    return znasenia


def formul1(x, u):
    return 1.5 - abs(x * (1 / u))
def formul2(x, u):
    return 1.5 - abs(x * (1 / (u - 1)))


