from statsIntperpretor import strkCheck

def spread(stats):
    stats = calculateSpread(stats["homeTeam"], stats, "home")
    stats = calculateSpread(stats["awayTeam"], stats, "away")
    stats = spreadTotal(stats)
    return stats
    
def calculateSpread(team, dict, status):
    streak = 0
    covers = 0
    games = 0
    teamStr = str(team)

    file = open('Games/NBA/' + teamStr + '.txt', 'r')
    lines = file.readlines()
    for line in lines:
        results = line.split(' ')
        if results[1] == "y" or results[1] == "yes":
            covers += 1
        games += 1
        streak = strkCheck(results[1], streak)
    dict[status]["spread"]["spread"] = 100 * covers / games
    dict[status]["spread"]["spreadStrk"] = streak
    return dict       
        
def spreadTotal(stats):
    spread = stats["home"]["spread"]["spread"] - stats["away"]["spread"]["spread"]
    stats["total"]["spread"] = 50 + (spread / 2)
    return stats