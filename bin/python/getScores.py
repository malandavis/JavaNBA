import requests
from variables import *

scores = {}

def checkValidTeam(team):
    if TEAMS.__contains__(team):
        return True
    return False

def findTeams(line, splitVal):
    teams = line.split(splitVal)
    team = teams.pop(0).lower()
    score = teams[0].split("</span>").pop(0)
    score = int(score)
    if team == "trail blazers":
        team = "blazers"
    if not checkValidTeam(team):
        print("Invalid team: " + team)
        print("Enter correct team name: ")
        team = input()
    dict = {team: score}
    return dict


def updateScores(scores, date):
    newLines = []
    newDate = date.split("-")[1] + "-" + date.split("-")[2] + "-" + date.split("-")[0]
    with open ("Games/NBA/" + SZN + "/Days/" + MONTH[int(date.split("-")[1])] + "/" + newDate + ".csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            teams = line.split(",")
            newLine = line[:-1] + "," + str(scores[teams[0]]) + "," + str(scores[teams[1]]) + '\n'
            newLines.append(newLine)
    with open ("Games/NBA/" + SZN + "/Days/" + MONTH[int(date.split("-")[1])] + "/" + newDate + ".csv", "w") as file:
        file.writelines(newLines)



print("Enter date (YYYY-MM-DD): ")
date = input()

            
url = "https://sports.yahoo.com/nba/scoreboard/?confId=&dateRange=" + date + "&schedState=2"

response = requests.get(url)
content = str(response.content)

# class="YahooSans Fw(400)! Fz(12px)!"><div class="Fw(n) Fz(12px)">
firstSplit = "class=\"YahooSans Fw(400)! Fz(12px)!\"><div class=\"Fw(n) Fz(12px)\">"
# </div></span></div><div class="Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)"><span class="YahooSans Fw(700)! Va(m) Fz(24px)!">
secondSplit = "</div></span></div><div class=\"Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)\"><span class=\"YahooSans Fw(700)! Va(m) Fz(24px)!\">"



games = content.split(firstSplit)
games.pop(0)


for i in games:
    scores.update(findTeams(i, secondSplit))

print(scores)
updateScores(scores, date)

    