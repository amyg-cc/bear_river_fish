import unittest
from src.bear import Bear
from src.river import River
from src.fish import Fish

class TestBear(unittest.TestCase):
    
    def setUp(self):
        self.bear = Bear("Yogi", "grizzly")
        self.fish1 = Fish("Bob")
        self.fish2 = Fish("Harry")
        self.fish3 = Fish("Fred")
        self.river = River("Amazon", [self.fish1, self.fish2, self.fish3])

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear.name)

    def test_bear_has_type(self):
        self.assertEqual("grizzly", self.bear.type)

    def test_take_fish(self):
        self.bear.take_fish(self.river)
        self.assertEqual(1, len(self.bear.stomach))

    def test_roar(self):
        self.assertEqual("ROAR", self.bear.roar())

    def test_food_count(self):
        self.assertEqual(0, self.bear.food_count())