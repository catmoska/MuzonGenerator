# from sintezResi import *
from config import *

# читает количество слов в тексте
def nodsotSlov(text):
    if len(text) <= 0:
        return 0

    textMas = sistkaSKraiov(rasiedinenia(text))

    del(text)

    Nslova = 1
    novtor = False
    for i in textMas:
        if (i == " " or i == "\n" or i == "," or i == ".") and novtor == False:
            novtor = True
            Nslova += 1
        elif i != " " and i != "\n" and i != "," and i != ".":
            novtor = False
    return Nslova

# из масива делает строку
def obedinenia(A):
    tixt = ""
    for o in A:
        tixt +=o
    return tixt

# из строки делает масив
def rasiedinenia(A):
    textMas = []
    textMas += A
    return textMas

# очичает мусор с краев масива
def sistkaSKraiov(textMas):
    while True:
        A = textMas[len(textMas) - 1]
        if A == " " or A == "\n" or A == "," or A == ".":
            del (textMas[len(textMas) - 1])
        else:
            break
    del (A)

    while True:
        A = textMas[0]
        if A == " " or A == "\n" or A == "," or A == ".":
            del(textMas[0])
        else:
            break
    del(A)

    return textMas

# очичает мусор с краев строки
def sistkaTextSKraiov(A):
    return obedinenia(sistkaSKraiov(rasiedinenia(A)))

# чистка текста и с краев и в сентре (beta)
def sistkaText(A):
    return obedinenia(sistka(rasiedinenia(A)))

# чистка масива и с краев и в сентре (beta)
def sistka(A):
     return sistkaSenter(sistkaSKraiov(A))

# чистка масива в сентре (beta)
def sistkaSenter(A):
     novtor = False
     q = len(A)
     for i in range(len(A)-1):
         i+=1
         if q <=i:
             return A
         if (A[q-i] == " " or A[q-i] == "\n" or A[q-i] == "," or A[q-i] == ".") and novtor == False:
             novtor = True
         elif A[q-i] != " " and A[q-i] != "\n" and A[q-i] != "," and A[q-i] != ".":
             novtor = False
         else:
             del(A[q-i])
     return A

# разварачивает масив
def reverseMas(mas):
    mas2 = []
    for i in range(len(mas)):
        mas2.append(mas[len(mas)-1-i])
    return mas2

# разварачивает строку
def reversText(slovOq):
    return obedinenia(reverseMas(rasiedinenia(slovOq)))

# уберает начало текста по примеру
def minusSlov(slovOq, slovMq):
    if len(slovOq) == len(slovMq):
        return ""

    slovO = rasiedinenia(slovOq)
    slovM = rasiedinenia(slovMq)

    del(slovOq)
    del(slovMq)

    if len(slovO) > len(slovM):
        for i in range(len(slovM)):
            if slovO[0] != slovM[0]:
                return i
            del(slovO[0])
            del(slovM[0])
        return obedinenia(slovO)
    else:
        for i in range(len(slovO)):
            if slovO[0] != slovM[0]:
                return i
            del (slovO[0])
            del (slovM[0])
        return obedinenia(reverseMas(slovM))

# уберает начало текста в масиве по примерам
def minusSlovMas(slovOq, slovMq):
    if len(slovOq) != len(slovMq):
        return 0
    t = []
    for i in range(len(slovOq)):
        t.append(minusSlov(slovOq[i],slovMq[i]))
    return t

# уберает начало текста в масиве по одному примеру  (баг мог появиса за удаления)
def minusSlovMasV(slovOq, slovMq):
    if len(slovOq[0]) < len(slovMq):
        return 0
    t = []
    for i in range(len(slovOq)):
        t.append(minusSlov(slovOq[0],slovMq))
        del(slovOq[0])
    return t

# берот первую строчку текста
def sitezZvania(text):
    mas = []
    for i in rasiedinenia(text):
        if i != "\n":
            mas += i
        else:
            return obedinenia(mas)

