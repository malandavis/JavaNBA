from statsIntperpretor import strkCheck

def spread(stats, TEST, season):
    stats = calculateSpread(stats["homeTeam"], stats, "home", TEST, season)
    stats = calculateSpread(stats["awayTeam"], stats, "away", TEST, season)
    stats = spreadTotal(stats)
    return stats
    
def calculateSpread(team, dict, status, TEST, season):
    filepath = 'Games/NBA/' + str(team) + '.txt'
    if TEST:
        filepath = 'TestData/TrainingData/' + season + '/NBA/' + str(team) + '.txt'
    streak = 0
    covers = 0
    games = 0

    file = open(filepath, 'r')
    lines = file.readlines()
    for line in lines:
        results = line.split(' ')
        if results[1] == "y" or results[1] == "yes":
            covers += 1
        games += 1
        streak = strkCheck(results[1], streak)
    if games == 0:
        games = 100000
    dict[status]["spread"]["spread"] = 100 * covers / games
    dict[status]["spread"]["spreadStrk"] = streak
    return dict           
        
def spreadTotal(stats):
    spread = stats["home"]["spread"]["spread"] - stats["away"]["spread"]["spread"]
    stats["total"]["spread"] = 50 + (spread / 2)
    return stats