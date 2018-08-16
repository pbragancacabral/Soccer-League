import csv

PLAYERS = []
EXPERIENCED_PLAYERS = []
INEXPERIENCED_PLAYERS = []
DRAGONS, SHARKS, RAPTORS = [], [], []


def add_players_from_file_to_list():
    players = []
    with open("soccer_players.csv", newline="") as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)
        for row in rows:
            players += [row]
    return players


def separate_by_experience(players):
    experienced = []
    inexperienced = []
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced += [player]
        else:
            inexperienced += [player]
    return experienced, inexperienced


def assign_players_to_teams(experienced, inexperienced):
    teams = []
    for index, player in zip(range(len(experienced)), inexperienced):
        teams = [DRAGONS, SHARKS, RAPTORS]
        teams[index % 3] += [player]

    for index, player in zip(range(len(experienced)), inexperienced):
        teams = [DRAGONS, SHARKS, RAPTORS]
        teams[index % 3] += [player]
    return teams


def write_file_with_teams():
    with open("teams.txt", "w") as file:
        file.write("DRAGONS\n")
        for player in DRAGONS:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
        file.write("\n")

        file.write("SHARKS\n")
        for player in SHARKS:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")
        file.write("\n")

        file.write("RAPTORS\n")
        for player in RAPTORS:
            file.write(f"{player['Name']}, {player['Soccer Experience']}, {player['Guardian Name(s)']}\n")


def write_individual_letters_to_guardians():
    for player in DRAGONS:
        first_name, last_name = player["Name"].split()
        with open(f"{first_name}_{last_name}.txt", "w") as file:
            file.write(f"Dear {player['Guardian Name(s)']}, {player['Name']} as been selected to play for DRAGONS with "
                       "first practice next Sunday at 13:00")

    for player in SHARKS:
        first_name, last_name = player["Name"].split()
        with open(f"{first_name}_{last_name}.txt", "w") as file:
            file.write(f"Dear {player['Guardian Name(s)']}, {player['Name']} as been selected to play for SHARKS with "
                       "first practice next Sunday at 13:00")

    for player in RAPTORS:
        first_name, last_name = player["Name"].split()
        with open(f"{first_name}_{last_name}.txt", "w") as file:
            file.write(f"Dear {player['Guardian Name(s)']}, {player['Name']} as been selected to play for RAPTORS with "
                       "first practice next Sunday at 13:00")


if __name__ == "__main__":
    PLAYERS = add_players_from_file_to_list()
    EXPERIENCED_PLAYERS, INEXPERIENCED_PLAYERS = separate_by_experience(PLAYERS)
    DRAGONS, SHARKS, RAPTORS = assign_players_to_teams(EXPERIENCED_PLAYERS, INEXPERIENCED_PLAYERS)
    write_file_with_teams()
    write_individual_letters_to_guardians()
