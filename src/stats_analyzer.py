import numpy as np

from dataset_io import read_json

matches = read_json('../raw_data/matchesChallenger10.json')

def find_cluster_representatives(data, cluster_center):
  distances = np.array([])

  for row in data:
    distances = np.append(distances,
       np.linalg.norm(row - cluster_center))

  min_dist = distances.argsort()[:5]
  max_dist = np.argsort(-distances)[:5]


  return (min_dist, max_dist)

def print_point_details(point_index):
  match_index, player_index = calculate_index(point_index)

  print matches[match_index]['participants'][player_index]['championId']
  print get_item_names(matches[match_index]['participants'][player_index])

def calculate_index(number):
  match_index = number/10
  player_index = number%10

  return match_index, player_index

def get_item_names(player):
  items = read_json('../raw_data/itemsnew.json')
  player_items = [
    player['stats']['item0'],
    player['stats']['item1'],
    player['stats']['item2'],
    player['stats']['item3'],
    player['stats']['item4'],
    player['stats']['item5']
  ]

  player_item_names = []

  for player_item_id in player_items:
    if str(player_item_id) in items:
      item = items[str(player_item_id)]
      player_item_names.append([player_item_id, item['name']])

  return player_item_names

