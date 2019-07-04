#from tkinter import *
import numpy
#import sys
#import os
#window = Tk()
#window.title("K means Algorithm")
#window.geometry('250x250')
#window.config(background='blue')
#lbl = Label(window, text="K-means Algorithm")
#lbl.pack(side=TOP)
#def clicked():
 #   os.system('kmeans.py')
#btn = Button(window, text="Check", command=clicked)
#btn.config(height=2,width=20,bg='red')
#btn.pack(side=LEFT)
#window.mainloop()

#if ......:RAISED GROOVE SUNKEN RIDGE

#Label(text="one").pack()

#separator = Frame(height=10, bd=100, relief=GROOVE)
#separator.pack(fill=X, padx=5, pady=5)

#Label(text="two").pack()
from sklearn.cluster import KMeans
import pandas as pd

# Number of clusters
kmeans = KMeans(n_clusters=2)
dataset = pd.read_csv('time.txt')
X = dataset.iloc[:29].values
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_
#print(C) # From Scratch
print(centroids)



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams['figure.figsize'] = (16, 9)

# Creating a sample dataset with 4 clusters
X, y = make_blobs(n_samples = 800, n_features = 3, centers = 4)


fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])

# Initializing KMeans
kmeans = KMeans(n_clusters=4)
# Fitting with inputs
kmeans = kmeans.fit(X)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c = y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker = '*', c = '#050505', s = 1000)