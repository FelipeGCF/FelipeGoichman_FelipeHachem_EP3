# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:15:51 2015

@author: Felipe
"""

alimentos=open("alimentos.csv")
x=alimentos.readlines()
print(x)

tabela_calorias = {}
x=[]
y=[]
for l in x[1:]:
    pedacos = l.strip().split(",")
    cal = float(l[2])
    prot=float(l[3])
    carb=float(l[4])
    gord=float(l[5])
    massa = float(l[1])
    nome = l[0]
    print(pedacos)
    calpad=(cal/massa)
    protpad=(prot/massa)
    carbpad=(carb/massa)
    gordpad=(gord/massa)
    tabela_calorias[l]+=calpad
    tabela_calorias[l]+=protpad
    tabela_calorias[l]+=carbpad
    tabela_calorias[l]+=gordpad
    
    print(tabela_calorias)    
    # montar o dicionario que vai ser tabela de calorias
    



usuario=open("usuario_semana.csv")
y=usuario.readlines()


parte=y[1].strip().split(",")
for p in parte:
    print(p)


for l in y[3:]: 
    for pedaco in l.strip().split(","):
        print(pedaco)


    