import random as rd
import csv

def diff(a, b):
    return abs(a - b)

def assign_cluster(string, centroid):
    clusters = [[] for i in range(len(centroid))]
    for i in string:
        dist = [diff(i, j) for j in centroid]
        min_dist = dist.index(min(dist))
        clusters[min_dist].append(i)
    return clusters

def Kmean(string, no_clusters, max_iter = 100):
    centroid = rd.sample(string, no_clusters)
    for i in range(max_iter):
        clusters = assign_cluster(string, centroid)
        clusters = [sorted(cluster) for cluster in clusters]
        new_centroid = [sum(i) / len(i) for i in clusters]
        if new_centroid == centroid:
            break
        centroid = new_centroid
    return clusters, centroid

# Input
with open("D:\Projects\Python\Academic\TE\DWM\input.csv", "r") as file:
    reader = csv.reader(file)
    string = [int(number) for row in reader for number in row]

no_clusters = int(input("Enter no. of cluster: "))
sorted(string)

clusters , centroids = Kmean(string, no_clusters)

i = 1 
for cluster, centroid in zip (sorted(clusters), sorted(centroids)):
    print(f"Mean, Cluster {i} : {int(centroid)},\t{cluster}")
    i += 1