from models import materialType
from models.dishes import Dishes

class Dinnerware(Dishes):
    def __init__(self, price=0, capacity=0, manufacturerCountry="noCountry", MaterialType=materialType.MaterialType.METALS, radius=0):
        super(Dinnerware, self).__init__(price, capacity, manufacturerCountry, MaterialType)
        self.radius = radius

    def __str__(self):
        return ('The price is {0}, capacity is {1}, it\'s from {2},'
                + 'material is {3},' + 'radius = {4} \n').format(self.price,
                                                                 self.capacity,
                                                                 self.manufacturerCountry,
                                                                 self.materialType,
                                                                 self.radius,)

    def __repr__(self):
        return self.__str__()
