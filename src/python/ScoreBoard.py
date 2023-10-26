# import requests
# from variables import *

# scores = {}

# def checkValidTeam(team):
#     if TEAMS.__contains__(team):
#         return True
#     return False

# def findTeams(line, splitVal):
#     teams = line.split(splitVal)
#     team = teams.pop(0).lower()
#     score = teams[0].split("</span>").pop(0)
#     score = int(score)
#     if team == "trail blazers":
#         team = "blazers"
#     if not checkValidTeam(team):
#         print("Invalid team: " + team)
#         print("Enter correct team name: ")
#         team = input()
#     dict = {team: score}
#     return dict

# def getDate():
#     print("Enter date (YYYY-MM-DD): ")
#     date = input()
#     return date

# date = getDate()
       
# url = "https://sports.yahoo.com/nba/scoreboard/?confId=&dateRange=" + date + "&schedState=2"

# response = requests.get(url)
# content = str(response.content)

# firstSplit = "class=\"YahooSans Fw(400)! Fz(12px)!\"><div class=\"Fw(n) Fz(12px)\">"
# secondSplit = "</div></span></div><div class=\"Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)\"><span class=\"YahooSans Fw(700)! Va(m) Fz(24px)!\">"

# games = content.split(firstSplit)
# games.pop(0)

# for i in games:
#     scores.update(findTeams(i, secondSplit))

# print(scores)


import requests
import tkinter as tk
from tkinter import messagebox
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

def get_scores():
    scores.clear()
    date = date_entry.get()
    url = "https://sports.yahoo.com/nba/scoreboard/?confId=&dateRange=" + date + "&schedState=2"

    try:
        response = requests.get(url)
        content = str(response.content)

        firstSplit = "class=\"YahooSans Fw(400)! Fz(12px)!\"><div class=\"Fw(n) Fz(12px)\">"
        secondSplit = "</div></span></div><div class=\"Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)\"><span class=\"YahooSans Fw(700)! Va(m) Fz(24px)!\">"

        games = content.split(firstSplit)
        games.pop(0)

        for i in games:
            scores.update(findTeams(i, secondSplit))

        scoreboard_text.config(state=tk.NORMAL)
        scoreboard_text.delete(1.0, tk.END)
        firstTeam = True
        for team1, score1 in scores.items():
            check = False
            if firstTeam == True:
                for team2, score2 in scores.items():
                    if check == True:
                        scoreboard_text.insert(tk.END, f"{team1} {score1} @ {team2} {score2}\n")
                        check = False
                    if team1 == team2:
                        check = True
            firstTeam = not firstTeam
        scoreboard_text.config(state=tk.DISABLED)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "An error occurred while fetching data.")

# Create the main window
root = tk.Tk()
root.title("NBA Scores App")

# Create a label and an entry for the date
date_label = tk.Label(root, text="Enter date (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Create a button to fetch scores
get_scores_button = tk.Button(root, text="Get Scores", command=get_scores)
get_scores_button.pack()

# Create a text widget to display the scoreboard
scoreboard_text = tk.Text(root, height=15, width=75)
scoreboard_text.pack()
scoreboard_text.config(state=tk.DISABLED)

root.mainloop()

