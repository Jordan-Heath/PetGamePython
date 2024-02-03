class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.energy = 100

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} is fed and happy!")

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} had a great time playing!")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is well-rested and energized!")

    def status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")
