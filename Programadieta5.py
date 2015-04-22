# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:35:54 2015

@author: Felipe
"""

import matplotlib.pyplot	as plt

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



usuario=open("usuario_semana.csv")
y=usuario.readlines()
calpadr= tabela_alimentos.values()
#print (calpadr)

tabela_usuario={}

caltotal=0
protototal=0
gorduratotal=0
carbototal=0

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
    caltotal+=calpadr
    protototal+=protopadr
    gorduratotal+=gordpadr
    carbototal+=carbpadr
    

    
    
tabela_usuario1={}

caltotal1=0
protototal1=0
gorduratotal1=0
carbototal1=0

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
    
    caltotal1+=calpadr
    protototal1+=protopadr
    gorduratotal1+=gordpadr
    carbototal1+=carbpadr
    

tabela_usuario2={}

caltotal2=0
protototal2=0
gorduratotal2=0
carbototal2=0

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
    caltotal2+=calpadr
    protototal2+=protopadr
    gorduratotal2+=gordpadr
    carbototal2+=carbpadr

tabela_usuario3={}

caltotal3=0
protototal3=0
gorduratotal3=0
carbototal3=0
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
    caltotal3+=calpadr
    protototal3+=protopadr
    gorduratotal3+=gordpadr
    carbototal3+=carbpadr
    
caltotal4=0
protototal4=0
gorduratotal4=0
carbototal4=0
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
    caltotal4+=calpadr
    protototal4+=protopadr
    gorduratotal4+=gordpadr
    carbototal4+=carbpadr
    
tabela_usuario5={}
caltotal5=0
protototal5=0
gorduratotal5=0
carbototal5=0
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
    caltotal5+=calpadr
    protototal5+=protopadr
    gorduratotal5+=gordpadr
    carbototal5+=carbpadr

tabela_usuario6={}
caltotal6=0
protototal6=0
gorduratotal6=0
carbototal6=0
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
    caltotal6+=calpadr
    protototal6+=protopadr
    gorduratotal6+=gordpadr
    carbototal6+=carbpadr

   

for p in y[1:2]:
    x=p.strip().split(",")
    print(x)
    idade=int(x[1])
    peso=int(x[2])
    sexo=x[3]
    altura=int(x[4])
def TMB(peso,altura,idade):
   return (88.36+(13.4*peso)+(4.8*altura)-(5.7*idade))*1.725
print(TMB(peso,altura,idade))
q=TMB(peso,altura,idade)
listalimpa=[caltotal,caltotal1,caltotal2,caltotal3,caltotal4,caltotal5,caltotal6]
print(listalimpa)
listalimpa1=[protototal,protototal1,protototal2,protototal3,protototal4,protototal5,protototal6]
print(listalimpa1)
listalimpa2=[gorduratotal,gorduratotal1,gorduratotal2,gorduratotal3,gorduratotal4,gorduratotal5,gorduratotal6]
print(listalimpa2)
listalimpa3=[carbototal,carbototal1,carbototal2,carbototal3,carbototal4,carbototal5,carbototal6]
print(listalimpa3)
listadia=[1,2,3,4,5,6,7]
listatmb=[q,q,q,q,q,q,q]


plt.plot(listadia,listalimpa)
plt.plot(listadia,listatmb)
plt.plot(listadia,listalimpa1)
plt.plot(listadia,listalimpa2)
plt.plot(listadia,listalimpa3)
plt.title("Consumo de Calorias,Proteínas,Carboidratos e Gorduras Diarias")
plt.ylabel("Consumo")
plt.xlabel("Dias")
plt.axis(min(listadia), max(listadia), 0, 5000)
plt.show()

plt.plot(listadia,listalimpa1)
plt.axis(min(listadia), max(listadia), 0, 250)
plt.show()

plt.plot(listadia,listalimpa2)
plt.axis(min(listadia), max(listadia), 0, 250)
plt.show()

plt.plot(listadia,listalimpa3)
plt.axis(min(listadia), max(listadia), 0, 500)
plt.show()



#Carboidratos equivale a linha roxa
#Calorias equivale a linha azul
#TMB equivale a linha verde escura
#Proteína equivale a linha vermelha
#Gordura equivale a linha verde claro
