import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):
    
    def setUp(self):
        self.fish = Fish("Alan")

    def test_fish_has_name(self):
        self.assertEqual("Alan", self.fish.name)