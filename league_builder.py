#!/usr/bin/env python3

import csv

CSV_FILE = "soccer_players.csv"
CSV_DELIMITER = ","
TEAMS_FILE = "teams.txt"
GUARDIANS_TEMPLATE = """Dear {},
{} is enrolled in the team {}.
The first practice will take place at the Foo Bar High School, Friday at 12:34AM.
"""

players = []
experienced_players = []
inexperienced_players = []
TEAMS = {
    "Sharks": [],
    "Dragons": [],
    "Raptors": []
}


def load_players():
    """Creates a list of players from a .csv file."""
    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file, delimiter=CSV_DELIMITER)
        rows = list(reader)
        for row in rows:
            players.append(row)


def divide_players_by_experience():
    """Creates two separate lists: players with and without experience."""
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)


def assign_players_to_teams():
    """Assigns one experienced and one inexperienced player to each team."""
    for i in range(len(experienced_players) // len(TEAMS)):
        for team in TEAMS.values():
            team.append(experienced_players.pop())
            team.append(inexperienced_players.pop())


def write_teams_file():
    """Writes a file listing all the team names and their players."""
    with open(TEAMS_FILE, "w") as file:
        for team_name, team_list in TEAMS.items():
            file.write(f"{team_name}\n")
            for player in team_list:
                file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
            file.write("\n")


def write_guardians_file():
    """Writes a file to each player with an invitation letter."""
    for team_name, team_list in TEAMS.items():
        for player in team_list:
            first_name, last_name = player["Name"].split()
            with open(f"{first_name}_{last_name}.txt", "w") as file:
                file.write(GUARDIANS_TEMPLATE.format(player["Guardian Name(s)"], player["Name"], team_name))


if __name__ == "__main__":
    load_players()
    divide_players_by_experience()
    assign_players_to_teams()
    write_teams_file()
    write_guardians_file()
