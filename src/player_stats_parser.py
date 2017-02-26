from dataset_io import read_json
from item_parser import parse_items_for_player

def format_player_stats():
  matches = read_json('../raw_data/matches1.json')

  players_stats = []
  for match in matches['matches']:
    duration = match['matchDuration']
    for player in match['participants']:
      player_stats = []
      #player_stats.append(player['timeline']['creepsPerMinDeltas']['zeroToTen'])
      #player_stats.append(player['timeline']['creepsPerMinDeltas']['tenToTwenty'])
      #player_stats.append(player['timeline']['creepsPerMinDeltas']['twentyToThirty'])
      #player_stats.append(player['timeline']['creepsPerMinDeltas']['thirtyToEnd'])
      #player_stats.append(player['timeline']['xpPerMinDeltas']['zeroToTen'])
      #player_stats.append(player['timeline']['xpPerMinDeltas']['tenToTwenty'])
      #player_stats.append(player['timeline']['xpPerMinDeltas']['twentyToThirty'])
      #player_stats.append(player['timeline']['xpPerMinDeltas']['thirtyToEnd'])
      #player_stats.append(player['timeline']['goldPerMinDeltas']['zeroToTen'])
      #player_stats.append(player['timeline']['goldPerMinDeltas']['tenToTwenty'])
      #player_stats.append(player['timeline']['goldPerMinDeltas']['twentyToThirty'])
      #player_stats.append(player['timeline']['goldPerMinDeltas']['thirtyToEnd'])
      #player_stats.append(player['stats']['kills'])
      #player_stats.append(player['stats']['deaths'])
      #player_stats.append(player['stats']['assists'])
      #player_stats.append(player['stats']['totalDamageDealt']/duration)
      player_stats.append(player['stats']['totalDamageDealt']/duration)
      player_stats.append(player['stats']['totalDamageTaken']/duration)
      #player_stats.append(player['stats']['largestCriticalStrike'])
      #player_stats.append(player['stats']['totalHeal']/duration)
      #player_stats.append(player['stats']['minionsKilled'])
      #player_stats.append(player['stats']['neutralMinionsKilled'])
      #player_stats.append(player['stats']['goldEarned']/duration)
      player_stats.append(player['stats']['physicalDamageDealt']/duration)
      player_stats.append(player['stats']['magicDamageDealt']/duration)
      #player_stats.append(player['stats']['trueDamageDealt'])
      #player_stats.append(player['stats']['wardsPlaced']/duration)
      #player_stats.append(player['stats']['wardsKilled']/duration)
      player_stats += parse_items_for_player(player, duration)
      players_stats.append(player_stats)

  return players_stats

def ratio(part, total):
  return (part/total) * 100
