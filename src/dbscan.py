import sys

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
data = zscore(data)
data = StandardScaler().fit_transform(data)

def db_scan(data, eps, min_samples, metric):
  dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric=metric).fit(data)
  print 'DBSCAN'
  #print dbscan.labels_
  print metrics.silhouette_score(data, dbscan.labels_)
  print collections.Counter(dbscan.labels_)
  reduced_data = reduce_with_pca(data)
  plot_2d_data(reduced_data, dbscan.labels_)

db_scan(np.array(data), float(sys.argv[1]), float(sys.argv[2]), 'euclidean')
print 'Data shape'
print data.shape
