import numpy as np
from sklearn import decomposition
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dataset_io import read_csv

markers = ('s', 'd', 'o')
colors = {0: 'yellow',
          1: 'blue',
          2: 'lightgreen',
          3: 'orange',
          4: 'cyan',
          5: 'magenta',
          6: 'black',
          7: 'white'}
legend = {0: 'Assassin',
          1: 'Mage',
          2: 'Bruiser',
          3: 'Tank',
          4: 'Support',
          5: 'Marksman',
          6: 'None'}

def reduce_with_pca(data, n_components):

  pca = decomposition.PCA(n_components=n_components)
  pca.fit(data)

  return pca.fit_transform(data)

def plot_2d_data(data, labels):

  #plt.scatter(data[:, 0], data[:, 1],
  #            marker=markers(labels[:]),
  #            c=colors(labels[:])
  plt.figure()


  for idx, row in enumerate(data):
    plt.scatter(row[0], row[1],
                c=colors.get(labels[idx], 'red'),
                marker='o',
                label=legend.get(labels[idx], 'None'))
  plt.legend(loc='upper left', numpoints=1, ncol=2, fontsize=8, bbox_to_anchor=(0, 0))

  plt.show()

def plot_3d_data(data, labels):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  for idx, row in enumerate(data):
    plt.scatter(row[0], row[1], row[2],
                c=colors.get(labels[idx], 'red'),
                marker='o',
                label=legend.get(labels[idx], 'none'))

  plt.legend('upper left', numpoints=1, ncol=1, fontsize=8, bbox_to_anchor=(0, 0))

  plt.show()
