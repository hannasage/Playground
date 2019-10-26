import csv
import Keys as key
import plotly.graph_objects as go

input_file = csv.DictReader(open("C:/Users/Kevin/PycharmProjects/leagueoflegends/2019worldsOE.csv"))


def iteratevalue(key, dictionary):
    if key not in dictionary.keys():
        dictionary[key] = 1
    else:
        dictionary[key] += 1


def sortdictionary(dictionary):
    sorted_tuple = sorted(dictionary.items(), reverse=True, key=lambda x: x[1])
    return dict(sorted_tuple)


def newdatafunc(team1, team2):
    data_dict = {
        team1: {
            key.picks: {},
            key.bans: {}
        },
        team2: {
            key.picks: {},
            key.bans: {}
        }
    }
    for row in input_file:
        player_id = int(row.get(key.playerid))
        team_name = row.get(key.team)
        if team1 in team_name:
            if player_id <= 10:
                iteratevalue(row.get(key.champion), data_dict[team1][key.picks])
            elif player_id == 100 or player_id == 200:
                for ban_key in key.ban_keys:
                    iteratevalue(row.get(ban_key), data_dict[team1][key.bans])
        elif team2 in team_name:
            if player_id <= 10:
                iteratevalue(row.get(key.champion), data_dict[team2][key.picks])
            elif player_id == 100 or player_id == 200:
                for ban_key in key.ban_keys:
                    iteratevalue(row.get(ban_key), data_dict[team2][key.bans])
    return data_dict


# DEFINE YOUR MATCHUP #
data = newdatafunc(key.SPY, key.FPX)
team1_data = data[key.SPY]
team2_data = data[key.FPX]

team1_picks = team1_data[key.picks]
team1_bans = team1_data[key.bans]
team2_picks = team2_data[key.picks]
team2_bans = team2_data[key.bans]

fig = go.Figure()
fig.add_trace(go.Bar(y=list(team1_picks.values()), x=list(team1_picks.keys()),
                     marker={'color': '#cccccc'},
                     name=key.SPY))
fig.add_trace(go.Bar(y=list(team2_picks.values()), x=list(team2_picks.keys()),
                     marker={'color': '#333333'},
                     name=key.GRF))
fig.update_layout(
    title='Champions Picked at Worlds',
    barmode='group',
    xaxis_tickangle=-90,
    yaxis_tickangle=-90,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Times Picked',
        titlefont_size=16,
        tickfont_size=16,
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()

