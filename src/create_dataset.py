import csv
from scipy.stats import zscore

from player_stats_parser import format_player_stats

def write_data_to_csv():
  data = z_score(format_player_stats())
  with open('../formatted_data/player_stats.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in data:
      writer.writerow(row)

def z_score(data):
  return zscore(data)
  #return (data - data.mean())/data.std()

write_data_to_csv()
