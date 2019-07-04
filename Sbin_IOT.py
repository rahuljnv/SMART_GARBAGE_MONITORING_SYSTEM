# include all necessary libs
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from PIL import ImageTk, Image
import tkinter.messagebox




# KMEANS
def PtGraph():
    # Importing the dataset
    dataset = pd.read_csv('time.txt')
    X = dataset.iloc[:29].values
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test = train_test_split(X, test_size=0.2, random_state = 0)
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    # Using the elbow method to find the optimal number of clusters#
    from sklearn.cluster import KMeans
    wcss = []
    for i in range(1, 2):
        kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # Fitting K-Means to the dataset
    kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
    y_kmeans = kmeans.fit_predict(X)
    # Visualising the clusters
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 0], s = 100, c = 'red', marker = '1',
                label = 'Cluster 1-->LESS TIME')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 0], s = 100, c = 'blue', marker = 'o',
                label = 'Cluster 2-->MAX TIME')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 0], s = 300, c = 'yellow', label = 'Centroids')
    plt.title('SMART GARBAGE MONITORING SYSTEM')
    plt.xlabel('Time -->')
    plt.ylabel('Fillup rate---->')
    plt.legend()
    plt.show()


# get the centroid
def Ptcentroid():
    from sklearn.cluster import KMeans
    import pandas as pd

    # Number of clusters
    kmeans = KMeans(n_clusters = 2)
    dataset = pd.read_csv('time.txt')
    X = dataset.iloc[:29].values
    # Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the clusters labels
    labels = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_
    # print(C) # From Scratch
    print(centroids)


# BUILD the gui

root = Tk()
# root.geometry('600x300')
root.title("SGMS")
root.config(background = 'blue')

Tframe = Frame(root)
Tframe.pack(side = TOP)

# separator
separator = Frame(height = 5, bd = 10, relief = GROOVE)
separator.pack(fill = X, padx = 5, pady = 5)

# create toolbar
toolbar = Frame(Tframe, bg = 'aqua', padx = 380, pady = 2)
insertB1 = Button(toolbar, text = "Graph Visual", fg = 'brown', command = PtGraph)
insertB1.pack(side = LEFT, padx = 2, pady = 2)
insertB2=Button(toolbar, text = "Check Centroid",fg = "brown", command = Ptcentroid)
insertB2.pack(side = LEFT, padx = 2, pady = 2)
insertB3=Button(toolbar, text = "Exit",fg = 'brown', command = quit)
insertB3.pack(side = RIGHT, padx = 2, pady = 2)
toolbar.pack()

# separator
separator = Frame(height = 5, bd = 10, relief = GROOVE)
separator.pack(fill = X, padx = 5, pady = 5)

# title of the project
label = Label(Tframe, text = "SMART GARBAGE MANGEMENT SYSTEM USING IOT & ML", bg = 'yellow', fg = 'black')
label.config(padx = 240, pady = 30, font = 45)
label.pack(side = BOTTOM, fill = X)

# creating mid frame
Mframe= Frame(root)
Mframe.pack(side = TOP)

Mlframe = Frame(Mframe)
Mlframe.pack(side = LEFT)

# separator
separator = Frame(height = 5, bd = 10, relief = GROOVE)
separator.pack(fill = X, padx = 5, pady = 5)

Mrframe = Frame(Mframe)
Mrframe.pack(side = RIGHT)

# insert image
path1 = "img2.png"
path2 = "img3.png"
imag1 = ImageTk.PhotoImage(Image.open(path1))
l1 = Label(Mlframe, image = imag1, padx = 10,pady = 2)
l1.pack(side = LEFT,fill = X)
imag2 = ImageTk.PhotoImage(Image.open(path2))
l2 = Label(Mrframe,image = imag2, padx = 90, pady = 2)
l2.pack(side = RIGHT, fill = X)

# separator
separator = Frame(height = 5, bd = 10, relief = GROOVE)
separator.pack(fill = X, padx = 5, pady = 5)

# creating BOTTOM frame
Bframe = Frame(root)
Bframe.pack(side = BOTTOM)

# status
status = Label(Bframe, text = "@cheee che Grooup", bd = 2, bg = 'magenta', relief = SUNKEN, padx = 430, pady = 2, anchor = W)
status.pack(side = BOTTOM, fill = X)

# Welcome screen
tkinter.messagebox.showinfo('Welcome Screen','WELCOME TO THE DIGITAL INDIA')


root.mainloop()