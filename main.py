from Text import *
from rifmatorText import *
from gpt import *
from sintezResi import *
from geniratorSxemiGolasa import *

p = "а я што я, и што будет со мнои"
pp= "ноль один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать десять двадцать тридцать сорок пятьдесят шестьдесят семьдесят семьдесят девяносто сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот "
from datetime import datetime
start_time = datetime.now()

gp = generatorPesni("tdfgsdn asdfasf sdfgsdh", 0)

sintegGpt(gp, gen(gp), T=True)

# gen(generatorPesni("tdfgsdn asdfasf sdfgsdh", 0))
# sintez("d")0
# print("впы апбыв. пкв, ып оел  б")
# print(razdelSlogov(""))
# print(mathString(12345))
# razdelSlogovGPT([["аааа","ааа"],[["аааа","ааа"], ["аааа","ааа"], ["аааа","ааа"]]])
# gen(p)
# print(razdelSlogov(p))
# sintez(razdelSlogov(p), razdelSlogov(p), T=True)
# obnarureniaEror(razdelSlogov(pp))
# sintez(razdelSlogov(generatorPesni("tdfgsdn asdfasf sdfgsdh", 0, False)), [" "], T=True)
# print(nroverkaSisel("hnr445 gdfdfg54"))
# print(p)
# print(nodsotSlov(p))
# print(sistkaText(p))
# print(reversText(p))
# print()
# print(p+reversText(p) +"\n  ----->   "+minusSlov(p+reversText(p),p))
# print(osenkaf(p))
# print(generatorStroski(p))
# print(generatorPesni("tdfgsdn asdfasf sdfgsdh", 0, False))
# for i in range(1):
#     print(generatorStroski("d"))
# print(zanret(p))
# print(sisloSlov(p))




#print("f")

#import torch
#import deepspeed.ops.sparse_attention.sparse_attn_op


#pip install triton==0.2.3


print(datetime.now() - start_time)
