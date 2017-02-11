from sklearn.cluster import KMeans, DBSCAN, ward_tree, MeanShift
from sklearn import metrics
import numpy as np

from ..dataset_io import read_csv

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
data = np.array(data).astype(np.float)

def k_means(data, n_clusters):
  kmeans = KMeans(n_clusters = n_clusters, random_state=0).fit(data)
  print kmeans.labels_
  print kmeans.cluster_centers_
  print np.bincount(kmeans.labels_)
  print metrics.silhouette_score(data, kmeans.labels_)

def mini_batch_k_means(data, n_clusters):
  return 0

def ward_tree(data):
  wardtree = ward_tree(data)
  print wardtree

def db_scan(data):
  dbscan = DBSCAN(eps=3, min_samples=5).fit(data)
  print dbscan.labels_
  print metrics.silhouette_score(data, dbscan.labels_)

def mean_shift(data):
  print data
  mean_shift = MeanShift(cluster_all=False, n_jobs=1).fit(data)
  print mean_shift.labels_
  print np.unique(mean_shift.labels_)
  print mean_shift.labels_.shape

# k_means(np.array(data), 6)
db_scan(np.array(data))
# mean_shift(data)
print data.shape
