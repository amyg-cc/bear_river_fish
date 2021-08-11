from src.river import River


class Bear: 
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def take_fish(self, river):
        fish = river.remove_fish()
        self.stomach.append(fish)
    
    def roar(self):
        return "ROAR"

    def food_count(self):
        return len(self.stomach)