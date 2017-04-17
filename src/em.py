import sys

from sklearn.mixture import GaussianMixture
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from scipy.stats import zscore
import numpy as np

from dataset_io import read_csv
from data_visualizer import *
import collections

data = read_csv('../formatted_data/player_stats_z_normalized.csv')
# data = zscore(data)
data = StandardScaler().fit_transform(data)

def em(data):
  gmm = GaussianMixture(
    n_components=6,
    covariance_type="tied"
  ).fit(data)
  predicted_data = gmm.predict(data)

  print collections.Counter(predicted_data)
  print metrics.silhouette_score(data, predicted_data)

  reduced_data = reduce_with_pca(data, 2)
  plot_2d_data(reduced_data, predicted_data)

em(data)
