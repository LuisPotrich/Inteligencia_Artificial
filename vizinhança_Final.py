

import operator
import random
import time
import numpy as np  #Contas numericas
import matplotlib.pyplot as plt  #Plot
import skfuzzy as fuzz    #Logica fuzzy



colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# Define three cluster centers    Chutado
centers = [[4, 2],
           [1, 7],
           [5, 6]]

# Define three cluster sigmas in x and y, respectively        Desvio padraoo
sigmas = [[0.8, 0.3],
          [0.3, 0.5],
          [1.1, 0.7]]

#%% Generate test data

np.random.seed(42)  # Set seed for reproducibility    Definindo a semente de randomicidade
xpts = []#np.zeros(1)
ypts = []#np.zeros(1)
labels = []#np.zeros(1)
for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
    xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))  
    ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
    labels = np.hstack((labels, np.ones(200) * i))


#%% Visualize the test data   
fig0, ax0 = plt.subplots()
for label in range(3):
    ax0.plot(xpts[labels == label], ypts[labels == label], '.',
             color=colors[label])
ax0.set_title('Test data')

#misturando os dados
alldata = np.zeros((600,4))

for i in range(600):
    alldata[i,0] = xpts[i]
    alldata[i,1] = ypts[i]
    alldata[i,2] = np.round(random.random()*2)
    alldata[i,3] = labels[i]


#%% Visualize the Clusters misturados
fig1, ax1 = plt.subplots()
for label in range(3):
    ax1.plot(xpts[alldata[:,2] == label], ypts[alldata[:,2] == label], '.',
             color=colors[label])
ax1.set_title('Clusters misturados')


#Seprando os clusters

k = 5
interacoes = 50
count = 0

while (count <= interacoes): 
    count += 1
    elabel = np.zeros(600)  #nova label
    for i in range(len(ypts)):
        resposta = np.zeros((600,3))
        for j in range(len(ypts)):
            #distância 
            dist = ((ypts[j]-ypts[i])**(2) + (xpts[i]-xpts[j])**(2))**(1/2)
            resposta[j,0] = dist
            resposta[j,1] = alldata[j,2]
            resposta[j,2] = alldata[j,3]
        ordenada = sorted(resposta[:,0]) #distancia ordenada
        score0 = 0
        score1 = 0
        score2 = 0
        for j in range(k):
            for q in range(len(ypts)):
                if(ordenada[j+1] == resposta[q,0]):
                    if(resposta[q,1] == 0):
                        score0 += 1
                    elif(resposta[q,1] == 1):
                        score1 += 1
                    else:
                        score2 += 1
        if(score0 > score1):
            if(score0 > score2):
                elabel[i] = 0
        if(score0 < score1):
            if(score1 > score2):
                elabel[i] = 1
        if(score0 < score1):
            if(score0 < score2):
                elabel[i] = 2
        if(score0 == score1):
            elabel[i] = np.round(random.random())
        if(score1 == score2):
            elabel[i] = np.round(random.random()+1)
        if(score0 == score2):
            if(random.random()<0.5):
                elabel[i] = 0
            else:
                elabel[i] = 2
    alldata[:,2] = elabel[:]
    # print(count)


#%% Visualize the test data   
fig2, ax2 = plt.subplots()
for label in range(3):
    ax2.plot(xpts[alldata[:,2] == label], ypts[alldata[:,2] == label], '.',
             color=colors[label])
ax2.set_title('Clusters separados.')











