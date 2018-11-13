import os
import unittest

from league_builder import *


class LeagueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run()

    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile(CSV_FILE))

    def test_divide_players_by_experience(self):
        self.assertEqual(len(players), 18)

    def test_assign_players_to_teams(self):
        self.assertEqual(len(TEAMS["Sharks"]), 6)
        self.assertEqual(len(TEAMS["Dragons"]), 6)
        self.assertEqual(len(TEAMS["Raptors"]), 6)
        self.assertEqual(len(players), 0)

    def test_write_teams_file(self):
        self.assertTrue(os.path.isfile(TEAMS_FILE))

    def test_write_guardians_file(self):
        for player in players:
            first_name, last_name = player["Name"].split()
            self.assertTrue(os.path.isfile(f"{first_name}_{last_name}.txt"))

    @classmethod
    def tearDownClass(cls):
        players.clear()
        experienced_players.clear()
        inexperienced_players.clear()
        TEAMS["Sharks"].clear()
        TEAMS["Dragons"].clear()
        TEAMS["Raptors"].clear()


if __name__ == "__main__":
    unittest.main()
