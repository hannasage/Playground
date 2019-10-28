import csv
import Keys as key
import Evaluation as eval
import plotly.graph_objects as go

input_file = csv.DictReader(open("C:/Users/Kevin/PycharmProjects/leagueoflegends/2019worldsOE.csv"))


def gatherStats(*args):
    gathered_data = {}
    for row in input_file:
        player_id = int(row.get(key.playerid))
        team = row.get(key.team)
        if player_id == 100 or player_id == 200:
            if team not in gathered_data.keys():
                gathered_data[team] = {
                    key.team: row.get(key.team)
                }
            else:
                for stat in args:
                    player_dict = gathered_data[team]
                    if stat not in player_dict.keys():
                        player_dict[stat] = []
                    data_list = player_dict[stat]
                    data_list.append(row.get(stat))
                    player_dict[stat] = data_list
    return gathered_data


stats = gatherStats(key.dmgtochamps)
print(eval.averageStat(key.dmgtochamps, stats[key.SKT]))
print(eval.averageStat(key.dmgtochamps, stats[key.G2]))
