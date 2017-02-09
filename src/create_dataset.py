from scipy.stats import zscore

from player_stats_parser import format_player_stats
from dataset_io import write_csv

def write_data_to_csv():
  data = z_score(format_player_stats())
  write_csv('../formatted_data/player_stats_z_normalized.csv', data)

def z_score(data):
  return zscore(data)
  #return (data - data.mean())/data.std()

write_data_to_csv()
