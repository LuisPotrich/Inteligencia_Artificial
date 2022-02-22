# -*- coding: utf-8 -*-

import random   #importa a biblioteca Random
import operator #importa os operadores
import matplotlib.pyplot as plt
import numpy as np #Não sei o que faz

def fitness(a,b,c,x):
    y = a * x ** 2 + b * x + c
    return y

def generateNumber():
    return random.uniform(-10,10) # Gera um número aleatório de - 10 a 10

# Criando a primeira população com números aleatórios de -10 a 10
def generateFirstPopulation(sizePopulation):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateNumber())
        i+=1
    return population

# Execução do fitness com a primeira geração criada. O retorno dessa função é o que não entendi direito,entendi que o retorno é um número aleatório dentro da resposta do fitness
def computePerfPopulation(population):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(a,b,c,indivual)
    return sorted(populationPerf.items() , key = operator.itemgetter(1))
    
# 
def selectFromPopulation(populationSorted, best_sample, lucky_few):
    nextGeneration = []
    
    for i in range(best_sample):
        if < len(populationSorted):
            nextGeneration.append(populationSorted[i][0])
    for i 
