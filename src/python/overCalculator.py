# from predictor import changeDir

# stats = {"home":{
        # "overCur":
        #     {"over": 0, "overStrk": 0},
        # "overSuccess":
        #     {"over": 0, "overStrk": 0},
        # "spread":
        #     {"spread": 0, "spreadStrk": 0}
        # },
        # "away":{
        # "overCur":
        #     {"over": 0, "overStrk": 0},
        # "overSuccess":
        #     {"over": 0, "overStrk": 0},
        # "spread":
        #     {"spread": 0, "spreadStrk": 0}
        # },
        # "total":
        #     {"overCur": 0, "overCurStrk": 0, "overSucc": 0, "overSuccStrk": 0, "spread": 0, "spreadStrk": 0},
        # "homeTeam": "",
        # "awayTeam": "",
        # "spread": 0,
        # "over": 0
        # }

def over(stats):
    # changeDir()
    stats = overCur(stats["homeTeam"], stats["over"], stats, "home")
    stats = overCur(stats["awayTeam"], stats["over"], stats, "away")
    stats = overSuccess(stats["homeTeam"], stats["over"], stats, "home")
    stats = overSuccess(stats["awayTeam"], stats["over"], stats, "away")
    return stats
    



def overCur(team, over, dict, status):
    # changeDir()
    streak = 0
    overs = 0
    games = 0
    teamstr = str(team)

    file = open('Games/NBA/' + teamstr + '.txt', 'r')
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

    

            

def overSuccess(team, over, dict, status):
    # changeDir()
    streak = 0
    overs = 0
    games = 0
    teamstr = str(team)

    file = open('Games/NBA/' + teamstr + '.txt', 'r')
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

def strkCheck(result, cur):
    if cur > 0:
        if result == "y" or result == "yes":
            return cur + 1
        else:
            return -1
    elif cur < 0:
        if result == "n" or result == "no":
            return cur - 1
        else:
            return 1
    else:
        if result == "y" or result == "yes":
            return 1
        else:
            return -1