import requests

SPORT = "nba/"
# SPORT = "mlb/"

TEAMS = {
    "76ers", "blazers", "bucks", "bulls", "cavaliers", "celtics", "clippers", "grizzlies", "hawks", "heat", "hornets", "jazz", "kings", "knicks", "lakers", "magic",
    "mavericks", "nets", "nuggets", "pacers", "pelicans", "pistons", "raptors", "rockets", "spurs", "suns", "thunder", "timberwolves", "warriors", "wizards"
    }

ABBR = {
    "ATL": "hawks", "BOS": "celtics", "BKN": "nets", "CHA": "hornets", "CHI": "bulls", "CLE": "cavaliers", "DAL": "mavericks", "DEN": "nuggets", "DET": "pistons", 
    "GS": "warriors", "HOU": "rockets", "IND": "pacers", "LAC": "clippers", "LAL": "lakers", "MEM": "grizzlies", "MIA": "heat", "MIL": "bucks", "MIN": "timberwolves",
    "NOP": "pelicans", "NYK": "knicks", "OKC": "thunder", "ORL": "magic", "PHI": "76ers", "PHX": "suns", "POR": "blazers", "SAC": "kings", "SA": "spurs",
    "TOR": "raptors", "UTA": "jazz", "WAS": "wizards"
    }
todaysTeams = []
spreads = {}
ou = []

def teamParser(line):
    game = line.split("class=\"C(primary-text)")
    game.pop()
    game = game.pop()
    game = game.split(SPORT)
    game = game.pop()
    team = game.split("-")
    for i in team:
        if TEAMS.__contains__(i):
            todaysTeams.append(i)

def ouParser(line):
    if not line.__contains__("around") or not line.__contains__("favored"):
        ou.append("0")
        spreads.update({"NA": "0"})
        return False
    game = line.split("around ")
    game = game.pop()
    game = game.split(" combined")
    game.pop()
    ou.append(game.pop())
    return True

def spreadParser(line):
    game = line.split("</span></div><div class=\"odds total")
    game.pop()
    game = game.pop()
    game = game.split("\"><span class=\"Tt(u)\">")
    game = game.pop()
    game = game.split("</span><span class=\"Px(4px)\">")
    spread = game.pop()
    game = game.pop()
    favorite = ABBR[game]
    spreads.update({favorite: spread})
            


# url = "https://web.archive.org/web/20230214005823/https://sports.yahoo.com/nba/scoreboard/"
url = "https://web.archive.org/web/20230106091601/https://sports.yahoo.com/nba/scoreboard/"
# url = "https://web.archive.org/web/20230102110344/https://sports.yahoo.com/nba/scoreboard/"

response = requests.get(url)
content = str(response.content)
firstSplit = ">Upcoming<"



if content.__contains__(">Postponed<"):
    firstSplit = ">Postponed<"


upcoming = content.split(firstSplit)
upcoming = upcoming.pop()
games = upcoming.split("\"sticky-outer-wrapper\"")
games.pop()
games = games.pop()
games = games.split("href")

first_iteration = True
for i in games:
    if not first_iteration:
        # print(i)
        # print("\n\n\n")
        teamParser(i)
        if ouParser(i):
            spreadParser(i)
    else:
        first_iteration = False

with open('Games.csv', 'w') as file:
    for i in range(0, len(todaysTeams), 2):
        if not ou[int(i/2)] == "0":
            away = list(todaysTeams)[i]
            home = list(todaysTeams)[i+1] if i+1 < len(todaysTeams) else None
            print(home + " VS " + away)
            if spreads.__contains__(away):
                spreads[away] = str(float(spreads[away]) * -1)
                file.write(home + "," + away + "," + spreads[away] + "," + ou[int(i/2)] + "\n")
            else:
                file.write(home + "," + away + "," + spreads[home] + "," + ou[int(i/2)] + "\n")

