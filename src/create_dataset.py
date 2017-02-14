from player_stats_parser import format_player_stats
from dataset_io import write_csv

def write_data_to_csv():
  data = format_player_stats()
  write_csv('../formatted_data/player_stats_z_normalized.csv', data)


write_data_to_csv()
