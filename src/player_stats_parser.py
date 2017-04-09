from dataset_io import read_json
from item_parser import parse_items_for_player
import numpy as np

def format_player_stats():
  matches = read_json('../raw_data/matchesChallenger10.json')

  players_stats = []
  for match in matches:
    duration = duration_coefficient(match['matchDuration']/60)
    for player in match['participants']:
      player_stats = []

      player_stats.append(100*player['stats']['physicalDamageDealt']/(player['stats']['totalDamageDealt']))
      player_stats.append(100*player['stats']['magicDamageDealt']/(player['stats']['totalDamageDealt']))
      #player_stats.append(player['stats']['trueDamageDealt'])
      #player_stats.append(player['stats']['wardsPlaced']/duration)
      #player_stats.append(player['stats']['wardsKilled']/duration)
      player_stats += parse_items_for_player(player, duration)
      players_stats.append(player_stats)

  return np.array(players_stats)

def duration_coefficient(duration):
  if duration >= 30 and duration < 35:
    duration_coefficient = 1.5
  elif duration >= 35 and duration < 40:
    duration_coefficient = 1.3
  else:
    duration_coefficient = 1

  return duration_coefficient