# перевод сисла в техт (баги)
def mathString(text):    # баги баги и баги исправить
    mass = list(str(text))
    mas = []
    masNos = []
    G = True
    for i in range(len(mass)):
        if mass[i] != "." and G:
            mas.append(int(mass[i]))
        elif mass[i] != ".":
            masNos.append(int(mass[i]))
        else:
            G = False
    del i

    sisl = len(mas)
    slovo = []

    if sisl >= 4:
        for p in range(int((sisl-1)/3)):
            lev1 = int((len(mas)-1)/3)
            lev2 = len(mas)-lev1*3
            o = []
            for q in range(lev2):
                o.append(mas[q])
            slovo2 = []
            if lev2 == 1:
                slovo2.append(sislomas[0][o[lev2 - 1]])
            elif lev2 == 2 and o[0] == 1:
                slovo2.append(sislomas[1][o[lev2 - 1]])
            elif lev2 == 3 or lev2 == 2:
                for i in range(lev2):
                    if lev2 - i <= 2:
                        break
                    if o[i] > 0:
                        slovo2.append(sislomas[lev2 - i][o[i] - 1])

                if lev2 - i == 2 and o[lev2 - 2] == 1:
                    slovo2.append(sislomas[1][o[lev2 - 1]])
                elif lev2 - i == 2 and o[lev2 - 2] != 0:
                    slovo2.append(sislomas[2][o[lev2 - 2] - 1])
                if o[lev2 - 1] != 0 and o[lev2 - 2] != 1:
                    slovo2.append(sislomas[0][o[lev2 - 1]])
            del o
            for q in range(lev2):
                del mas[q]

            slovo.append(obeSnrob(slovo2)+" "+sisloLeval[lev1-1])
    sisl = len(mas)
    if sisl == 1:
        slovo.append(sislomas[0][mas[sisl-1]])
    elif sisl == 2 and mas[sisl-2] == 1:
        slovo.append(sislomas[1][mas[sisl - 1]])
    elif sisl == 2 and mas[sisl-2] != 0:
        slovo.append(sislomas[2][mas[sisl - 1]])
    elif sisl == 3 or sisl == 2:
        if mas[0] > 0:
            slovo.append(sislomas[3][mas[0] - 1])
        if mas[1] > 0:
            if mas[1] == 1:
                slovo.append(sislomas[1][mas[1]-1])
            else:
                slovo.append(sislomas[2][mas[1] - 1])
        if mas[2] > 0:
            slovo.append(sislomas[0][mas[2]])
    if len(masNos) != 0 and (masNos[0] != 0 or len(masNos) > 1):
        y = False
        for w in masNos:
            if w != 0:
                y = True
                break
        if y:
            slovo.append("и")
            sisl = len(masNos)
            sislRezer = len(masNos)
            if sisl >= 4:
               for p in range(int((sisl - 1) / 3)):
                    lev1 = int((len(masNos) - 1) / 3)
                    lev2 = len(masNos) - lev1 * 3
                    o = []
                    for q in range(lev2):
                        o.append(masNos[q])
                    slovo2 = []
                    if lev2 == 1:
                        slovo2.append(sislomas[0][o[lev2 - 1]])
                    elif lev2 == 2 and o[lev2 - 2] == 1:
                        slovo2.append(sislomas[1][o[lev2 - 1]])
                    elif lev2 == 3 or sisl == 2:
                        if mas[0] > 0:
                            slovo.append(sislomas[3][mas[0] - 1])
                        if mas[1] > 0:
                            if mas[1] == 1:
                                slovo.append(sislomas[1][mas[1] - 1])
                            else:
                                slovo.append(sislomas[2][mas[1] - 1])
                        if mas[2] > 0:
                            slovo.append(sislomas[0][mas[2]])

                    del o
                    for q in range(lev2):
                        del masNos[q]

                    slovo.append(obeSnrob(slovo2) + " " + sisloLeval[lev1 - 1])
        sisl = len(masNos)
        if sisl == 1:
            slovo.append(sislomas[0][masNos[sisl - 1]])
        elif sisl == 2 and masNos[sisl - 2] == 1:
            slovo.append(sislomas[1][masNos[sisl - 1]])
        elif sisl == 3 or sisl == 2:
            for i in range(sisl):
                if sisl - i <= 2:
                    break
                if masNos[i] > 0:
                    slovo.append(sislomas[sisl - i][masNos[i] - 1])

            if sisl - i == 2 and masNos[sisl - 2] == 1:
                slovo.append(sislomas[1][masNos[sisl - 1]])
            elif sisl - i == 2 and masNos[sisl - 2] != 0:
                slovo.append(sislomas[2][masNos[sisl - 2] - 1])
            if masNos[sisl - 1] != 0 and masNos[sisl - 2] != 1:
                slovo.append(sislomas[0][masNos[sisl - 1]])
        slovo.append(sisloLeval2[sislRezer-1])
    return obeSnrob(slovo)

