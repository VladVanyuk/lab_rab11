from models import materialType

class Dishes:

    def __init__(self, price=0, capacity=0, manufacturerCountry="noCountry",
                 MaterialType=materialType.MaterialType.METALS):
        self.price = price
        self.capacity = capacity
        self.manufacturerCountry = manufacturerCountry
        self.materialType = materialType

    def __str__(self):
        return ('The price is {0}, capacity is {1}, it\'s from {2},'
                + 'material is {3} \n').format(self.price,
                                               self.capacity,
                                               self.manufacturerCountry,
                                               self.materialType, )


    def __repr__(self):
        return self.__str__()
