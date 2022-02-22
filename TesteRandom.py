# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:50:14 2018

@author: aluno
"""
import random

"Gera um número aleatório de 0 a 100"
#random.random()
#letter = int(100*random.random())

"Gera um caracter aleatório de a até z - utilizando a tabela ASCII"
#letter = chr(97 + int(26 * random.random()))
#print(letter)

"Gera um número aleatório de 0 até 9 - utilizando a tabela ASCII"
numero = chr(48 + int(10 * random.random()))
print(numero)