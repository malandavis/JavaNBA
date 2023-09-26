import subprocess
import shutil
import os

Teams = {'1610612737': 'Hawks', '1610612738': 'Celtics', '1610612739': 'Cavaliers', '1610612740': 'Pelicans', 
         '1610612741': 'Bulls', '1610612742': 'Mavericks', '1610612743': 'Nuggets', '1610612744': 'Warriors', 
         '1610612745': 'Rockets', '1610612746': 'Clippers', '1610612747': 'Lakers', '1610612748': 'Heat', 
         '1610612749': 'Bucks', '1610612750': 'Timberwolves', '1610612751': 'Nets', '1610612752': 'Knicks', 
         '1610612753': 'Magic', '1610612754': 'Pacers', '1610612755': '76ers', '1610612756': 'Suns', '1610612757': 'Blazers',
         '1610612758': 'Kings', '1610612759': 'Spurs', '1610612760': 'Thunder', '1610612761': 'Raptors', '1610612762': 'Jazz', 
         '1610612763': 'Grizzlies', '1610612764': 'Wizards', '1610612765': 'Pistons', '1610612766': 'Hornets'}
log = {"Date": "", "betSize": 0, "capital": 100, "Game#": 0, "Home": "", "Away": "", "flip": False}
catagory = {"1": "0-10.csv", "2": "10-20.csv", "3": "20-30.csv", "4": "30+.csv"}
day = "11/1/2017"
season = "2018"

def cutLosses():
    with open ('TestData/TrainingResults/capital.txt', 'r') as file:
        total = float(file.read())
        if total > 120:
            with open ('TestData/TrainingResults/totalEarnings.txt', 'r') as file:
                totalEarnings = float(file.read())
                totalEarnings = totalEarnings + total - 100
            with open ('TestData/TrainingResults/totalEarnings.txt', 'w') as file:
                file.write(str(totalEarnings))
            with open ('TestData/TrainingResults/earningsLog.txt', 'a') as file:
                file.write("Earnings: " + str(totalEarnings) + '\n')
            with open ('TestData/TrainingResults/capital.txt', 'w') as file:
                file.write('100')
            with open ('TestData/TrainingResults/cutLossesLog.txt', 'a') as file:
                file.write("Earned " + str(total - 100) + '\n')
        elif total < 80:
            with open ('TestData/TrainingResults/totalEarnings.txt', 'r') as file:
                totalEarnings = float(file.read())
                totalEarnings = totalEarnings + total - 100
            with open ('TestData/TrainingResults/totalEarnings.txt', 'w') as file:
                file.write(str(totalEarnings))
            with open ('TestData/TrainingResults/earningsLog.txt', 'a') as file:
                file.write("Earnings: " + str(totalEarnings) + '\n')
            with open ('TestData/TrainingResults/capital.txt', 'w') as file:
                file.write('100')
            with open ('TestData/TrainingResults/cutLossesLog.txt', 'a') as file:
                file.write("Lost " + str(100 - total) + '\n')

def addGame(team1, team2, season):
    output = ""
    homescore = 0
    awayscore = 0
    if team1[3] == 't':
        home = Teams[team1[2]]
        away = Teams[team2[2]]
        output = home + "," + away
        homescore = team1[4]
        awayscore = team2[4]
    else:
        home = Teams[team2[2]]
        away = Teams[team1[2]]
        output = home + "," + away
        homescore = team2[4]
        awayscore = team1[4]

    with open ('TestData/TrainingData/' + season + '/Spreads.csv', 'r') as file:
        for line in file:
            if line.__contains__(team1[0]):
                spread = line.split(',')[6]
                output = output + "," + str(spread)
                break
    with open ('TestData/TrainingData/' + season + '/Overs.csv', 'r') as file:
        for line in file:
            if line.__contains__(team1[0]):
                over = line.split(',')[5]
                output = output + "," + str(over)
                break
    output = output + "," + str(homescore) + "," + str(awayscore) + ",\n"
    with open ('Games.csv' , 'a') as file:
        file.write(output)

def addResults(predictOutcome, numDay):
    game = 0
    with open ('Games.csv', 'r') as file:
        for lines in file:
            line = lines.split(',')
            home = line[0]
            away = line[1]
            homeScore = float(line[4])
            awayScore = float(line[5])
            spread = float(line[2])
            over = float(line[3])
            result = ["", "", ""]
            betResult = [0,0]
            log["Home"] = home
            log["Away"] = away
            log["Game#"] = game
            numGames = 0
            with open('TestData/TrainingData/' + season + '/NBA/' + home + '.txt', 'a') as file:
                if homeScore + spread > awayScore:
                    result[0] = " y "
                    betResult[0] = 1
                else:
                    result[0] = " n "
                    betResult[0] = 0
                if homeScore + awayScore > over:
                    result[1] = " y "
                    betResult[1] = 1
                else:
                    result[1] = " n "
                    betResult[1] = 0
                result[2] = str(homeScore + awayScore)
                output = str(spread) + result[0] + str(over) + result[1] + result[2] + '\n'
                file.write(output)
            with open('TestData/TrainingData/' + season +'/NBA/' + away + '.txt', 'a') as file:
                if awayScore - spread > homeScore:
                    result[0] = " y "
                else:
                    result[0] = " n "
                output = str(spread * -1) + result[0] + str(over) + result[1] + result[2] + '\n'
                file.write(output)
            
            if predictOutcome == True:
                with open ('TestData/TrainingData/' + season + '/Predictions.csv', 'r') as file:
                    for lines in file:
                        if not lines.__contains__("-1"):
                            numGames = numGames + 1
                predict(game, numGames, betResult, numDay)
            game = game + 1
            
            with open('TestData/TrainingResults/log.txt', 'a') as file:
                file.write(str(log) + '\n')
    
    if predictOutcome == True and numGames >= 2:
        capital = 0
        with open('TestData/TrainingData/daysBets.txt', 'r') as file:
            capital = float(file.read())
        with open('TestData/TrainingResults/capital.txt', 'w') as file:
            file.write(str(capital))
    with open('TestData/TrainingData/daysBets.txt', 'w') as file:
        file.write('0')

