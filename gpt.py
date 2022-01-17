import config
from rifmatorText import *
from config import *


# создает нузное каличества припевов и куплетов и виводит
def generatorPesni(text, level, T=True):

    if isinstance(level, int):
        zanis = levelPesni[level]
    else:
        zanis = level

    del(level)
    nrinev = []
    kuplet = []
    for i in range(zanis[2]):
        kuplet.append([])


    for i in range(zanis[0]):
        d = sistkaTextSKraiov(rifmatorTest(minusSlovMasV(generatorStroski(text, sravneniaStrok, True), text), True))
        text += "\n" + d
        nrinev.append(d)

    for i in range(zanis[2]):
        for q in range(zanis[1]):
            d = sistkaTextSKraiov(rifmatorTest(minusSlovMasV(generatorStroski(text, sravneniaStrok), text), True))
            text += "\n" + d
            kuplet[i].append(d)
    del (d)
    del(text)

    if T:
        i = []
        i.append(nrinev)
        i.append(kuplet)
        return i

    textNesni=""
    for i in range(zanis[2]):
        textNesni += kuplet[i] + "\n\n" + nrinev + "\n\n"
    return textNesni


# тут долзен бить модуль gpt
def generatorStroski(text, k=sravneniaStrok, nrinev=False):
    config.q += 1
    mas = \
["Снова я напиваюсь, снова говорю (у-у-у-у)",
"Мы несовместимы, у меня пустой карман",
"Снова я напиваюсь, снова говорю ",
"Мы с тобой не будем никогда, никогда, никогда",
"А ты считаешь деньги в моём кошельке",
"И ты любишь только деньги, меня не совсем",
"И я вижу, как ты смотришь на этих людей",
"У кого есть своя яхта, тачка, бассейн",
"А я? Что я? Что я?",
"Слушай, я дам всё, что захочешь",
"Слушай, и, может, даже больше",
"Суммы, проси любые суммы",
"Любишь, надеюсь, меня любишь",
"Йа, йа, а-а (а-а), я давно всё понял (ага)",
"Не нужен я, нужны деньги, тачки, пойло",
"Будут деньки, обещаю, ты вернёшься",
"И я влюблюсь, я влюблюсь в тебя по новой"]
    if config.q >= len(mas):
        config.q = 0
    return [text+mas[config.q], text+mas[config.q]]



