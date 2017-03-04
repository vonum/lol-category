from sklearn.cluster import KMeans, DBSCAN, ward_tree, MeanShift, AffinityPropagation
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

def mini_batch_k_means(data, n_clusters):
  return 0

def ward_tree(data):
  wardtree = ward_tree(data)
  print wardtree

def db_scan(data, metric):
  dbscan = DBSCAN(eps=0.6, min_samples=14, metric=metric, p=2).fit(data)
  print 'DBSCAN'
  #print dbscan.labels_
  print metrics.silhouette_score(data, dbscan.labels_)
  print collections.Counter(dbscan.labels_)
  reduced_data = reduce_with_pca(data)
  plot_2d_data(reduced_data, dbscan.labels_)

def mean_shift(data):
  mean_shift = MeanShift(cluster_all=False, n_jobs=1).fit(data)
  print 'Mean Shift'
  #print mean_shift.labels_
  print metrics.silhouette_score(data, mean_shift.labels_)
  print collections.Counter(mean_shift.labels_)

def affinity_prop(data):
  af = AffinityPropagation(damping=0.5, convergence_iter=15, affinity='euclidean').fit(data)
  #print af.labels_
  print 'Affinity Propagation'
  print metrics.silhouette_score(data, af.labels_)
  print collections.Counter(af.labels_)

#k_means(np.array(data), 3)
db_scan(np.array(data), 'minkowski')
#mean_shift(np.array(data))
#affinity_prop(np.array(data))
print 'Data shape'
print data.shape
