from models import materialType
from models.dishes import Dishes
from models import storageType

class DishesForStorage(Dishes):
    def __init__(self, price=0, capacity=0, manufacturerCountry="noCountry", MaterialType=materialType.MaterialType.METALS, StorageType=storageType.StorageType.FOOD):
        super(DishesForStorage, self).__init__(price, capacity, manufacturerCountry, MaterialType)
        self.storageType = storageType

    def __str__(self):
        return ('The price is {0}, capacity is {1}, it\'s from {2},'
                + 'material is {3},' + 'storage type is {4} \n').format(self.price,
                                                                 self.capacity,
                                                                 self.manufacturerCountry,
                                                                 self.materialType,
                                                                 self.storageType,)

    def __repr__(self):
        return self.__str__()

