"""
========================
Fuzzy c-means clustering
========================

Fuzzy logic principles can be used to cluster multidimensional data, assigning
each point a *membership* in each cluster center from 0 to 100 percent. This
can be very powerful compared to traditional hard-thresholded clustering where
every point is assigned a crisp, exact label.

Fuzzy c-means clustering is accomplished via ``skfuzzy.cmeans``, and the
output from this function can be repurposed to classify new data according to
the calculated clusters (also known as *prediction*) via
``skfuzzy.cmeans_predict``

Data generation and setup
-------------------------

In this example we will first undertake necessary imports, then define some
test data to work with.
from __future__ import division, print_function
"""
#%% Imports
import csv
import numpy as np
import skfuzzy as fuzz


#%%
colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

dados = [] 

with open("winequality-red.csv") as arquivocsv:
    ler = csv.DictReader(arquivocsv, delimiter=",")
    for linha in ler:
        for chave, valor in linha.items():
            valor = valor.split(';')
            valorf = list(map(float,valor))
            dados.append(valorf)
           
data2 = np.array(dados)[:,:]




#%%
var0 = data2[:, 0]
var1 = data2[:, 1]
var2 = data2[:, 2]
var3 = data2[:, 3]
var4 = data2[:, 4]
var5 = data2[:, 5]
var6 = data2[:, 6]
var7 = data2[:, 7]
var8 = data2[:, 8]
var9 = data2[:, 9]
var10 = data2[:, 10]
label = data2[:, 11]

alldata = np.vstack((var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10))# duas linha de n elementos




#%%
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(alldata, 6, 2, error=0.005, maxiter=1000, init=None)
cluster_membership = np.argmax(u, axis=0)
ei = sorted(cluster_membership, key=int)

grupo1=[]
grupo2=[]
grupo3=[]
grupo4=[]
grupo5=[]
grupo6=[]

#separação dos centros que representam as classificações

for i in range(len(data2)):
    if data2[i,11]==3:
        grupo1.append(np.array(data2[i,:]))
    if data2[i,11]==4:
        grupo2.append(np.array(data2[i,:]))
    if data2[i,11]==5:
        grupo3.append(np.array(data2[i,:]))
    if data2[i,11]==6:
        grupo4.append(np.array(data2[i,:]))
    if data2[i,11]==7:
        grupo5.append(np.array(data2[i,:]))
    if data2[i,11]==8:
        grupo6.append(np.array(data2[i,:]))
        
        #centros que representam as classificações separados em variáveis
a = (sum(grupo1)/len(grupo1)) #3
b = (sum(grupo2)/len(grupo2)) #4
c = (sum(grupo3)/len(grupo3)) #5
d = (sum(grupo4)/len(grupo4)) #6
e = (sum(grupo5)/len(grupo5)) #7
f = (sum(grupo6)/len(grupo6)) #8


trem1 = []
trem2 = []
trem3 = []
trem4 = []
trem5 = []
trem6 = []
vetorlabel = []
vetorlabel2 = []
score1 = []
score2 = []
score3 = []
scoreindefinido = []
# descobrindo a qual classificação cada amostra pertence usando a característica alcool
for i in range(len(data2)):
        trem1.append(np.array(abs(data2[i,10]-a[10]))) 
        trem2.append(np.array(abs(data2[i,10]-b[10])))
        trem3.append(np.array(abs(data2[i,10]-c[10])))
        trem4.append(np.array(abs(data2[i,10]-d[10])))
        trem5.append(np.array(abs(data2[i,10]-e[10])))
        trem6.append(np.array(abs(data2[i,10]-f[10])))

        if trem3[i] < trem1[i] and trem3[i] < trem2[i] and trem3[i] < trem4[i] and trem3[i] < trem5[i] and trem3[i] < trem6[i]:
            vetorlabel.append(5)
        elif trem1[i] < trem2[i] and trem1[i] < trem3[i] and trem1[i] < trem4[i] and trem1[i] < trem5[i] and trem1[i] < trem6[i]:
            vetorlabel.append(3)
        elif trem2[i] < trem1[i] and trem2[i] < trem3[i] and trem2[i] < trem4[i] and trem2[i] < trem5[i] and trem2[i] < trem6[i]:
            vetorlabel.append(4)
        elif trem4[i] < trem1[i] and trem4[i] < trem2[i] and trem4[i] < trem3[i] and trem4[i] < trem5[i] and trem4[i] < trem6[i]:
            vetorlabel.append(6)
        elif trem5[i] < trem1[i] and trem5[i] < trem2[i] and trem5[i] < trem3[i] and trem5[i] < trem4[i] and trem5[i] < trem6[i]:
            vetorlabel.append(7)  
        elif trem6[i] < trem1[i] and trem6[i] < trem2[i] and trem6[i] < trem3[i] and trem6[i] < trem4[i] and trem6[i] < trem5[i]:
            vetorlabel.append(8) 
        else:
            vetorlabel2.append(1)
            

 #comparando o resultado do vetorlabel com a label real e, assim, criando 3 scores
