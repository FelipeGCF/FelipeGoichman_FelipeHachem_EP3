# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:39:33 2015

@author: Felipe
"""

alimentos=open("alimentos.csv")
x=alimentos.readlines()
#print(x)

tabela_alimentos = {}

for l in x[1:]:
    pedacos = l.strip().split(",")
    cal = float(pedacos[2])
    prot=float(pedacos[3])
    carb=float(pedacos[4])
    gord=float(pedacos[5])
    massa = float(pedacos[1])
    nome = pedacos[0]
    calpad=(cal/massa)
    protpad=(prot/massa)
    carbpad=(carb/massa)
    gordpad=(gord/massa)
    tabela_alimentos[pedacos[0]] = []
    tabela_alimentos[pedacos[0]]+=[calpad]
    tabela_alimentos[pedacos[0]]+=[protpad]
    tabela_alimentos[pedacos[0]]+=[carbpad]
    tabela_alimentos[pedacos[0]]+=[gordpad]
    
    #print(tabela_alimentos)    
    #montar o dicionario que vai ser tabela de alimentos

listalimpa=[]
listalimpa1=[]
listalimpa2=[]
listalimpa3=[]
listalimpa4=[]
listalimpa5=[]
listalimpa6=[]
usuario=open("usuario_semana.csv")
y=usuario.readlines()
calpadr= tabela_alimentos.values()
print (calpadr)

tabela_usuario={}

for p in y[3:11]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso
    tabela_usuario[parte[0]]=[]
    tabela_usuario[parte[0]]+=[alimento] 
    tabela_usuario[parte[0]]+=[calpadr]
    tabela_usuario[parte[0]]+=[protopadr]
    tabela_usuario[parte[0]]+=[carbpadr]
    tabela_usuario[parte[0]]+=[gordpadr]
    
    print(tabela_usuario)
    
tabela_usuario1={}

for p in y[11:19]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso
    
    tabela_usuario1[parte[0]]=[]
    tabela_usuario1[parte[0]]+=[alimento] 
    tabela_usuario1[parte[0]]+=[calpadr]
    tabela_usuario1[parte[0]]+=[protopadr]
    tabela_usuario1[parte[0]]+=[carbpadr]
    tabela_usuario1[parte[0]]+=[gordpadr]
    
    print(tabela_usuario1)

tabela_usuario2={}

for p in y[19:27]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso

    tabela_usuario2[parte[0]]=[]
    tabela_usuario2[parte[0]]+=[alimento] 
    tabela_usuario2[parte[0]]+=[calpadr]
    tabela_usuario2[parte[0]]+=[protopadr]
    tabela_usuario2[parte[0]]+=[carbpadr]
    tabela_usuario2[parte[0]]+=[gordpadr]
    
    print(tabela_usuario2)

tabela_usuario3={}

for p in y[27:35]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso

    tabela_usuario3[parte[0]]=[]
    tabela_usuario3[parte[0]]+=[alimento] 
    tabela_usuario3[parte[0]]+=[calpadr]
    tabela_usuario3[parte[0]]+=[protopadr]
    tabela_usuario3[parte[0]]+=[carbpadr]
    tabela_usuario3[parte[0]]+=[gordpadr]
    
    print(tabela_usuario3)

tabela_usuario4={}

for p in y[35:43]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso
    
    tabela_usuario4[parte[0]]=[]
    tabela_usuario4[parte[0]]+=[alimento] 
    tabela_usuario4[parte[0]]+=[calpadr]
    tabela_usuario4[parte[0]]+=[protopadr]
    tabela_usuario4[parte[0]]+=[carbpadr]
    tabela_usuario4[parte[0]]+=[gordpadr]
    
    print(tabela_usuario4)
    
tabela_usuario5={}

for p in y[43:51]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso

    tabela_usuario5[parte[0]]=[]
    tabela_usuario5[parte[0]]+=[alimento] 
    tabela_usuario5[parte[0]]+=[calpadr]
    tabela_usuario5[parte[0]]+=[protopadr]
    tabela_usuario5[parte[0]]+=[carbpadr]
    tabela_usuario5[parte[0]]+=[gordpadr]
    
    print(tabela_usuario5)

tabela_usuario6={}

for p in y[51:59]:
    parte=p.strip().split(",")
    alimento=str(parte[1])
    peso=float(parte[2])
    data=str(parte[0])
    calpadr= (tabela_alimentos[alimento][0])*peso
    protopadr= (tabela_alimentos[alimento][1])*peso
    carbpadr= (tabela_alimentos[alimento][2])*peso
    gordpadr= (tabela_alimentos[alimento][3])*peso

    tabela_usuario6[parte[0]]=[]
    tabela_usuario6[parte[0]]+=[alimento] 
    tabela_usuario6[parte[0]]+=[calpadr]
    tabela_usuario6[parte[0]]+=[protopadr]
    tabela_usuario6[parte[0]]+=[carbpadr]
    tabela_usuario6[parte[0]]+=[gordpadr]
    
    print(tabela_usuario6)
    