import numpy as np
from sklearn import decomposition
from matplotlib import pyplot as plt

from dataset_io import read_csv
from transform_data import z_score

def reduce_with_pca():
  data = read_csv('../formatted_data/player_stats_z_normalized.csv')
  data = z_score(data)

  pca = decomposition.PCA(n_components=2)
  pca.fit(data)

  return pca.fit_transform(data)

def plot_2d_data(data):
  data = np.array(data)
  plt.xlabel("first_column")
  plt.ylabel("second_column")
  plt.scatter(data[:, 0], data[:, 1])

  plt.show()

data =  reduce_with_pca()
print data
print data.shape

plot_2d_data(data)
