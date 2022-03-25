class Pet:
    def __init__(self, name, age, species, color, favorite_toy):
        self.name = name
        self.species = species
        self.age = age
        self.color = color
        self.favorite_toy = favorite_toy

    def __repr__(self):
        description = f"""
        {self.name}
        {self.species}
        {self.age}
        {self.color}
        {self.favorite_toy}
        """
        return description
