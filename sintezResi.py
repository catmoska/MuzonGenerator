import wave
import struct
from Text import *
from config import *

def sintegGpt(masGPT,stenia,neim = 'olas', T = False):
    nrinev = masGPT[0][0]
    for i in range(len(masGPT[0]) - 1):
        nrinev += "\n" + masGPT[0][i + 1]

    kuplet = []
    for i in range(len(masGPT[1])):
        kuplet.append(masGPT[1][i][0])
        for u in range(len(masGPT[1][i]) - 1):
            kuplet[i] += "\n" + masGPT[1][i][u + 1]

    nesna = kuplet[0] + "\n" + nrinev
    for i in range(len(masGPT[1]) - 1):
        nesna += "\n" + kuplet[i + 1] + "\n" + nrinev
    del masGPT, i, u, nrinev, kuplet
    ##############
    nrinevS = stenia[0][0]
    for i in range(len(stenia[0]) - 1):
        nrinevS += stenia[0][i + 1]

    kupletS = []
    for i in range(len(stenia[1])):
        kupletS.append([stenia[1][i][0]])
        for u in range(len(stenia[1][i]) - 1):
            kupletS[i].append(stenia[1][i][u + 1])

    nesnaS = kupletS[0] + nrinevS
    for i in range(len(stenia[1]) - 1):
        nesnaS += kupletS[i + 1] + nrinevS
    del stenia, i, u, nrinevS, kupletS
    sintez(razdelSlogov(nesna), nesnaS, neim, T)



# запуск синтеза
def sintez(mas, stenia, neim='olas', T=False):
    masAud = onredileniaSlovo(mas)
    del(mas)

    golas = wave.open("kes\g"+neim+".wav", mode="wb")
    g = wave.open("golos\eNrim.wav", mode="rb")
    golas.setparams(g.getparams())
    del (g)

    zaderzka = []

    if T: print("етап в sintezResi 1/5 виполнен")

    for i in range(len(masAud)):
        u = masAud[:(i+1)]
        p = 0
        for o in range(len(u)):
            p += u[o][2]
        zaderzka.append(p)

    if T: print("етап в sintezResi 2/5 виполнен")

    muz = []
    for i in range(len(zaderzka)):
        muza = masAud[i][3]
        frameCount = muza.getnframes()
        data = muza.readframes(frameCount)
        muzonn = list(struct.unpack("<" + str(frameCount) + "h", data))
        muzonn = obrabotka(muzonn, stenia[i])
        if i != 0:
            freimNronusk = int(round(zaderzka[i-1]*freimS*obrabotkaZderzki(stenia[i])))   #######
        else:
            freimNronusk = 0

        muz.append(zvik(freimNronusk, muzonn))
    del data, frameCount, muzonn, freimNronusk

    if T: print("етап в sintezResi 3/5 виполнен")

    nerexod = []
    for i in range(len(muz)):
        nerexod.append(len(muz[i]))

    if T: print("етап в sintezResi 4/5 виполнен")


    resultat = []
    for i in range(max(nerexod)):
        if T and i % 20000 == 0: print("виполнения етапа 5: озвучина на "+str(i)+"/"+str(max(nerexod))+"  :  "+str(100/max(nerexod)*i)+"%")

        for y in range(len(muz)):
            if y < len(muz) and nerexod[y] == i:
                del (nerexod[y])
                del (muz[y])

        res = 0
        for u in range(len(muz)):       # оптимизасия
            res += muz[u].dani(i)
        resultat.append(res)

    if T: print("етап в sintezResi 5/5 виполнен")

    frameCount0 = struct.pack("<" + str(len(resultat)) + "h", *resultat)
    golas.writeframes(frameCount0)
    golas.close()

# обработка задерзки звука
def obrabotkaZderzki(tip):
    return 1           #################################

# обработка звука
def obrabotka(audi, tip):
    return audi           #################################




# типаов слогов в мас
def onredileniaSlovo(mas):
    mas2 = []

    for i in range(len(mas)):
        mas2.append(onredileniaSlog(mas[i]))
    return mas2

# опредиления типа слога
def onredileniaSlog(text):
    xx = len(text) - 1
    if xx > 3:
        xx = 3
    for yy in range(len(clog[xx])):
        if clog[xx][yy] == text:
            # print(xx, yy)
            return [xx, yy, clogTaim[xx][yy], wave.open("golos\golos" + str(xx) + "\sn" + str(yy + 1) + ".wav", mode="rb")]
    print("EROOR: slog : " +text)
    return [0, 33, clogTaim[1][3], wave.open("golos\golos" + str(1) + "\sn" + str(33 + 1) + ".wav", mode="rb")]


# тип даних для уменшения нагрузки на оперативку
class zvik:
    mas = []
    nov = 0
    def __init__(self,novv,mass):
        self.nov = novv
        self.mas = mass

    def dani(self,i):
        if i >= self.nov:
            return self.mas[i-self.nov]
        else:
            return 0

    def __len__(self):
        return len(self.mas)+self.nov