for i in range(len(data2)):
    if data2[i,11]==3 and vetorlabel[i] == 3:
        score1.append(1)  
    elif data2[i,11]==4 and vetorlabel[i] == 4:
        score1.append(1)
    elif data2[i,11]==5 and vetorlabel[i] == 5:
        score2.append(2)
    elif data2[i,11]==6 and vetorlabel[i] == 6:
        score2.append(2)
    elif data2[i,11]==7 and vetorlabel[i] == 7:
        score2.append(2)
    elif data2[i,11]==8 and vetorlabel[i] == 8:
        score3.append(3)
    else:
        scoreindefinido.append(0)
        
ruim = len(score1)
bom = len(score2)
deveras = len(score3)
errrrrou = len(scoreindefinido)

#for i in range(len(data2)):
#    if vetorlabel[i]==3:
#        score1.append(1)  
#    elif vetorlabel[i]==4:
#        score1.append(1)
#    elif vetorlabel[i]==5:
#        score2.append(2)
#    elif vetorlabel[i]==6:
#        score2.append(2)
#    elif vetorlabel[i]==7:
#        score2.append(2)
#    elif vetorlabel[i]==8:
#        score3.append(3)
#    else:
#        scoreindefinido.append(9)
#        
#ruim = len(score1)
#bom = len(score2)
#deveras = len(score3)
#errrrrou = len(scoreindefinido)
        
print('Classificação dos vinhos de acordo com a característica "álcool":')   
print('Ruim:', ruim )
print('Bom:', bom )
print('Muito Bom:', deveras)
print('IA Errou:', errrrrou)

