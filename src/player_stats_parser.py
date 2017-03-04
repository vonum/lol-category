from dataset_io import read_json
from item_parser import parse_items_for_player, parse_items_for_player2

def format_player_stats():
  matches = read_json('../raw_data/matchesChallenger10.json')

  players_stats = []
  for match in matches:
    duration = match['matchDuration']/60
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

      #player_stats.append(player['stats']['totalDamageDealt']*100/duration)
      #player_stats.append(player['stats']['totalDamageTaken']*100/duration)

      #player_stats.append(player['stats']['largestCriticalStrike'])
      #player_stats.append(player['stats']['totalHeal']/duration)
      #player_stats.append(player['stats']['minionsKilled'])
      #player_stats.append(player['stats']['neutralMinionsKilled'])
      #player_stats.append(player['stats']['goldEarned']/duration)
      player_stats.append(100*player['stats']['physicalDamageDealt']/(player['stats']['totalDamageDealt'] + 1))
      player_stats.append(100*player['stats']['magicDamageDealt']/(player['stats']['totalDamageDealt'] + 1))
      #player_stats.append(player['stats']['trueDamageDealt'])
      #player_stats.append(player['stats']['wardsPlaced']/duration)
      #player_stats.append(player['stats']['wardsKilled']/duration)
      player_stats += parse_items_for_player2(player, duration)
      players_stats.append(player_stats)

  return players_stats
