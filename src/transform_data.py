import json
import csv

from item_parser import parse_item
#from pprint import pprint

with open('../raw_data/matches1.json') as matches_data:
  matches = json.load(matches_data)

with open('../formatted_data/player_stats.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
  for match in matches['matches']:
    for player in match['participants']:
      playerStats = []
      playerStats.append(player['spell1Id'])
      playerStats.append(player['spell2Id'])
      playerStats.append(player['timeline']['creepsPerMinDeltas']['zeroToTen'])
      playerStats.append(player['timeline']['creepsPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['creepsPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['creepsPerMinDeltas']['thirtyToEnd'])
      playerStats.append(player['timeline']['xpPerMinDeltas']['zeroToTen'])
      playerStats.append(player['timeline']['xpPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['xpPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['xpPerMinDeltas']['thirtyToEnd'])
      playerStats.append(player['timeline']['goldPerMinDeltas']['zeroToTen'])
      playerStats.append(player['timeline']['goldPerMinDeltas']['tenToTwenty'])
      #playerStats.append(player['timeline']['goldPerMinDeltas']['twentyToThirty'])
      #playerStats.append(player['timeline']['goldPerMinDeltas']['thirtyToEnd'])
      playerStats.append(player['stats']['kills'])
      playerStats.append(player['stats']['deaths'])
      playerStats.append(player['stats']['assists'])
      playerStats.append(player['stats']['totalDamageDealt'])
      playerStats.append(player['stats']['totalDamageDealtToChampions'])
      playerStats.append(player['stats']['totalDamageTaken'])
      playerStats.append(player['stats']['largestCriticalStrike'])
      playerStats.append(player['stats']['totalHeal'])
      playerStats.append(player['stats']['minionsKilled'])
      playerStats.append(player['stats']['neutralMinionsKilled'])
      playerStats.append(player['stats']['goldEarned'])
      playerStats.append(player['stats']['physicalDamageDealt'])
      playerStats.append(player['stats']['magicDamageDealt'])
      playerStats.append(player['stats']['trueDamageDealt'])
      playerStats.append(player['stats']['wardsPlaced'])
      playerStats.append(player['stats']['wardsKilled'])
      writer.writerow(playerStats)
      #print playerStats

with open('../raw_data/item.json') as items_data:
  items = json.load(items_data)

item = items['data']['1001']
#print item['stats']
parse_item(item)

for item_id in items['data']:
  print parse_item(items['data'][item_id])
  print item_id