# дополнения для mathString
def obeSnrob(mas):
    slovoV = mas[0]
    for i in range(len(mas)-1):
        slovoV += " " + mas[i+1]
    return slovoV

# обнарузения числа
def nroverkaSiselN(mas):
    novtor = 0
    mas.append("")
    for i in range(len(mas)):
        if mas[i] == '0' or mas[i] == '1' or mas[i] == '2' or mas[i] == '3' or mas[i] == '4' or mas[i] == '5' or mas[i] == '6'\
                or mas[i] == '7' or mas[i] == '8' or mas[i] == '9' or (mas[i] == '.' or mas[i] == ',') and novtor != 0:
            novtor += 1
        elif novtor != 0:
            sislo = []
            for j in range(novtor):
                sislo.append(mas[i - 1 - j])
                if j != novtor-1:
                    del mas[i - 1 - j]

            mas[i - novtor] = mathString(reverseMas(sislo))

            del(mas[len(mas)-1])
            return [mas, False]
    del (mas[len(mas)-1])
    return [mas, True]

# обнарузения числа в тексте по сиклу
def nroverkaSisel(text):
    while True:
        o = nroverkaSiselN(list(text.lower()))
        text = obedinenia(o[0])
        if o[1]:
            return obedinenia(text)

# разбевает речиня на слоги
def razdelSlogov(text):
    if len(text) == 0:
        return []
    text = nroverkaSisel(text)
    mas = list(text.lower())
    del text
    mass = [""]
    sislo = 0
    for i in mas:
        if i != ' ' and i != '.' and i != ',' and i != '\n':
            mass[sislo] += i

        if i == 'а' or i == 'о' or i == 'у' or i == 'е' or i == 'ё' or i == 'э' or i == 'и' or i == 'ы' or i == 'ю' or \
            i == 'я' or i == ' ' or i == '.' or i == ',' or i == "\n" or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':

            if (i == " " or i == "." or i == "," or i == "\n" or i == ":" or i == ";" or i == "-" or i == "—" or i == "!" or i == "?" or
                i == "(" or i == ")" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or
                i == "8" or i == "9") and mass[len(mass) - 1] == '':
                mass[sislo] += i
            elif (i == " " or i == "." or i == "," or i == "\n") and mass[len(mass)-1] != '':
                sislo += 1
                mass.append(i)

            if mass[len(mass)-1] != '':
                mass.append("")
                sislo = len(mass)-1  # sislo += 1

    if mass[len(mass)-1] == '':
        del(mass[len(mass)-1])
    return sistkaSKraiov(mass)

# разбевает речиня на слоги
def razdelSlogovGPT(masGPT):
    mas1 = []
    mas2 = []
    for i in range(len(masGPT[0])):
        mas1.append(razdelSlogov(masGPT[0][i]))
    for i in range(len(masGPT[1])):
        masV = []
        for q in range(len(masGPT[1][i])):
            masV.append(razdelSlogov(masGPT[1][i][q]))
        mas2.append(masV)
    return [mas1,mas2]

# обнарузения ошибок в складах в техт
def obnarureniaErorText(text):
    obnarureniaEror(razdelSlogov(text))

# обнарузения ошибок в складах в масиве
def obnarureniaEror(masSlog):
    nov = 0
    for text in masSlog:
        nov += obnarureniaErorV(text)
    print("Nocvtor Eroor : "+str(nov))

# обнарузения ошибок в складах доп
def obnarureniaErorV(text):
    xx = len(text) - 1
    if xx > 3:
        xx = 3
    for yy in range(len(clog[xx])):
        if clog[xx][yy] == text:
            return 0
    print("EROOR: slog : " +text)
    return 1






