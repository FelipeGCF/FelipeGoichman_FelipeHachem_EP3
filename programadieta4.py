# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:32:35 2015

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
#listacal=[]
#listacal1=[]
#listacal2=[]
#listacal3=[]
#listacal4=[]
#listacal5=[]
#listacal6=[]
#listaprot=[]
#listaprot1=[]
#listaprot2=[]
#listaprot3=[]
#listaprot4=[]
#listaprot5=[]
#listaprot6=[]
#listacarb=[]
#listacarb1=[]
#listacarb2=[]
#listacarb3=[]
#listacarb4=[]
#listacarb5=[]
#listacarb6=[]
#listagord=[]
#listagord1=[]
#listagord2=[]
#listagord3=[]
#listagord4=[]
#listagord5=[]
#listagord6=[]


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
    listalimpa.append(calpadr)
    print(listalimpa)
    x=sum (listalimpa)
    print(x)
    print(tabela_usuario)
    
    #listacal.append(calpadr)
    #print(listacal)
    #c=sum (listacal)
    #print(cal)
    
  #  listaprot.append(protopadr)
   # print(protopadr)
    #p=sum (listaprot)
    #print(prot)
    
    #listacarb.append(carbpadr)
    #print(carbpadr)
    #c=sum (listacarb)
    #print(carb)
    
   # listagord.append(gordpadr)
    #print(gordpadr)
    #g=sum(listagord)
    #print(gord)
    
    
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
    listalimpa1.append(calpadr)
    print(listalimpa1)
    q=sum (listalimpa1)
    print(q)
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
    listalimpa2.append(calpadr)
    print(listalimpa2)
    w=sum (listalimpa2)
    print(w)
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
    listalimpa3.append(calpadr)
    print(listalimpa3)
    r=sum (listalimpa3)
    print(r)
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
    listalimpa4.append(calpadr)
    print(listalimpa4)
    t=sum (listalimpa4)
    print(t)
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
    listalimpa5.append(calpadr)
    print(listalimpa5)
    s=sum (listalimpa5)
    print(s)
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
    listalimpa6.append(calpadr)
    print(listalimpa6)
    f=sum (listalimpa6)
    print(f)
    print(tabela_usuario6)

#def TMB(peso,altura,idade):
   # return [88.36+(13.4*peso)+(4.8*altura)–(5.7*idade)]*1.725
#Resposta=TMB(70,167,30)
#print(Resposta)    
    