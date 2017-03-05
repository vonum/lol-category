from dataset_io import read_json

def parse_items_for_player(player, duration_coefficient):
  items = read_json('../raw_data/itemsnew.json')
  player_items = [
    player['stats']['item0'],
    player['stats']['item1'],
    player['stats']['item2'],
    player['stats']['item3'],
    player['stats']['item4'],
    player['stats']['item5']
  ]

  stats = [0] * 5 #13

  for player_item_id in player_items:
    if str(player_item_id) in items:
      item = items[str(player_item_id)]
      item_stats = item['stats']
      for stat in item_stats:
        if stat['s'] == 'ad':
          stats[0] += stat['v']*duration_coefficient
        elif stat['s'] == 'ap':
          stats[1] += stat['v']*duration_coefficient
        elif stat['s'] == 'hp':
          stats[2] += stat['v']*duration_coefficient
        #elif stat['s'] == 'mp':
        #  stats[3] += stat['v']*duration_coefficient
        elif stat['s'] == 'armor':
          stats[3] += stat['v']*duration_coefficient
        elif stat['s'] == 'mr':
          stats[4] += stat['v']*duration_coefficient

  return stats
