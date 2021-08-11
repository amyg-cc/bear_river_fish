import unittest
from src.river import River
from src.fish import Fish
from src.bear import Bear

class TestRiver(unittest.TestCase):
    
    def setUp(self):
        self.fish1 = Fish("Bob")
        self.fish2 = Fish("Harry")
        self.fish3 = Fish("Fred")
        self.river = River("Tay", [self.fish1, self.fish2, self.fish3])

    def test_river_has_name(self):
        self.assertEqual("Tay", self.river.name)

    def test_river_has_fish(self):
        self.assertEqual(3, len(self.river.fish_in_river))

    def test_remove_fish(self):
        fish = self.river.remove_fish()
        self.assertEqual(self.fish3.name, fish.name)

    def test_fish_count(self):
        self.assertEqual(3, self.river.fish_count())