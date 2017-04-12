import sys

from sklearn.cluster import SpectralClustering
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
#data = z_score(data)
data = StandardScaler().fit_transform(data)

def spectral(data, n_clusters):
  spectral = SpectralClustering(n_clusters=n_clusters,
      eigen_solver='arpack',
      affinity='rbf',
      assign_labels='discretize').fit(data)
  #print spectral.labels_
  print 'Spectral'
  print collections.Counter(spectral.labels_)
  print metrics.silhouette_score(data, spectral.labels_)
  reduced_data = reduce_with_pca(data, 3)
  plot_2d_data(reduced_data, spectral.labels_)

spectral(np.array(data), int(sys.argv[1]))
print 'Data shape'
print data.shape
