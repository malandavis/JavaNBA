from variables import *

def didCover(spread, us, them):
    if us + spread > them:
        return "y"
    else:
        return "n"

def didOver(ou, us, them):
    if us + them > ou:
        return "y"
    else:
        return "n"


def updateTeam(arr, isHome):
    spread = float(arr[2])
    if isHome:
        team = arr[0]
    else:
        team = arr[1]
        temp = arr[5]
        arr[5] = arr[4]
        arr[4] = temp
        spread = spread * -1

    with open("Games/NBA/" + SZN + "/" + team + ".txt", "a") as file:
        file.write(str(spread) + " " + didCover(spread, float(arr[4]), float(arr[5])) + " " + arr[3] + " " + didOver(float(arr[3]), float(arr[4]), float(arr[5])) + " " + str(float(arr[4]) + float(arr[5])))
    

print("Enter date (YYYY-MM-DD): ")
date = input()
date = date.split("-")[1] + "-" + date.split("-")[2] + "-" + date.split("-")[0]

with open("Games/NBA/" + SZN + "/Days/" + MONTH[int(date.split("-")[0])] + "/" + date + ".csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        words = line.split(",")
        updateTeam(words, True)
        updateTeam(words, False)
        