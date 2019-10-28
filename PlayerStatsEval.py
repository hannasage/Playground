import csv
import Keys as key
import plotly.graph_objects as go

input_file = csv.DictReader(open("C:/Users/Kevin/PycharmProjects/leagueoflegends/2019worldsOE.csv"))


def gatherStats(*args):
    gathered_data = {}
    for row in input_file:
        player_id = int(row.get(key.playerid))
        player = row.get(key.player)
        if player_id <= 10:
            if player not in gathered_data.keys():
                gathered_data[player] = {
                    key.position: row.get(key.position)
                }
            else:
                for stat in args:
                    player_dict = gathered_data[player]
                    if stat not in player_dict.keys():
                        player_dict[stat] = []
                    data_list = player_dict[stat]
                    data_list.append(row.get(stat))
                    player_dict[stat] = data_list
    return gathered_data


stats = gatherStats(key.dmgtochamps)
print(stats)
