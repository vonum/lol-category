import sys

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
#data = zscore(data)
data = StandardScaler().fit_transform(data)

def cluster2d(data, n_clusters):
  reduced_data = reduce_with_pca(data)

  kmeans = KMeans(n_clusters = n_clusters, random_state=0).fit(reduced_data)
  print 'K-Means'
  print collections.Counter(kmeans.labels_)
  print metrics.silhouette_score(data, kmeans.labels_)

  plot_2d_data(reduced_data, kmeans.labels_)

cluster2d(np.array(data), int(sys.argv[1]))
print 'Data shape'
print data.shape
