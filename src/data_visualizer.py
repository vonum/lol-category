import numpy as np
from sklearn import decomposition

from dataset_io import read_csv

def reduce_with_pca_example():
  pca = decomposition.PCA(n_components=2)
  x1 = np.random.normal(size=100)
  x2 = np.random.normal(size=100)
  x3 = x1 + x2
  x = np.c_[x1, x2, x3]

  print x.shape

  pca.fit(x)

  print pca.explained_variance_

  x_reduced = pca.fit_transform(x)

  print x_reduced.shape

  print x
  print x_reduced

reduce_with_pca_example()

def reduce_with_pca():
  data = read_csv('../formatted_data/player_stats_z_normalized.csv')

  pca = decomposition.PCA(n_components=2)
  pca.fit(data)

  return pca.fit_transform(data)

print reduce_with_pca()
