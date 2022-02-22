# -*- coding: utf-8 -*-

import random
import operator
import matplotlib.pyplot as plt
import numpy as np

def fitness(a,b,c,number):
    y = a * number ** 2 + b * number + c
    return y

def generateNumber():
    return random.uniform(-15,15)

def generateFirstPopulation(sizePopulation):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateNumber())
        i+=1
    return population

def computePerfPopulation(population):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(a, b, c, individual)
    return sorted(populationPerf.items(), key = operator.itemgetter(1))

def selectFromPopulation(populationSorted, best_sample, lucky_few):
    nextGeneration = []
        
    for i in range(best_sample):
        if i < len(populationSorted):
            nextGeneration.append(populationSorted[i][0])
    for i in range(lucky_few):
        nextGeneration.append(random.choice(populationSorted)[0])
    random.shuffle(nextGeneration)
    return nextGeneration

def createChild(individual1, individual2):
    child = (individual1 + individual2)/2
    return child

def createChildren(breeders, number_of_child):
    nextPopulation = []
    for i in range(int(len(breeders)/2)):
        for j in range(number_of_child):
            nextPopulation.append(createChild(breeders[i], breeders[len(breeders)-1 - i]))
    return nextPopulation

def mutateNumber(number):
    number += random.uniform(-1,1)
    return number

def mutatePopulation(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random() * 100 < chance_of_mutation:
            population[i] = mutateNumber(population[i])
    return population

def nextGeneration(firstGeneration, best_sample, lucky_few, number_of_child, chance_of_mutation):
    populationSorted = computePerfPopulation(firstGeneration)
    nextBreeders = selectFromPopulation(populationSorted, best_sample, lucky_few)
    nextPopulation = createChildren(nextBreeders, number_of_child)
    nextGeneration = mutatePopulation(nextPopulation, chance_of_mutation)
    return nextGeneration

def multipleGeneration(number_of_generation, size_population, best_sample, lucky_few, number_of_child, chance_of_mutation):
    historic = []
    historic.append(generateFirstPopulation(size_population))
    for i in range(number_of_generation):
        historic.append(nextGeneration(historic[i], best_sample, lucky_few, number_of_child, chance_of_mutation))
    return historic

def printSimpleResult(historic, number_of_generation):
    result = getListBestIndividualFromHistorique(historic)[number_of_generation-1]
    print("solução: " + str(result))
    
def getBestIndividualFromPopulation(population):
    return computePerfPopulation(population)[0]

def getListBestIndividualFromHistorique(historic):
    bestIndividuals = []
    for population in historic:
        bestIndividuals.append(getBestIndividualFromPopulation(population)[1])
    return bestIndividuals

def evolutionBestFitness(historic):
	plt.axis([0,len(historic),0,105])
	plt.title("Melhores fitness")
	
	evolutionFitness = []
	for population in historic:
		evolutionFitness.append(getBestIndividualFromPopulation(population)[1])
	plt.plot(evolutionFitness)
	plt.ylabel('fitness best individual')
	plt.xlabel('generation')
	plt.show()

def evolutionAverageFitness(historic, size_population):
	plt.axis([0,len(historic),0,105])
	plt.title("Fitness média")
	
	evolutionFitness = []
	for population in historic:
		populationPerf = computePerfPopulation(population)
		averageFitness = 0
		for individual in populationPerf:
			averageFitness += individual[1]
		evolutionFitness.append(averageFitness/size_population)
	plt.plot(evolutionFitness)
	plt.ylabel('Average fitness')
	plt.xlabel('generation')
	plt.show()

def showGraph(a,b,c, historic):
    x = np.linspace(-15,15,400)
        
    plt.title("Gráfico da função " + str(a) + "*x^2 + " + str(b) + "*x + " + str(c))    
    plt.plot(x, a * pow(x,2) + b * x + c)
    
    minimum = - b / (2*a)
    print("mínimo real: " + str(fitness(a,b,c,minimum)))

#variables
    
a = 10 * random.random()
b = random.uniform(-20,20)
c = random.uniform(-20,20)
size_population = 100
best_sample = 20
lucky_few = 20
number_of_child = 5 
number_of_generation = 50
chance_of_mutation = 5


#program

if ((best_sample + lucky_few) / 2 * number_of_child != size_population):
	print ("population size not stable")
else:
	historic = multipleGeneration(number_of_generation, size_population, best_sample, lucky_few, number_of_child, chance_of_mutation)
	
	printSimpleResult(historic, number_of_generation)
	
	#evolutionBestFitness(historic)
    
	#evolutionAverageFitness(historic, size_population)
    
	showGraph(a,b,c, historic)