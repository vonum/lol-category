import sys

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
from stats_analyzer import find_cluster_representatives

import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
#data = zscore(data)
data = StandardScaler().fit_transform(data)

def k_means(data, n_clusters):
  kmeans = KMeans(n_clusters = n_clusters, random_state=0).fit(data)
  # print kmeans.labels_
  print 'K-Means'
  print collections.Counter(kmeans.labels_)
  print metrics.silhouette_score(data, kmeans.labels_)
  # reduced_data = reduce_with_pca(data)
  # plot_2d_data(reduced_data, kmeans.labels_)

  for cluster_idx in range(0, 6):
    single_cluster_data = [x for idx, x in enumerate(data) if kmeans.labels_[idx] == cluster_idx]

    print "Cluster {0}".format(cluster_idx)
    min_dist = find_cluster_representatives(single_cluster_data, kmeans.cluster_centers_[cluster_idx])
    print min_dist
    print "************************************************************"

k_means(np.array(data), int(sys.argv[1]))
print 'Data shape'
print data.shape