def predict(gameNum, numGames, betResult, numDay):
    capital = 0
    earned = 0 
    total = 0
    results = []

    predictions = getPredictions(gameNum)
    flip = False
    with open('TestData/TrainingResults/' + catagory[predictions[2]], 'r') as file:
        line = file.read()
        results = line.split(',')
        if predictions[1] == "0":
            q = 1
        else:
            q = float(predictions[0]) / float(predictions[1])
        ############ change numDays peramter to make the flip functional
        if q < .5 and numDays >  4000:
            flip = True
            log["flip"] = True
    with open('TestData/TrainingResults/results.csv', 'r') as file:
        line = file.read()
        results = line.split(',')

    results[1] = int(results[1]) + 1
    results[3] = int(results[3]) + 1

    with open('TestData/TrainingResults/capital.txt', 'r') as file:
        capital = float(file.read())

    bet = capital / (numGames * 2)
    # print("BET SIZE = " + str(bet) + "/" + str(capital) + "/" + str(numGames))
    log["betSize"] = bet
    log["capital"] = capital

    catagoryResults = [0, 0]
    with open('TestData/TrainingResults/' + catagory[predictions[2]], 'r') as file:
        line = file.readline().split(',')
        catagoryResults[0] = int(line[0])
        catagoryResults[1] = int(line[1]) + 1
    if (betResult[0] == float(predictions[0]) and flip == False) or (betResult[0] != float(predictions[0]) and flip == True):
        earned = bet + bet * 0.9191
        results[0] = int(results[0]) + 1
        # print("spread correct")
        if betResult[0] == float(predictions[0]) and flip == False:
            catagoryResults[0] += 1
        # elif betResult[0] != float(predictions[0]) and flip == True:
            # print("THE FLIP WORKED\n\n\n")
    
    with open('TestData/TrainingResults/' + catagory[predictions[2]], 'w') as file:
        file.write(str(catagoryResults[0]) + ',' + str(catagoryResults[1]) + ',')
    
    
    if betResult[1] == float(predictions[1]):
        earned = earned + bet + bet * 0.9191
        results[2] = int(results[2]) + 1
        # print("over correct")

    with open('TestData/TrainingData/daysBets.txt', 'r') as file:
        total = float(file.read())
        total = total + earned

    with open ('TestData/TrainingData/daysBets.txt', 'w') as file:
        file.write(str(total))
    # print("captial = " + str(capital))

    with open ('TestData/TrainingResults/results.csv', 'w') as file:
        file.write(str(results[0]) + ',' + str(results[1]) + ',' + str(results[2]) + ',' + str(results[3]) + ',')


def getPredictions(game):
    i = 0
    with open ('TestData/TrainingData/' + season + '/Predictions.csv', 'r') as file:
        for line in file:
            if i == game:
                return line.split(',')
            i += 1

            


############################################################
###### This is the beginning of the training program  ######
############################################################

subprocess.call(['python', 'TestData/src/Reset.py'])

if os.path.exists('TestData/TrainingData/' + season + '/NBA'):
    shutil.rmtree('TestData/TrainingData/' + season + '/NBA')
os.mkdir('TestData/TrainingData/' + season + '/NBA')



with open('TestData/TrainingData/' + season + '/GamesSimple.csv', "r") as file:
    lines = file.readlines()  # Read all lines into a list
    numDays = 1
    numGames = 1
    predictOutcome = False

    ### Loops through each game of the season
    for i in range(0, len(lines), 2):
        print("Day: " + str(numDays) + " Game: " + str(numGames))

        team1 = lines[i].strip()  # Get the first line of the pair
        if i + 1 < len(lines):
            team2 = lines[i + 1].strip()  # Get the second line of the pair
        else:
            print("ERROR: Odd number of lines in file")
            exit(1)

        team1 = team1.split(',')
        team2 = team2.split(',')
        log["Date"] = team1[1]

        if team1[0] != team2[0]:
            print("Error: Game IDs do not match")
            print("Team1 = " + team1[0])
            print("Team2 = " + team2[0])
            break

        if team1[1] == day:     
            addGame(team1, team2, season)
            numGames = numGames + 1

        else:
            with open ('TestData/TrainingData/' + season + '/Predictions.csv' , 'w') as file:
                file.write('')

            if numDays > 20:
                subprocess.call(['python', 'src/python/predictor.py'])
                addResults(True, numDays)
                cutLosses()
            else:
                addResults(False, numDays)
            with open ('Games.csv' , 'w') as file:
                file.write('')
            day = team1[1]
            # input("Press Enter to continue...")
            addGame(team1, team2, season)
            numGames = 1
            numDays = numDays + 1
