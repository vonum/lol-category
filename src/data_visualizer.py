import numpy as np
from sklearn import decomposition

def reduce_with_pca(data):
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
reduce_with_pca(1)
