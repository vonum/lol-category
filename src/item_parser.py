def parse_item(item):
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
  item_stats = item['stats']
  stats = [0] * 13
  for stat in item_stats:
    if stat == 'FlatHPPoolMod':
      stats[0] += item_stats[stat]
    elif stat == 'FlatMPPoolMod':
      stats[1] += item_stats[stat]
    elif stat == 'PercentHPRegenMod':
      stats[2] += item_stats[stat]
    elif stat == 'PercentMPRegenMod':
      stats[3] += item_stats[stat]
    elif stat == 'FlatArmorMod':
      stats[4] += item_stats[stat]
    elif stat == 'FlatSpellBlockMod':
      stats[5] += item_stats[stat]
    elif stat == 'FlatPhysicalDamageMod':
      stats[6] += item_stats[stat]
    elif stat == 'FlatMagicDamageMod':
      stats[7] += item_stats[stat]
    elif stat == 'FlatMovementSpeedMod':
      stats[8] += item_stats[stat]
    elif stat == 'PercentMovementSpeedMod':
      stats[9] += item_stats[stat]
    elif stat == 'PercentAttackSpeedMod':
      stats[10] += item_stats[stat]
    elif stat == 'PercentCritChanceMod':
      stats[11] += item_stats[stat]
    elif stat == 'PercentLifeStealMod':
      stats[12] += item_stats[stat]
  return stats

