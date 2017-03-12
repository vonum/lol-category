import sys

from sklearn.mixture import GaussianMixture
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

def em(data):
  gmm = GaussianMixture(n_components=5, covariance_type="tied").fit(data)
  predicted_data = gmm.predict(data)

  print collections.Counter(predicted_data)
  print metrics.silhouette_score(data, predicted_data)

  reduced_data = reduce_with_pca(data)
  plot_2d_data(reduced_data, predicted_data)

em(data)



