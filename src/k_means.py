import sys

from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
import stats_analyzer

import collections

unnormalized_data = read_csv('../formatted_data/player_stats_z_normalized.csv')
# data = zscore(unnormalized_data)
data = StandardScaler().fit_transform(unnormalized_data)

def k_means(data, n_clusters):
  kmeans = KMeans(n_clusters=n_clusters,
                  n_init=10,
                  init='k-means++',
                  random_state=0).fit(data)
  # print kmeans.labels_
  print 'K-Means'
  print collections.Counter(kmeans.labels_)
  print metrics.silhouette_score(data, kmeans.labels_)

  print len(kmeans.cluster_centers_)
  for cluster_idx in range(0, len(kmeans.cluster_centers_)):
    single_cluster_data = [x for idx, x in enumerate(data) if kmeans.labels_[idx] == cluster_idx]

    print "Cluster {0}".format(cluster_idx)
    min_dist, max_dist = stats_analyzer.find_cluster_representatives(data, kmeans.cluster_centers_[cluster_idx])

    for point_idx in min_dist:
      stats_analyzer.print_point_details(point_idx)
      print kmeans.labels_[point_idx]
      print unnormalized_data[point_idx]

    print min_dist
    print max_dist
    print "************************************************************"

  reduced_data = reduce_with_pca(data, 3)
  plot_3d_data(reduced_data, kmeans.labels_)

k_means(np.array(data), int(sys.argv[1]))
print 'Data shape'
print data.shape
