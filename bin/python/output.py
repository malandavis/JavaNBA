from statsIntperpretor import overChecker

def clear():
    with open('InDepthPredictions.txt', 'w') as file:
        file.write('')
    with open('Predictions.txt', 'w') as file:
        file.write('')


def output(stats):
    with open('InDepthPredictions.txt', 'a') as file:
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
        file.write("\t\tOver/Under Success: " + str(stats["total"]["overSuccess"]) + "\n")
        file.write("\t\tOver/Under Success Streak: " + str(stats["total"]["overSuccessStrk"]) + "\n")
        file.write("\n")

    with open('Predictions.txt', 'a') as file:
        file.write(stats["homeTeam"] + " VS " + stats["awayTeam"] + "\n")
        if stats["total"]["spread"] > 50:
            file.write("\tSpread: " + str(stats["homeTeam"]) + " at " + str(stats["spread"]) + "\n")
        elif  stats["total"]["spread"] < 50:
            spread = -1 * float(stats["spread"])
            file.write("\tSpread: " + str(stats["awayTeam"]) + " at " + str(spread) + "\n")
        else:
            file.write("\tSpread: No Bet\n")

        
        if overChecker(stats) == "success":
            if stats["total"]["overSuccess"] > 50:
                file.write("\tOver/Under: Over at " + str(stats["over"]) + "\n")
            elif stats["total"]["overSuccess"] < 50:
                file.write("\tOver/Under: Under at " + str(stats["over"]) + "\n")
            else:
                file.write("\tOver/Under: No Bet\n")
        else:  
            if stats["total"]["overCur"] > 50:
                file.write("\tOver/Under: Over at " + str(stats["over"]) + "\n")
            elif stats["total"]["overCur"] < 50:
                file.write("\tOver/Under: Under at " + str(stats["over"]) + "\n")
            else:
                file.write("\tOver/Under: No Bet\n")

def testOutput(stats, season):
    output = ""
    with open('TestData/TrainingData/' + season + '/Predictions.csv', 'a') as file:
        catagory = ""
        if abs(stats["total"]["spread"] - 50) < 2.5:
            catagory = "0,"
        elif abs(stats["total"]["spread"] - 50) < 5:
            catagory = "1,"
        elif abs(stats["total"]["spread"] - 50) < 7.5:
            catagory = "2,"
        elif abs(stats["total"]["spread"] - 50) < 10:
            catagory = "3,"
        elif abs(stats["total"]["spread"] - 50) < 12.5:
            catagory = "4,"
        elif abs(stats["total"]["spread"] - 50) < 15:
            catagory = "5,"
        else:
            catagory = "6,"
    
        if stats["total"]["spread"] > 50:
            output = "1,"
        else:
            output = "0,"
        if overChecker(stats) == "success":
            overtype = "overSuccess"
            if stats["total"]["overSuccess"] > 50:
                output = output + "1,"
            else:
                output = output + "0,"
        else:
            overtype = "overCur"
            if stats["total"]["overCur"] > 50:
                output = output + "1,"
            else:
                output = output + "0,"
        output = output + catagory
        if abs(stats["total"][overtype] - 50) < 2.5:
            catagory = "0,"
        elif abs(stats["total"][overtype] - 50) < 5:
            catagory = "1,"
        elif abs(stats["total"][overtype] - 50) < 7.5:
            catagory = "2,"
        elif abs(stats["total"][overtype] - 50) < 10:
            catagory = "3,"
        elif abs(stats["total"][overtype] - 50) < 12.5:
            catagory = "4,"
        elif abs(stats["total"][overtype] - 50) < 15:
            catagory = "5,"
        else:
            catagory = "6,"
        output = output + catagory
        ###### output = 'home covers (1/0), over hits (1/0), spread catagory (0-6), over catagory (0-6)'
        file.write(output + "\n")