
def clear():
    with open('Predictions.txt', 'w') as file:
        file.write('')


def output(stats):
    

    with open('Predictions.txt', 'a') as file:
        file.write(stats["homeTeam"] + " VS " + stats["awayTeam"] + ".\n")
        file.write("\tSpread: " + str(stats["spread"]) + "\n")
        file.write("\tOver/Under: " + str(stats["over"]) + "\n")
        file.write("\t" + str(stats["homeTeam"]) + ":\n")
        file.write("\t\tSpread: " + str(stats["home"]["spread"]["spread"]) + "\n")
        file.write("\t\tSpread Streak: " + str(stats["home"]["spread"]["spreadStrk"]) + "\n")
        file.write("\t\tOver/Under: " + str(stats["home"]["overCur"]["over"]) + "\n")
        file.write("\t\tOver/Under Streak: " + str(stats["home"]["overCur"]["overStrk"]) + "\n")
        file.write("\t\tOver/Under Success: " + str(stats["home"]["overSuccess"]["over"]) + "\n")
        file.write("\t\tOver/Under Success Streak: " + str(stats["home"]["overSuccess"]["overStrk"]) + "\n")
        file.write("\t" + str(stats["awayTeam"]) + ":\n")
        file.write("\t\tSpread: " + str(stats["away"]["spread"]["spread"]) + "\n")
        file.write("\t\tSpread Streak: " + str(stats["away"]["spread"]["spreadStrk"]) + "\n")
        file.write("\t\tOver/Under: " + str(stats["away"]["overCur"]["over"]) + "\n")
        file.write("\t\tOver/Under Streak: " + str(stats["away"]["overCur"]["overStrk"]) + "\n")
        file.write("\t\tOver/Under Success: " + str(stats["away"]["overSuccess"]["over"]) + "\n")
        file.write("\t\tOver/Under Success Streak: " + str(stats["away"]["overSuccess"]["overStrk"]) + "\n")
        file.write("\tTotal:\n")
        file.write("\t\tSpread: " + str(stats["total"]["spread"]) + "\n")
        file.write("\t\tSpread Streak: " + str(stats["total"]["spreadStrk"]) + "\n")
        file.write("\t\tOver/Under: " + str(stats["total"]["overCur"]) + "\n")
        file.write("\t\tOver/Under Streak: " + str(stats["total"]["overCurStrk"]) + "\n")
        file.write("\t\tOver/Under Success: " + str(stats["total"]["overSucc"]) + "\n")
        file.write("\t\tOver/Under Success Streak: " + str(stats["total"]["overSuccStrk"]) + "\n")
        file.write("\n")

