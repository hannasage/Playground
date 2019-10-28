

def averageStatPerMin(stat_list, minutes):
    stat_total = 0.0
    for stat in stat_list:
        stat_total += int(stat) / minutes
    return stat_total / len(stat_list)


# FOR NUMBERS ONLY #
def averageStat(stat, data):
    stat_total = 0
    game_total = len(data[stat])
    data_list = data[stat]
    for item in data_list:
        stat_total += int(item)
    return stat_total / game_total

