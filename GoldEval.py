import csv
import Keys as key
import plotly.graph_objects as go

input_file = csv.DictReader(open("C:/Users/Kevin/PycharmProjects/leagueoflegends/2019worldsOE.csv"))


# TODO:
# Determine GPM from 10-15


def gatherStats(team, *args):
    gathered_data = {}
    for row in input_file:
        player_id = int(row.get(key.playerid))
        team_name = row.get(key.team)
        if (player_id == 100 or player_id == 200) and team in team_name:
            for stat in args:
                data = []
                if stat in gathered_data.keys():
                    data = gathered_data[stat]
                    data.append(row.get(stat))
                else:
                    data.append(row.get(stat))
                    gathered_data[stat] = data
    return gathered_data


def averageStatPerMin(stat_list, minutes):
    stat_total = 0.0
    for stat in stat_list:
        stat_total += int(stat) / minutes
    return stat_total/len(stat_list)


def averageGameLength(times):
    stat_total = 0.0
    for time in times:
        stat_total += float(time)
    return stat_total/len(times)


# FOR NUMBERS ONLY #
def averageStat(stat, data):
    stat_total = 0
    game_total = len(data[stat])
    data_list = data[stat]
    for item in data_list:
        stat_total += int(item)
    return stat_total/game_total


stats = gatherStats(key.GRF, key.gdat10, key.goldat10, key.oppgoldat10,
                    key.gdat15, key.goldat15, key.oppgoldat15, key.totalgold, key.gamelength)

x = stats[key.goldat15]
y = stats[key.goldat10]

print(x[1])
print(y[1])
print((int(x[1])-int(y[1]))/5)

