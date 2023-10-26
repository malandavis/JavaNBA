from statsIntperpretor import strkCheck
from variables import *

def over(stats, TEST, season):
    stats = overCur(stats["homeTeam"], stats["over"], stats, "home", TEST, season)
    stats = overCur(stats["awayTeam"], stats["over"], stats, "away", TEST, season)
    stats = overSuccess(stats["homeTeam"], stats["over"], stats, "home", TEST, season)
    stats = overSuccess(stats["awayTeam"], stats["over"], stats, "away", TEST, season)
    stats = overTotal(stats)
    return stats
    
def overCur(team, over, dict, status, TEST, season):
    filepath = 'Games/NBA/' + SZN + str(team) + '.txt'
    if TEST:
        filepath = 'TestData/TrainingData/' + season + '/NBA/' + str(team) + '.txt'
    streak = 0
    overs = 0
    games = 0

    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:
        results = line.split(' ')
        if results[4] > over:
            overs += 1
        games += 1
        streak = strkCheck(results[3], streak)
    dict[status]["overCur"]["over"] = 100 * overs / games
    dict[status]["overCur"]["overStrk"] = streak
    return dict       

def overSuccess(team, over, dict, status, TEST, season):
    filepath = 'Games/NBA/' + SZN + str(team) + '.txt'
    if TEST:
        filepath = 'TestData/TrainingData/' + season + '/NBA/' + str(team) + '.txt'
    streak = 0
    overs = 0
    games = 0

    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:
        results = line.split(' ')
        if results[3] == "y" or results[3] == "yes":
            overs += 1
        games += 1
        streak = strkCheck(results[3], streak)
    dict[status]["overSuccess"]["over"] = 100 * overs / games
    dict[status]["overSuccess"]["overStrk"] = streak
    return dict
        
def overTotal(stats):
    overCur = stats["home"]["overCur"]["over"] * stats["away"]["overCur"]["over"] / 100
    underCur = (1 - stats["home"]["overCur"]["over"] / 100) * (1 - stats["away"]["overCur"]["over"] / 100) * 100
    dif = overCur - underCur
    overCur = 50 + (dif / 2)
    stats["total"]["overCur"] = overCur
    overSuccess = stats["home"]["overSuccess"]["over"] * stats["away"]["overSuccess"]["over"] / 100
    underSuccess = (1 - stats["home"]["overSuccess"]["over"] / 100) * (1 - stats["away"]["overSuccess"]["over"] / 100) * 100
    dif = overSuccess - underSuccess
    overSuccess = 50 + (dif / 2)
    stats["total"]["overSuccess"] = overSuccess
    return stats