# include all necessary libs
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd


# Build a class
class Kmsmart:
        def __init__(self, master):
            frame1 = Frame(master, bg = 'black')
            frame1.pack()
            self.lbl_1 = Label(frame1, text = "SMART GARBAGE MONITORING SYSTEM", activebackground = 'blue', activeforeground = 'red', bg = 'red')
            self.lbl_1.config(width = 300,height = 4)
            self.lbl_1.pack(side = TOP)
            frame2 = Frame(master)
            frame2.pack(side = BOTTOM)
            IMAGE = PhotoImage(file = "img3.png")

            self.lbl_2 = Label(frame2, image = IMAGE, activebackground = 'blue', activeforeground = 'red', bg = 'blue')
            self.lbl_2.config(width = 200, height = 10)
            self.lbl_2.pack(side = TOP)

            self.but_1 = Button(frame2, text = "Graph visual", command = self.PtGraph)
            self.but_1.config(width = 20, height = 3, bg = 'blue')
            self.but_1.pack(side = LEFT)

            self.but_2 = Button(frame2, text = "Check ID", command = self.PtCluster)
            self.but_2.config(width = 20, height = 3, bg = 'blue')
            self.but_2.pack(side = RIGHT)

            self.but_3 = Button(frame2, text = "Quit", command = frame.quit)
            self.but_3.config(width = 20, height = 3, bg = 'blue')
            self.but_3.pack(side = BOTTOM)

        def PtGraph(self):

            # Import the dataset
            dataset = pd.read_csv('time.txt')
            X = dataset.iloc[:29].values
            # Splitting the dataset into the Training set and Test set
            from sklearn.cross_validation import train_test_split
            X_train, X_test = train_test_split(X, test_size = 0.2, random_state = 0)
            # Feature Scaling
            from sklearn.preprocessing import StandardScaler
            sc_X = StandardScaler()
            X_train = sc_X.fit_transform(X_train)
            X_test = sc_X.transform(X_test)
            # Using the elbow method find the optimal numbers of clusters
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
            plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 0], s=100, c='blue', marker = 'o',
                        label = 'Cluster 2-->MAX TIME')
            # plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 0], s = 100, c = 'green', label = 'Cluster 3')
            # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 0], s = 100, c = 'cyan', label = 'Cluster 4')
            # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 0], s = 100, c = 'magenta', label = 'Cluster 5')
            # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 0], s = 300, c = 'yellow', label = 'Centroids')
            plt.title('SMART GARBAGE MONITORING SYSTEM')
            plt.xlabel('Time -->')
            plt.ylabel('Fillup rate---->')
            plt.legend()
            plt.show()


        def PtCluster(self):
            print("ADD the cluster function")

root = Tk()
root.title("SGMS")
root.geometry('600x500')
root.config(background='black')
b = Kmsmart(root)
root.mainloop()




