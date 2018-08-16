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
teams = {
    "Sharks": [],
    "Dragons": [],
    "Raptors": []
}


def load_players():
    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file, delimiter=CSV_DELIMITER)
        rows = list(reader)
        for row in rows:
            players.append(row)


def divide_players_by_experience():
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)


def assign_players_to_teams():
    for i in range(len(experienced_players) // len(teams)):
        for team in teams.values():
            team.append(experienced_players.pop())
            team.append(inexperienced_players.pop())


def write_teams_file():
    with open(TEAMS_FILE, "w") as file:
        for team_name, team_list in teams.items():
            file.write(f"{team_name}\n")
            for player in team_list:
                file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
            file.write("\n")


def write_guardians_file():
    for team_name, team_list in teams.items():
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
