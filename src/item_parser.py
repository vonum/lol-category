import json

with open('../raw_data/item.json') as items_data:
  items = json.load(items_data)['data']

def parse_items_for_player(player):
  #0 fhp
  #1 fmp
  #2 php_regen
  #3 pmp_regen
  #4 farmor
  #5 fmr
  #6 fdmg
  #7 fap
  #8 fmovement_speed
  #9 pmovement_speed
  #10 pattack_speed
  #11 pcrit_chance
  #12 plife_steal
  player_items = [
    player['stats']['item0'],
    player['stats']['item1'],
    player['stats']['item2'],
    player['stats']['item3'],
    player['stats']['item4'],
    player['stats']['item5']
  ]
  stats = [0] * 10 #13

  for player_item_id in player_items:
    if str(player_item_id) in items:
      item = items[str(player_item_id)]
      item_stats = item['stats']

      for stat in item_stats:
        if stat == 'FlatHPPoolMod':
          stats[0] += item_stats[stat]
        elif stat == 'FlatMPPoolMod':
          stats[1] += item_stats[stat]
        #elif stat == 'PercentHPRegenMod':
          #stats[2] += item_stats[stat] * 100
        #elif stat == 'PercentMPRegenMod':
        #  stats[3] += item_stats[stat] * 100
        elif stat == 'FlatArmorMod':
          stats[2] += item_stats[stat]
        elif stat == 'FlatSpellBlockMod':
          stats[3] += item_stats[stat]
        elif stat == 'FlatPhysicalDamageMod':
          stats[4] += item_stats[stat]
        elif stat == 'FlatMagicDamageMod':
          stats[5] += item_stats[stat]
        elif stat == 'FlatMovementSpeedMod':
          stats[6] += item_stats[stat]
        elif stat == 'PercentMovementSpeedMod':
          stats[7] += item_stats[stat] * 100
        elif stat == 'PercentAttackSpeedMod':
          stats[8] += item_stats[stat] * 100
        #elif stat == 'PercentCritChanceMod':
        #  stats[9] += item_stats[stat] * 100
        elif stat == 'PercentLifeStealMod':
          stats[9] += item_stats[stat] * 100

  return stats

