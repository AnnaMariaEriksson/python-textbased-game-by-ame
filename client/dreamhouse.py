class Dreamhouse:
    def __init__(self, size, bedrooms, city, country, size_of_yard, floors, price, is_in_countryside = False, has_yard = False):
        self.size = size
        self.bedrooms = bedrooms
        self.city = city
        self.country = country
        self.size_of_yard = size_of_yard
        self.floors = floors
        self.price = price
        self.is_in_countryside = is_in_countryside
        self.has_yard = has_yard

    def __repr__(self):
        description = f"Your dream house is at least {self.size} square meters big and has {self.bedrooms} bedrooms. It costs around {self.price} to buy or build (everything included, such as furniture). "
        if self.is_in_countryside:
            description += f"This dream house is not in a city, but in the countryside. "
        if self.is_in_countryside == False:
            description += f"Your dream house is in the city of {self.city}"
        description += f"The house has {self.floors} floors and is located in the country of {self.country}. "
        if self.has_yard:
            description += f"You also have a yard that is at least {self.size_of_yard}."

        return description