#trem7 = []
#trem8 = []
#trem9 = []
#trem10 = []
#trem11 = []
#trem12 = []
#vetorlabel3 = []
#vetorlabel4 = []
#score4 = []
#score5 = []
#score6 = []
#scoreindef = []
## descobrindo a qual classificação cada amostra pertence usando a característica alcool
#for i in range(len(data2)):
#        trem7.append(np.array(abs(data2[i,1]-a[1]))) 
#        trem8.append(np.array(abs(data2[i,1]-b[1])))
#        trem9.append(np.array(abs(data2[i,1]-c[1])))
#        trem10.append(np.array(abs(data2[i,1]-d[1])))
#        trem11.append(np.array(abs(data2[i,1]-e[1])))
#        trem12.append(np.array(abs(data2[i,1]-f[1])))
#
#        if trem7[i] < trem8[i] and trem7[i] < trem9[i] and trem7[i] < trem10[i] and trem7[i] < trem11[i] and trem7[i] < trem12[i]:
#            vetorlabel3.append(5)
#        elif trem8[i] < trem9[i] and trem8[i] < trem10[i] and trem8[i] < trem11[i] and trem8[i] < trem12[i] and trem8[i] < trem7[i]:
#            vetorlabel3.append(3)
#        elif trem9[i] < trem7[i] and trem9[i] < trem8[i] and trem9[i] < trem10[i] and trem9[i] < trem11[i] and trem9[i] < trem12[i]:
#            vetorlabel3.append(4)
#        elif trem10[i] < trem7[i] and trem10[i] < trem8[i] and trem10[i] < trem9[i] and trem10[i] < trem11[i] and trem10[i] < trem12[i]:
#            vetorlabel3.append(6)
#        elif trem11[i] < trem7[i] and trem11[i] < trem8[i] and trem11[i] < trem9[i] and trem11[i] < trem10[i] and trem11[i] < trem12[i]:
#            vetorlabel3.append(7)  
#        elif trem12[i] < trem7[i] and trem12[i] < trem8[i] and trem12[i] < trem9[i] and trem12[i] < trem10[i] and trem12[i] < trem11[i]:
#            vetorlabel3.append(8) 
#        else:
#            vetorlabel4.append(1)
#            
#
# #comparando o resultado do vetorlabel com a label real e, assim, criando 3 scores
#for i in range(len(data2)):
#    if data2[i,11]==3 and vetorlabel3[i] == 3:
#        score4.append(1)  
#    elif data2[i,11]==4 and vetorlabel3[i] == 4:
#        score4.append(1)
#    elif data2[i,11]==5 and vetorlabel3[i] == 5:
#        score5.append(2)
#    elif data2[i,11]==6 and vetorlabel3[i] == 6:
#        score5.append(2)
#    elif data2[i,11]==7 and vetorlabel3[i] == 7:
#        score5.append(2)
#    elif data2[i,11]==8 and vetorlabel3[i] == 8:
#        score6.append(3)
#    else:
#        scoreindef.append(0)
#        
#ruimm = len(score4)
#bomm = len(score5)
#devers = len(score6)
#errou = len(scoreindef)
#
##for i in range(len(data2)):
##    if vetorlabel[i]==3:
##        score1.append(1)  
##    elif vetorlabel[i]==4:
##        score1.append(1)
##    elif vetorlabel[i]==5:
##        score2.append(2)
##    elif vetorlabel[i]==6:
##        score2.append(2)
##    elif vetorlabel[i]==7:
##        score2.append(2)
##    elif vetorlabel[i]==8:
##        score3.append(3)
##    else:
##        scorei.append(9)     
#print('Classificação dos vinhos de acordo com a característica "densidade":')   
#print('Ruim:', ruimm )
#print('Bom:', bomm )
#print('Muito Bom:', devers)
#print('IA Errou:', errou)
#
#
#
#
#
#
#
#for i in range(len(data2)):
#        trem7.append(np.array(abs(data2[i,7]-a[7]))) 
#        trem8.append(np.array(abs(data2[i,7]-b[7])))
#        trem9.append(np.array(abs(data2[i,7]-c[7])))
#        trem10.append(np.array(abs(data2[i,7]-d[7])))
#        trem11.append(np.array(abs(data2[i,7]-e[7])))
#        trem12.append(np.array(abs(data2[i,7]-f[7])))
#
#        if trem7[i] < trem8[i] and trem7[i] < trem9[i] and trem7[i] < trem10[i] and trem7[i] < trem11[i] and trem7[i] < trem12[i]:
#            vetorlabel3.append(5)
#        elif trem8[i] < trem9[i] and trem8[i] < trem10[i] and trem8[i] < trem11[i] and trem8[i] < trem12[i] and trem8[i] < trem7[i]:
#            vetorlabel3.append(3)
#        elif trem9[i] < trem7[i] and trem9[i] < trem8[i] and trem9[i] < trem10[i] and trem9[i] < trem11[i] and trem9[i] < trem12[i]:
#            vetorlabel3.append(4)
#        elif trem10[i] < trem7[i] and trem10[i] < trem8[i] and trem10[i] < trem9[i] and trem10[i] < trem11[i] and trem10[i] < trem12[i]:
#            vetorlabel3.append(6)
#        elif trem11[i] < trem7[i] and trem11[i] < trem8[i] and trem11[i] < trem9[i] and trem11[i] < trem10[i] and trem11[i] < trem12[i]:
#            vetorlabel3.append(7)  
#        elif trem12[i] < trem7[i] and trem12[i] < trem8[i] and trem12[i] < trem9[i] and trem12[i] < trem10[i] and trem12[i] < trem11[i]:
#            vetorlabel3.append(8) 
#        else:
#            vetorlabel4.append(1)
#            
#
# #comparando o resultado do vetorlabel com a label real e, assim, criando 3 scores
#for i in range(len(data2)):
#    if data2[i,11]==3 and vetorlabel3[i] == 3:
#        score4.append(1)  
#    elif data2[i,11]==4 and vetorlabel3[i] == 4:
#        score4.append(1)
#    elif data2[i,11]==5 and vetorlabel3[i] == 5:
#        score5.append(2)
#    elif data2[i,11]==6 and vetorlabel3[i] == 6:
#        score5.append(2)
#    elif data2[i,11]==7 and vetorlabel3[i] == 7:
#        score5.append(2)
#    elif data2[i,11]==8 and vetorlabel3[i] == 8:
#        score6.append(3)
#    else:
#        scoreindef.append(0)
#        
#ruimm = len(score4)
#bomm = len(score5)
#devers = len(score6)
#errou = len(scoreindef)
#
##for i in range(len(data2)):
##    if vetorlabel[i]==3:
##        score1.append(1)  
##    elif vetorlabel[i]==4:
##        score1.append(1)
##    elif vetorlabel[i]==5:
##        score2.append(2)
##    elif vetorlabel[i]==6:
##        score2.append(2)
##    elif vetorlabel[i]==7:
##        score2.append(2)
##    elif vetorlabel[i]==8:
##        score3.append(3)
##    else:
##        scorei.append(9)     
#print('Classificação dos vinhos de acordo com a característica "fixed acidity":')   
#print('Ruim:', ruimm )
#print('Bom:', bomm )
#print('Muito Bom:', devers)
#print('IA Errou:', errou)





















