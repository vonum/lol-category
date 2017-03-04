from dataset_io import read_json

def parse_items_for_player(player, duration):
  items = read_json('../raw_data/item.json')['data']
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
  stats = [0] * 5 #13

  for player_item_id in player_items:
    if str(player_item_id) in items:
      item = items[str(player_item_id)]
      item_stats = item['stats']

      for stat in item_stats:
        if stat == 'FlatHPPoolMod':
          stats[0] += item_stats[stat]/duration
        #elif stat == 'FlatMPPoolMod':
        #  stats[1] += item_stats[stat]/duration
        #elif stat == 'PercentHPRegenMod':
          #stats[2] += item_stats[stat] * 100
        #elif stat == 'PercentMPRegenMod':
        #  stats[3] += item_stats[stat] * 100
        elif stat == 'FlatArmorMod':
          stats[2] += item_stats[stat]/duration
        elif stat == 'FlatSpellBlockMod':
          stats[3] += item_stats[stat]/duration
        elif stat == 'FlatPhysicalDamageMod':
          stats[4] += item_stats[stat]/duration
        elif stat == 'FlatMagicDamageMod':
          stats[5] += item_stats[stat]/duration
        #elif stat == 'FlatMovementSpeedMod':
        #  stats[6] += item_stats[stat]
        #elif stat == 'PercentMovementSpeedMod':
        #  stats[7] += item_stats[stat] * 100
        #elif stat == 'PercentAttackSpeedMod':
        #  stats[6] += item_stats[stat]*100/duration
        #elif stat == 'PercentCritChanceMod':
        #  stats[9] += item_stats[stat] * 100
        #elif stat == 'PercentLifeStealMod':
        #  stats[9] += item_stats[stat] * 100

  return stats

def parse_items_for_player2(player, duration_coefficient):
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
        #  stats[3] += stat['v']*100/duration
        elif stat['s'] == 'armor':
          stats[3] += stat['v']*duration_coefficient
        elif stat['s'] == 'mr':
          stats[4] += stat['v']*duration_coefficient

  return stats
