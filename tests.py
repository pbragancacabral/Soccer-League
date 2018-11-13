import os
import unittest

from league_builder import *


class LeagueTests(unittest.TestCase):
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile(CSV_FILE))

    def test_18_players_have_been_loaded(self):
        load_players()
        self.assertEqual(len(players), 18)


if __name__ == "__main__":
    unittest.main()
