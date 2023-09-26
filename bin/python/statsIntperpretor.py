

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
        

def streakProbability(dict):
    ### File format: spread streak continues, total spread streak, overCur streak continues, total overCur streak, overSuccess streak continues, total overSuccess streak
    file = open('Results/streaks.txt', 'r')
    lines = file.readlines()
    stats = lines[0].split(' ')
    dict["total"]["spreadStrk"] = float(stats[0]) / float(stats[1])
    dict["total"]["overCurStrk"] = float(stats[2]) / float(stats[3])
    dict["total"]["overSuccStrk"] = float(stats[4]) / float(stats[5])
    return dict

def overChecker(tester):
    ### File format: overCur successes, games, overSuccess successes, games
    file = open('Results/OU.txt', 'r')
    lines = file.readlines()
    stats = lines[0].split(' ')
    cur = float(stats[0]) / float(stats[1])
    success = float(stats[2]) / float(stats[3])
    if success > cur:
        return "success"
    else:
        return "cur"

