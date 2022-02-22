# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:38:55 2018

@author:
"""

import random
import operator
import time
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
#%%
size_population = 100
best_sample = 20
lucky_few = 20
number_of_child = 5
number_of_generation = 50
chance_of_mutation = 5
temps1 = time.time()
#%%
def fitness(individuo, dado, resposta):
    f = 0
    for i in range(4):
        f+= individuo[i] * dado[i]
    
    y = (f - resposta) ** 2
    y = 1/y
    
    return y
#%%
def generateIndividuo():
    individuo = [random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)]
    return individuo
#%% 
def generateFirstPopulation(sizePopulation):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateIndividuo())
        i+=1
    return population
#%%
def computePerfPopulation(population):
    populationPerf = {}
    for individual in population:
        populationPerf[individual]=fitness(individual,dado,resposta)
    return sorted(populationPerf.items(), key = operator.itemgetter(1), reverse=True) 
#%%
def selectFromPopulation(populationSorted, best_sample, lucky_few):
	nextGeneration = []
	for i in range(best_sample):
		nextGeneration.append(populationSorted[i][0])
	for i in range(lucky_few):
		nextGeneration.append(random.choice(populationSorted)[0])
	random.shuffle(nextGeneration)
	return nextGeneration
#%%
def createChild(individual1, individual2):
	child = []
	for i in range(len(individual1)):
		if (int(100 * random.random()) < 50):
			child += individual1[i]
		else:
			child += individual2[i]
	return child