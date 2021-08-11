class River: 
    
    def __init__(self, name, fish_in_river):
        self.name = name
        self.fish_in_river = fish_in_river

    def remove_fish(self):
        return self.fish_in_river.pop()

    def fish_count(self):
        return len(self.fish_in_river)