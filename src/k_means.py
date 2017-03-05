import sys

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

from dataset_io import read_csv
from transform_data import z_score
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
#data = z_score(data)
data = StandardScaler().fit_transform(data)

def k_means(data, n_clusters):
  kmeans = KMeans(n_clusters = n_clusters, random_state=0).fit(data)
  #print kmeans.labels_
  print 'K-Means'
  print collections.Counter(kmeans.labels_)
  print metrics.silhouette_score(data, kmeans.labels_)
  reduced_data = reduce_with_pca(data)
  plot_2d_data(reduced_data, kmeans.labels_)

k_means(np.array(data), int(sys.argv[1]))
print 'Data shape'
print data.shape
