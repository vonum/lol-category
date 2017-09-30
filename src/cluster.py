from sklearn.cluster import ward_tree, MeanShift, AffinityPropagation
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

from dataset_io import read_csv
from transform_data import z_score
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
data = StandardScaler().fit_transform(data)

def mini_batch_k_means(data, n_clusters):
  return 0

def ward_tree(data):
  wardtree = ward_tree(data)
  print wardtree

def mean_shift(data):
  mean_shift = MeanShift(cluster_all=False, n_jobs=1).fit(data)
  print 'Mean Shift'
  print metrics.silhouette_score(data, mean_shift.labels_)
  print collections.Counter(mean_shift.labels_)

def affinity_prop(data):
  af = AffinityPropagation(damping=0.5, convergence_iter=15, affinity='euclidean').fit(data)
  print 'Affinity Propagation'
  print metrics.silhouette_score(data, af.labels_)
  print collections.Counter(af.labels_)

# mean_shift(np.array(data))
# affinity_prop(np.array(data))
