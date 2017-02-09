import json
import csv

from item_parser import parse_items_for_player
#from pprint import pprint

def format_player_stats():
  with open('../raw_data/matches1.json') as matches_data:
    matches = json.load(matches_data)

  players_stats = []
  for match in matches['matches']:
    for player in match['participants']:
      player_stats = []
      player_stats.append(player['spell1Id'])
      player_stats.append(player['spell2Id'])
      player_stats.append(player['timeline']['creepsPerMinDeltas']['zeroToTen'])
      player_stats.append(player['timeline']['creepsPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['creepsPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['creepsPerMinDeltas']['thirtyToEnd'])
      player_stats.append(player['timeline']['xpPerMinDeltas']['zeroToTen'])
      player_stats.append(player['timeline']['xpPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['xpPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['xpPerMinDeltas']['thirtyToEnd'])
      player_stats.append(player['timeline']['goldPerMinDeltas']['zeroToTen'])
      player_stats.append(player['timeline']['goldPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['goldPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['goldPerMinDeltas']['thirtyToEnd'])
      player_stats.append(player['stats']['kills'])
      player_stats.append(player['stats']['deaths'])
      player_stats.append(player['stats']['assists'])
      player_stats.append(player['stats']['totalDamageDealt'])
      player_stats.append(player['stats']['totalDamageDealtToChampions'])
      player_stats.append(player['stats']['totalDamageTaken'])
      player_stats.append(player['stats']['largestCriticalStrike'])
      player_stats.append(player['stats']['totalHeal'])
      player_stats.append(player['stats']['minionsKilled'])
      player_stats.append(player['stats']['neutralMinionsKilled'])
      player_stats.append(player['stats']['goldEarned'])
      player_stats.append(player['stats']['physicalDamageDealt'])
      player_stats.append(player['stats']['magicDamageDealt'])
      player_stats.append(player['stats']['trueDamageDealt'])
      player_stats.append(player['stats']['wardsPlaced'])
      player_stats.append(player['stats']['wardsKilled'])
      player_stats += parse_items_for_player(player)
      players_stats.append(player_stats)
      #print playerStats

  return players_stats


