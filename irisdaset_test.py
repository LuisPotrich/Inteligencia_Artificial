# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:23:30 2018

@author: Usuario
"""
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()


X = iris.data[:, :4]  # we only take the first two features.
y = iris.target
print(X)
x_min, x_max = X[:, 3].min() - .5, X[:, 3].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 3], X[:, 1], c=y, cmap=plt.cm.Set1,edgecolor='k')
plt.xlabel('petal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())