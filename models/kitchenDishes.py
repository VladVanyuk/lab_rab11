from models import cookingType
from models import workingType
from models import materialType
from models.dishes import Dishes

class KitchenDishes(Dishes):
    def __init__(self, price=0, capacity=0, manufacturerCountry="noCountry", MaterialType=materialType.MaterialType.METALS, WorkingType=workingType.FIRE, CookingType=cookingType.FORCOOKING):
        super(KitchenDishes, self).__init__(price, capacity, manufacturerCountry, MaterialType)
        self.workingType = workingType
        self.cookingType =cookingType

    def __str__(self):
        return ('The price is {0}, capacity is {1}, it\'s from {2},'
                + 'material is {3},' + 'it works on {4},' + 'type of cooking is {5} \n').format(self.price,
                                                                                                self.capacity,
                                                                                                self.manufacturerCountry,
                                                                                                self.materialType,
                                                                                                self.workingType,
                                                                                                self.cookingType,)


    def __repr__(self):
        return self.__str__()