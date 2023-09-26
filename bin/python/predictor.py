import csv
import os
from spreadCalculator import spread
from overCalculator import over
from output import output
from output import clear
from output import testOutput
from statsIntperpretor import streakProbability

TRAINING = True
SEASON = "2018"

stats = {
            "home": 
            {
                "overCur": 
                {
                    "over": 0, "overStrk": 0
                },
                "overSuccess":
                {
                    "over": 0, "overStrk": 0
                },
                "spread":
                {
                    "spread": 0, "spreadStrk": 0
                }
            },
            "away": 
            {
                "overCur": 
                {
                    "over": 0, "overStrk": 0
                },
                "overSuccess":
                {
                    "over": 0, "overStrk": 0
                },
                "spread":
                {
                    "spread": 0, "spreadStrk": 0
                }
            },
            "total":
            {
                "overCur": 0, "overCurStrk": 0, 
                "overSuccess": 0, "overSuccessStrk": 0, 
                "spread": 0, "spreadStrk": 0,
            },
            "homeTeam": "",
            "awayTeam": "",
            "spread": 0,
            "over": 0
        }

def changeDir():
    if os.getcwd().endswith('src'):
        os.chdir('..')


changeDir()
clear()
with open('Games.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        stats["homeTeam"] = row[0]
        stats["awayTeam"] = row[1]
        stats["spread"] = row[2]
        stats["over"] = row[3]
        stats = over(stats, TRAINING, SEASON)
        stats = spread(stats, TRAINING, SEASON)
        stats = streakProbability(stats)
        if TRAINING:
            testOutput(stats, SEASON)
        else:
            output(stats)
        line_count += 1
